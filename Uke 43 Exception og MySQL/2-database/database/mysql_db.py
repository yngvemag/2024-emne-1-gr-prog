import mysql.connector
from typing import Sequence


#
def query(host: str,
          user: str,
          password: str,
          database: str,
          query_str: str,
          port: int = 3306,
          dictionary: bool = False) -> list[tuple] | list[dict] | Sequence:

    try:
        # 1. STEP:  Vi trenger en kobling til database !
        with mysql.connector.connect(host=host, user=user, password=password, database=database,
                                     port=port) as con:

            # Ved å bruke databasekoblingen 'con', opprettes en 'cursor' som vil tillate deg å utføre
            # SQL-spørringer og hente resultater.
            # 2. STEP
            with con.cursor(dictionary=dictionary) as cur:
                # STEP 3: Gjennomfør spørring
                cur.execute(query_str)

                # STEP 4: Hente resultater
                result = cur.fetchall()

                return result


    except mysql.connector.Error as err:
        print(f'Database error: {err}')

