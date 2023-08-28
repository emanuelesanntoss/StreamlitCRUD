#https://www.youtube.com/watch?v=lOyCICREgy8
from os import write;
from numpy.core.fromnumeric import size;
import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente

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
    cliente.nome = input_name
    cliente.idade = input_age
    cliente.profissao = input_occupation
    
    ClienteController.Incluir(cliente)
    st.success("Cliente incluído com sucesso")
    