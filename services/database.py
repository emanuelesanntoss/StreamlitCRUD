#Instalação da biblioteca de conexão - pip install pyodbc
#https://learn.microsoft.com/pt-br/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16
#https://learn.microsoft.com/pt-br/sql/connect/python/python-driver-for-sql-server?view=sql-server-ver16

import pyodbc 

server = 'DESKTOP-860SDB5' 
database = 'crud_python' 
#username = 'myusername' 
#password = 'mypassword'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;Trusted_Connection=yes;')
cursor = cnxn.cursor()

