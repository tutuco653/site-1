import streamlit as st
import streamlit.components.v1 as components

# Título do seu site
st.title("Verificador de Fases da Vida 🧬")

# O primeiro número é o valor inicial (18)
# O min_value garante que ninguém digite número negativo
idade = st.number_input("Qual sua idade?", min_value=0, max_value=150, value=18)

if idade <= 3:
    st.write("voce e um/a bebe, nao consegue fazer nada sozinho/a e depende dos seus pais")

elif idade <= 5:
    st.write("voce e criançinha, ainda nao começou o ensino fundamental 1")

elif idade <= 7:
    st.write("voce e criança, ja começou o ensino fundamental mas nao consegue se virar sozinho/a")

elif idade <= 12:
    st.write("voce e criança, ja consegue se virar sozinho/a um pouco")

elif idade <= 16:
    st.write("voce e adolecente, consegue se virar sozinho, mas ainda precisa dos pais")
    
elif idade <= 30:
    st.write("voce e adulto/a, ja trabalha e tem que pagar as contas, talves faz faculdade")
             
elif idade <= 60:
    st.write("voce e adulto/a, ja trabalha e tem que pagar as contas, talves faz esteja na faculdade e talvez tem filhos")

elif idade <= 99:
    st.write("voce e velho/a voce ja esta com dor na lombar e joga bingo")

elif idade <= 150:
    st.write("voce e um/a esqueleto/a")

else:
    st.write("voce ja virou po, nem existe")

# --- ÁREA DA PROPAGANDA (CONSERTADA) ---
# Colocamos o código dentro do components.html para o Python não dar erro
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4581971001324805"
     crossorigin="anonymous"></script>
