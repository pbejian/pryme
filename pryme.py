#-------------------------------------------------------------------------------

import streamlit as st

#-------------------------------------------------------------------------------

st.title("Pryme")

st.write("""
    ### Décomposition d'un nombre entier en facteurs premiers


""")
st.write(" ")

#-------------------------------------------------------------------------------

n = int(st.text_input("Choisir un nombre entier n et valider : ", 2))

st.latex(f"n = {n}")


