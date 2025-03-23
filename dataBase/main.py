import pymysql

db_config = {
    'host': 'localhost',
    'user': 'ADM_FER',
    'password': 'Venom@326$s21',
    'database': 'corp'
}

def conect_db():
    return pymysql.connect(host='localhost', user= 'ADM_FER', password= 'Venom@326$s21', database= 'corp')

sql_command = input('Digite o comando SQL: ')

if sql_command != '':
    connection = conect_db()
    with connection.cursor() as cursor:
        cursor.execute(sql_command)
        user = cursor.fetchmany(50000)
    connection.close()

    print(user) #Retorna bloco de código!
else:
    print('Não conectado!')
