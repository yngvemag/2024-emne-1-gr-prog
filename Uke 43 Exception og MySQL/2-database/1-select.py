from database import mysql_db as db

query = """
    SELECT * from ncity;
"""

result = db.query(host='localhost',
                  user='root',
                  password='gokstad',
                  database='world',
                  query_str=query,
                  port=3306,
                  dictionary=False)

for row in result:
    print(row)
