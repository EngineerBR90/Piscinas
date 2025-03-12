# filtragem.py
import streamlit as st

BANCO_FILTROS = [
    # ... (mantenha a mesma lista de dicionários que você forneceu)
]

def run():
    st.title("🔧 Módulo de Filtragem")
    st.markdown("---")
    
    # Input do volume
    volume = st.number_input(
        "Digite o volume total da piscina (m³)",
        min_value=1.0,
        step=0.5,
        format="%.1f"
    )
    
    # Container para resultados
    result_container = st.container()
    
    if st.button("Calcular", type="primary"):
        # Seleção do filtro
        filtro_selecionado = None
        for filtro in sorted(BANCO_FILTROS, key=lambda x: x["volume_6h"]):
            if filtro["volume_6h"] >= volume:
                filtro_selecionado = filtro
                break
        
        if not filtro_selecionado:
            st.error("Nenhum filtro disponível suporta este volume!")
            return

        # Exibição dos resultados
        with result_container:
            st.success("**Resultados do Dimensionamento**")
            
            # Layout em colunas
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.metric("Filtro Selecionado", filtro_selecionado["modelo"])
                st.metric("Vazão Necessária", f"{filtro_selecionado['volume_6h']} m³/h")
                st.metric("Motobomba Recomendada", filtro_selecionado["modelo_motobomba"])
            
            with col2:
                with st.expander("🔍 Detalhes Técnicos do Filtro"):
                    st.write(f"**Capacidade:**")
                    st.write(f"- 6 horas: {filtro_selecionado['volume_6h']} m³")
                    st.write(f"- 8 horas: {filtro_selecionado['volume_8h']} m³")
                    
                    st.write(f"**Dimensões:**")
                    st.write(f"- Diâmetro: {filtro_selecionado['diametro_mm']} mm")
                    st.write(f"- Altura: {filtro_selecionado['altura_mm']} mm")
                    
                    st.write(f"**Carga de Areia:**")
                    st.write(f"- Total: {filtro_selecionado['carga_areia_kg']} kg")
                    st.write(f"- Sacos de 25kg: {filtro_selecionado['quant_sacos_25kg']}")
                    
                    st.write(f"**Peso:**")
                    st.write(f"- Com areia: {filtro_selecionado['peso_bruto_com_areia_kg']} kg")
                    st.write(f"- Sem areia: {filtro_selecionado['peso_bruto_sem_areia_kg']} kg")
            
            st.markdown("---")
    
    if st.button("Voltar ao Menu Principal"):
        st.session_state.current_page = "Menu Principal"
        st.rerun()

# Para testar individualmente
if __name__ == "__main__":
    run()