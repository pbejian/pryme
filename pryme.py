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


def display_factorization(L):
    R = "n = "
    for i in range(len(L)-1):
        X = L[i]
        p = X[0]
        a = X[1]
        R = R + f"{p}^{a}\\times"
    # Last step, without the 'times symbol':
    i = len(L)-1
    X = L[i]
    p = X[0]
    a = X[1]
    R = R + f"{p}^{a}"
    # The function return None but display the result string
    st.latex(R)
    return None


#-------------------------------------------------------------------------------

n = int(st.text_input("Choisir un nombre entier n et valider : ", 2))
d = smallest_divisor(n)
L = factorization(n)

st.write("Voici la décomposition de n :")
display_factorization(L)

#-------------------------------------------------------------------------------