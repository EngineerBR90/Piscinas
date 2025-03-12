import streamlit as st
from modules import filtragem, transbordo

def main():
    st.set_page_config(
        page_title="SisHidro Piscinas",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Sidebar Navigation
    with st.sidebar:
        st.image("assets/logo_fx2.png", width=100)
        st.title("Navegação")
        page = st.radio("Selecione o módulo:", 
                       ["Menu Principal", "Filtragem", "Transbordo", "Hidromassagem", "Cascatas", "Aquecimento"])
    
    # Page Routing
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Menu Principal"
    
    if page != st.session_state.current_page:
        st.session_state.current_page = page
        st.rerun()
    
    # Page Content
    if st.session_state.current_page == "Menu Principal":
        show_home()
    elif st.session_state.current_page == "Filtragem":
        filtragem.run()
    elif st.session_state.current_page == "Transbordo":
        transbordo.run()
    elif st.session_state.current_page == "Hidromassagem":
        st.warning("Módulo em desenvolvimento! 🚧")
    elif st.session_state.current_page == "Cascatas":
        st.warning("Módulo em desenvolvimento! 🚧")
    elif st.session_state.current_page == "Aquecimento":
        st.warning("Módulo em desenvolvimento! 🚧")
 

def show_home():
    st.title("SisHydro Piscinas")
    st.markdown("""
    ### Ferramentas para dimensionamento sistemas hidráulicos para piscinas
    
    **Recursos Disponíveis:**
    - Sistema de filtragem com seleção automática de conjunto Filtro+MB
    - Cálculo de vazão necessária para sistemas de transbordo (borda infinita)
    - Banco de dados técnicos sobre equipamentos (Sodramar database)

     **Módulos em desenvolvimento:**
     - Hidromassagem
     - Cascatas 
     - Aquecimento por trocador de calor elétrico (engenharia reversa da PLANILHA DE DIMENSIONAMENTO SODRAMAR)
     - Verificação de velocidade de fluxo em linhas de sucção conforme NBR 10.339:2018 (módulo pronto, falta adaptar UI)
     - Verificação de suscetibilidade à cavitação
    """)
    
    #st.image("assets/logo_fx2.png", use_container_width=True)

if __name__ == "__main__":
    main()
