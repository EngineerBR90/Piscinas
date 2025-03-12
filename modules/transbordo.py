# transbordo.py
import math
import streamlit as st

BANCO_BOMBAS = [
    # ... (mantenha a mesma lista de dicionários que você forneceu)
]

def run():
    st.title("🌊 Módulo de Transbordo")
    st.markdown("---")
    
    # Container principal
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            # Inputs do usuário
            altura_lamina_mm = st.number_input(
                "Altura da lâmina (mm)",
                min_value=1.0,
                step=0.5,
                format="%.1f"
            )
            comprimento_borda_m = st.number_input(
                "Comprimento total da borda infinita (m)",
                min_value=0.1,
                step=0.1,
                format="%.1f"
            )
            area_piscina_m2 = st.number_input(
                "Área da piscina (m²)",
                min_value=1.0,
                step=0.5,
                format="%.1f"
            )
            
        with col2:
            # Seleção de pressão
            possible_pressures = sorted({2,4,6,8,10,12,14,16,18})
            pressao_mca = st.selectbox(
                "Pressão dimensionada (m.c.a)",
                options=possible_pressures,
                index=2  # Valor padrão 6 m.c.a
            )
    
    # Cálculos e resultados
    if st.button("Calcular", type="primary"):
        with st.spinner("Calculando..."):
            # Realiza cálculos
            volume_cocho_litros = area_piscina_m2 * (altura_lamina_mm / 1000) * 1000
            area_lamina_m2 = (altura_lamina_mm / 1000) * comprimento_borda_m
            vazao_necessaria = (1608 * (altura_lamina_mm / 1000) * comprimento_borda_m) * math.sqrt(2 * 9.81 * (altura_lamina_mm / 1000))
            
            # Seleção da bomba
            selected_pump = None
            for bomba in BANCO_BOMBAS:
                key = f"vazao_{pressao_mca}_mca"
                vazao_pump = bomba.get(key)
                
                if vazao_pump is not None and vazao_pump >= vazao_necessaria:
                    selected_pump = bomba
                    break
            
            # Exibe resultados
            st.success("**Resultados do Dimensionamento**")
            
            # Layout em colunas
            res_col1, res_col2 = st.columns([1, 2])
            
            with res_col1:
                st.metric("Vazão Necessária", f"{vazao_necessaria:.2f} m³/h")
                st.metric("Volume do Coche", f"{volume_cocho_litros:.2f} L")
                st.metric("Área da Lâmina", f"{area_lamina_m2:.4f} m²")
                
                if selected_pump:
                    st.success(f"**Motobomba Selecionada:** {selected_pump['modelo']}")
                    st.metric("Potência", f"{selected_pump['potencia_cv']} CV")
                else:
                    st.error("Nenhuma motobomba adequada encontrada!")
                
            with res_col2:
                if selected_pump:
                    with st.expander("🔍 Detalhes da Motobomba"):
                        st.write(f"**Especificações Técnicas:**")
                        st.write(f"- Modelo: {selected_pump['modelo']}")
                        st.write(f"- Potência: {selected_pump['potencia_cv']} CV")
                        st.write(f"- Vazão em {pressao_mca} m.c.a: {selected_pump[f'vazao_{pressao_mca}_mca']} m³/h")
                        
                        st.write("**Outras Vazões:**")
                        for press in possible_pressures:
                            key = f"vazao_{press}_mca"
                            if selected_pump.get(key):
                                st.write(f"- {press} m.c.a: {selected_pump[key]} m³/h")
                else:
                    st.warning("""
                    **Recomendações:**
                    - Verificar se a pressão selecionada é adequada
                    - Considerar associação de múltiplas bombas
                    - Consultar modelos com maior capacidade
                    """)
            
            st.markdown("---")
    
    if st.button("Voltar ao Menu Principal"):
        st.session_state.current_page = "Menu Principal"
        st.rerun()

# Para testar individualmente
if __name__ == "__main__":
    run()