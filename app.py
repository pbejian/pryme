#-------------------------------------------------------------------------------
# Importation des modules

import streamlit as st
import include as inc

#-------------------------------------------------------------------------------
# Application principale

st.title("Pryme")

st.write("""
    ### Décomposition d'un entier en facteurs premiers
    """)

inc.espace(1)

n = int(st.text_input("Choisir un nombre entier n et valider : ", 2))
L = inc.factorisation(n)
S = inc.factorisation_en_latex(L)
st.write("Voici la décomposition de n :")
st.latex(S)

#-------------------------------------------------------------------------------
# Conclusion avec le lien vers les sources sur GitHub

st.markdown("""
    <hr>
""", unsafe_allow_html=True)

inc.espace(2)

st.write("""
    📝 Sources de l'application :
    [https://github.com/pbejian/pryme](https://github.com/pbejian/pryme)
""")
#-------------------------------------------------------------------------------