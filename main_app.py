import streamlit as st
from modules import filtragem, transbordo

def main():
    st.set_page_config(page_title="Sistema Piscinas", layout="wide")
    
    # Menu lateral
    with st.sidebar:
        st.title("Menu")
        pagina = st.radio("Escolha o módulo:", 
                        ["Home", "Filtragem", "Transbordo"])
    
    # Navegação
    if pagina == "Home":
        st.title("Bem-vindo!")
        st.write("Selecione um módulo na barra lateral 👈")
    elif pagina == "Filtragem":
        filtragem.run()
    elif pagina == "Transbordo":
        transbordo.run()

if __name__ == "__main__":
    main()
