import pymysql
# creacion de la conexion a bd
mysql = pymysql.connect(host='localhost', port=3307,
                        user='root', passwd='', database='ejemplo_db_flask')
