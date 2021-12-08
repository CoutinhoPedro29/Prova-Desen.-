import pymysql.cursors
import json


def jog():
    db_host="http://localhost/phpmyadmin/sql.php?db=jogador&table=jogador&pos=0"
    db_banco="jogador"
    
    listajog =[]
    jsonjog = {}
    
    
    # Connect to the database
    connection = pymysql.connect(host=db_host,
                                user='admin',
                                password='password',
                                database=db_banco,
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
   
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT nome FROM jogador order by score desc"
            cursor.execute(sql)
            registros = cursor.fetchall()
            for jogador in registros:
                listajog.append(jogador["nome"])
    
    #monta o json de saida
    jsonjog["jogador"] = listajog
    json_object = json.dumps(jsonjog, indent=4 ) 
    
    return json_object           