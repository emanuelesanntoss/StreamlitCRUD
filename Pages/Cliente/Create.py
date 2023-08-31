import streamlit as st
import Controllers.ClienteController as ClienteController
from models.Cliente import Cliente

def Create():
    idAlteracao = st.experimental_get_query_params().get("id")
    clienteRecuperado = None
    
    if idAlteracao is not None:
        idAlteracao = idAlteracao[0]
        clienteRecuperado = ClienteController.selecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[clienteRecuperado.id]
        )
        
    else:
        st.title("Incluir cliente")

    # Criar formulário
    with st.form(key="include_cliente"):
        listOccupation = ["Selecione...","Desenvolvedor","Analista","Gerente de projeto","Agilista"]
        if clienteRecuperado is None:
            input_name = st.text_input(label="Insira o seu nome")
            input_age = st.number_input(label="Insira a sua idade", format="%d", step=1)
            input_occupation = st.selectbox(
                "Selecione sua profissão", options=listOccupation)
        else:
            input_name = st.text_input(label="Insira o seu nome", value=clienteRecuperado.nome)
            input_age = st.number_input(label="Insira a sua idade", format="%d", step=1, value=clienteRecuperado.idade)
            
            selected_index = listOccupation.index(clienteRecuperado.profissao) if clienteRecuperado.profissao in listOccupation else 0
            
            input_occupation = st.selectbox(
                "Selecione sua profissão",
                options=listOccupation,
                index=selected_index  # Defina o índice selecionado com base no valor recuperado
            )

        input_button_submit = st.form_submit_button("Enviar")

        # Função do botão enviar
        if input_button_submit:
            if clienteRecuperado is None:
                new_client = Cliente(0, input_name, input_age, input_occupation)
                ClienteController.Incluir(new_client)
                st.success("Cliente incluído com sucesso")
            else:
                st.experimental_set_query_params()
                clienteRecuperado.nome = input_name
                clienteRecuperado.idade = input_age
                clienteRecuperado.profissao = input_occupation
                ClienteController.Alterar(clienteRecuperado)
                st.success("Cliente alterado com sucesso")
