import streamlit as st
import streamlit.components.v1 as components

# Título do seu site
st.title("Verificador de Fases da Vida 🧬")

# Entrada de idade
idade = st.number_input("Qual sua idade?", min_value=0, max_value=150, value=18)

if idade <= 3:
    st.write("Você é um/a bebê, não consegue fazer nada sozinho/a e depende dos seus pais.")
elif idade <= 5:
    st.write("Você é criancinha, ainda não começou o ensino fundamental 1.")
elif idade <= 7:
    st.write("Você é criança, já começou o ensino fundamental mas não consegue se virar sozinho/a.")
elif idade <= 12:
    st.write("Você é criança, já consegue se virar sozinho/a um pouco.")
elif idade <= 16:
    st.write("Você é adolescente, consegue se virar sozinho, mas ainda precisa dos pais.")
elif idade <= 30:
    st.write("Você é adulto/a, já trabalha e tem que pagar as contas, talvez faz faculdade.")
elif idade <= 60:
    st.write("Você é adulto/a, já trabalha e tem que pagar as contas, talvez tenha filhos.")
elif idade <= 99:
    st.write("Você é velho/a, você já está com dor na lombar e joga bingo.")
elif idade <= 150:
    st.write("Você é um/a esqueleto/a.")
else:
    st.write("Você já virou pó, nem existe.")

# --- ESPAÇO PARA O ANÚNCIO ---
st.write("---") # Uma linha para separar o conteúdo do anúncio
components.html(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4581971001324005"
     crossorigin="anonymous"></script>
    
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-4581971001324005"
         data-ad-slot="SEU_NUMERO_DE_SLOT_AQUI"
         data-ad-format="auto"
         data-full-width-responsive="true"></ins>
         
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
    """,
    height=300, # Aumentei a altura para o anúncio não ser cortado
