#!/usr/bin/python

import MySQLdb as mysql
import os

AHDH_DB_HOST = os.getenv('AHDH_DB_HOST','localhost')
AHDH_DB_PORT = os.getenv('AHDH_DB_PORT',3306)
AHDH_DB_USER = os.getenv('AHDH_DB_USER','root')
AHDH_DB_PASSWORD = os.getenv('AHDH_DB_PASSWORD','anakamak')
AHDH_DB_NAME = os.getenv('AHDH_DB_NAME','ahdh_db')

db = mysql.connect(host=AHDH_DB_HOST,
                   port=AHDH_DB_PORT,
                   user=AHDH_DB_USER,
                   passwd=AHDH_DB_PASSWORD,
                   db=AHDH_DB_NAME
)
