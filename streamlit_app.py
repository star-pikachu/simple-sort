import streamlit as st
import numpy as np

def main():
    # hide button
    hide_menu = """
    <style>
    header {
        visibility: hidden;
    }
    # MainMenu {
        visibility: hidden;
    }
    
    footer {
        visibility: hidden;
    }
    </style>
    """
    st.markdown(hide_menu, unsafe_allow_html=True)
    
    st.title("Простейшие алгоритмы сортировки")


if __name__ == "__main__":
    main()
