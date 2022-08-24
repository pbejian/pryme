import streamlit as st

def espace(n):
    """
    Cette fonction ne renvoie rien mais affiche n ligne vide
    dans une application streamlit.
    """
    for _ in range(n):
        st.write("")
    return None


def plus_petit_diviseur(n):
    """
    In  : un entier positif n (plus grand que 2)
    Out : le plus petit diviseur d de n entre 2 et n (si d=n cela signifie
          que n est premier).
    """
    for d in range(2, n+1):
        if (n % d) == 0:
            return d


def factorisation(n):
    """
    In  : un entier positif n (plus grand que 2)
    Out : la décomposition de n en facteurs premiers sous la forme d'une
          liste [[p_1,a_1], [p_2,a_2], [p_r,a_r]] dans laquelle les p_i
          sont les facteurs premiers de n et les a_i sont les valuations
          associées. 
    """
    L = []
    m = n
    while m != 1:
        p = plus_petit_diviseur(m)
        a = 0
        while (m % p**a) == 0:
            a = a + 1
        L.append([p, a-1])
        m = m//(p**(a-1))
    return L


def factorisation_en_latex(L):
    """
    In  : une liste L représentant la décomposition d'un entier n en facteur
          premier, exactement comme expliqué dans la docstring de la fonction
          factorisation(n)
    Out : une chaîne de caractère R qui est exactement l'écriture en LaTeX de 
          la décomposition en facteurs premier décrite par L
    """
    R = "n = "
    for i in range(len(L)-1):
        X = L[i]
        p = X[0]
        a = X[1]
        R = R + f"{p}^{a}\\times"
    # Dernière étape, sans le symbole 'times' :
    i = len(L)-1
    X = L[i]
    p = X[0]
    a = X[1]
    R = R + f"{p}^{a}"
    return R