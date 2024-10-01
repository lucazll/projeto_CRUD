import mysql
import mysql.connector

conn = mysql.connector.connect(
    username = 'lopes',
    host = 'localhost',
    password = 'projeto01',
    db = 'projeto_CRUD01'
)