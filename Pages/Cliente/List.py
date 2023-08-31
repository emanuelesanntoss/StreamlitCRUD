import streamlit as st
import Controllers.ClienteController as ClienteController
import Pages.Cliente.Create as PageCreateCliente

def List(customerList):
    paramId = st.experimental_get_query_params().get("id")
    st.experimental_set_query_params()

    if not paramId:
        st.title("Lista de Clientes")

        colms = st.columns((1, 2, 1, 2, 1, 1))
        campos = ['Nº', 'Nome', 'Idade', 'Profissão', 'Excluir', 'Alterar']

        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for item in customerList:  # Use a lista passada como argumento
            col1, col2, col3, col4, col5, col6 = st.columns((1, 2, 1, 2, 1, 1))
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.idade)
            col4.write(item.profissao)

            if col5.button('Excluir ' + str(item.id)):
                ClienteController.Excluir(item.id)               
                st.success("Cliente excluído com sucesso")

            if col6.button('Alterar ' + str(item.id)):
                st.experimental_set_query_params(id=[item.id])
                st.experimental_rerun()        
    else:
        on_click_voltar = st.button("Voltar") 
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
            
        # Se 'id' estiver presente, redirecione para a página de criação
        PageCreateCliente.Create()
