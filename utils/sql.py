import pymysql
import datetime

host = 'localhost'
username = 'root'
password = 'wt19970419!'

connection = ''
cursor = ''

create_tabel_sql = """\
CREATE TABLE {tabelname} (
  UID VARCHAR(255),
  NAME VARCHAR(255),
  COUNT VARCHAR(255)
)
"""

insert_table_sql = """\
INSERT INTO SUPPORTER (UID, NAME, COUNT) VALUES ('{uid}', '{name}', '{count}')
"""

query_table_sql = """\
SELECT NAME, COUNT FROM SUPPORTER WHERE UID='{uid}'
"""

update_table_sql = """\
UPDATE SUPPORTER SET '{type}'='{data}' WHERE UID='{uid}'
"""


def createDatabase(name):
  global db_name, connection, cursor
  db_name = name

  connection = pymysql.connect(
    host = host,
    user = username,
    passwd = password,
    charset = 'utf8mb4',
    db = db_name,
    port = 3306
  )

  cursor = connection.cursor()

def createTable(tabelname):
  if connection != '' and cursor != '':
    print('--------------新建表--------------')
    print(tabelname)
    cursor.execute(
      create_tabel_sql.format(tabelname = tabelname)
    )
    connection.commit()

def insertData(uid, username, count):
  if connection != '' and cursor != '':
    print('--------------插入数据-------------')
    print(uid, username, count)
    cursor.execute(
      insert_table_sql.format(uid = uid, name = username, count = count)
    )
    connection.commit()

def updateData(type, data, uid):
  if connection != '' and cursor != '':
    print('--------------更新数据-------------')
    cursor.execute(
      update_table_sql.format(type = type, data = data, uid = uid)
    )
    connection.commit()

def queryData(uid):
  if connection != '' and cursor != '':
    print('--------------查询数据-------------')
    cursor.execute(
      query_table_sql.format(uid = uid)
    )
    results = cursor.fetchall()
    if len(results):
      return results[0]
    else:
      return 'null'

