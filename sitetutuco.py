import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Fases da Vida", layout="centered")

st.title("Verificador de Fases da Vida 🧬")

idade = st.number_input("Qual sua idade?", min_value=0, max_value=150, value=18)

# Lógica das fases
if idade <= 3:
    st.write("Você é um/a bebê, depende dos seus pais.")
elif idade <= 5:
    st.write("Você é criancinha, ainda não começou o ensino fundamental 1.")
elif idade <= 7:
    st.write("Você é criança, já começou o ensino fundamental.")
elif idade <= 12:
    st.write("Você é criança, já consegue se virar um pouco.")
elif idade <= 16:
    st.write("Você é adolescente, mas ainda precisa dos pais.")
elif idade <= 30:
    st.write("Você é adulto/a, já trabalha e paga contas.")
elif idade <= 60:
    st.write("Você é adulto/a, talvez tenha filhos.")
elif idade <= 99:
    st.write("Você é velho/a, talvez tenha dor na lombar.")
elif idade <= 150:
    st.write("Você é um/a esqueleto/a.")
else:
    st.write("Você já virou pó.")

st.divider()

components.html(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4581971001324005"
     crossorigin="anonymous"></script>
    <div style="text-align: center; color: gray; font-size: 12px;">Publicidade</div>
    """,
    height=100
)
