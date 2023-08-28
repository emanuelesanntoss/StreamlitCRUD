import streamlit as st;

#Titulo
st.title("Incluir cliente")

#Criar formulário
with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Insira a sua idade", format ="%d", step=1) # formata para numero inteiro format ="%d", step=1
    input_occupation = st.selectbox("Selecione sua profissão", ["Selecione...","Desenvolvedor", "Analista", "Gerente de projeto", "Agilista"])
    input_button_submit = st.form_submit_button("Enviar")
    
#Funcao do botão enviar
if input_button_submit:
    st.write(f'Nome: {input_name}')
    st.write(f'Idade: {input_age}')
    st.write(f'Profissão: {input_occupation}')
    