#-------------------------------------------------------------------------------

import streamlit as st

#-------------------------------------------------------------------------------

st.title("Pryme")

st.write("""
    ### Décomposition d'un nombre entier en facteurs premiers

""")
st.write(" ")

#-------------------------------------------------------------------------------
# Ici figure le code principal

def smallest_divisor(n):
    for d in range(2, n+1):
        if (n % d) == 0:
            return d

def factorization(n):
    L = []
    m = n
    while m != 1:
        p = smallest_divisor(m)
        a = 0
        while (m % p**a) == 0:
            a = a + 1
        L.append([p, a-1])
        m = m//(p**(a-1))
    return L





#-------------------------------------------------------------------------------

n = int(st.text_input("Choisir un nombre entier n et valider : ", 2))
d = smallest_divisor(n)
L = factorization(n)

st.latex(f"n = {n}")
st.latex(f"d = {d}")
st.latex(f"L = {L}")
