import streamlit as st
import Controllers.ClienteController as ClienteController

def Edit(cliente_id):
    st.title("Editar cliente")
    
    # Carregar os detalhes do cliente com base no ID
    cliente = ClienteController.selecionarClientePorId(cliente_id)
    
    if not cliente:
        st.error("Cliente não encontrado.")
        return

    # Criar formulário com os detalhes do cliente
    with st.form(key="edit_cliente"):
        input_name = st.text_input(label="Nome", value=cliente.nome)
        input_age = st.number_input(label="Idade", value=cliente.idade, format="%d", step=1)
        input_occupation = st.selectbox(
            "Profissão",
            [
                "Desenvolvedor",
                "Analista",
                "Gerente de projeto",
                "Agilista",
            ],
            index=0 if cliente.profissao is None else cliente.profissao
        )
        input_button_submit = st.form_submit_button("Salvar Alterações")

    # Atualizar o cliente no banco de dados se o botão "Salvar Alterações" for clicado
    if input_button_submit:
        cliente.nome = input_name
        cliente.idade = input_age
        cliente.profissao = input_occupation
        ClienteController.atualizarCliente(cliente)
        st.success("Cliente atualizado com sucesso.")
