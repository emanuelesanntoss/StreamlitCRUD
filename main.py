import streamlit as st
import Controllers.ClienteController as ClienteController
import Pages.Cliente.Create as PageCreateCliente
import Pages.Cliente.List as PageListCliente

# Título
st.sidebar.title('Menu')
Page_cliente = st.sidebar.selectbox('Cliente',['Incluir','Consultar'])

# Incluir clientes
if Page_cliente == 'Incluir':  
    st.experimental_set_query_params()
    PageCreateCliente.Create()
    

# Consulta clientes
if Page_cliente == 'Consultar':
    customerList = ClienteController.selecionarTodos()
    PageListCliente.List(customerList)  # Não é necessário passar a lista como argumento
