#!/usr/bin/python

import MySQLdb as mysql
import os

AHDH_DB_HOST = os.getenv('AHDH_DB_HOST', 'localhost')
AHDH_DB_PORT = os.getenv('AHDH_DB_PORT', 3306)
AHDH_DB_USER = os.getenv('AHDH_DB_USER', 'root')
AHDH_DB_PASSWORD = os.getenv('AHDH_DB_PASSWORD', 'anakamak')
AHDH_DB_NAME = os.getenv('AHDH_DB_NAME', 'ahdh_db')

db = mysql.connect(host=AHDH_DB_HOST,
                   port=AHDH_DB_PORT,
                   user=AHDH_DB_USER,
                   passwd=AHDH_DB_PASSWORD,
                   db=AHDH_DB_NAME)

names = ["ujang", "uda", "uni", "abi", "gori"]

query = """
    INSERT INTO `ahdh` (`id`, `username`) VALUES ("{}", "{}");
    """

cur = db.cursor()

# remove existing ahdh table
cur.execute("DROP TABLE IF EXISTS ahdh;")

# create ahdh table
cur.execute('''
            CREATE TABLES ahdh(id int NOT NULL, username varchar(20) NOT NULL);
            ''')

# commit changes
db.commit()

# populate table with dummy data
for id in range(len(names)):
    sql = query.format(id, names[i])
    cur.execute(sql)
    db.commit()

# close connection to database
db.close()
