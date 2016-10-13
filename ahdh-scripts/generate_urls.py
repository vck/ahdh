#!/usr/bin/python

import MySQLdb as mysql
import os
import random

# get environment variables, if none use default value instead
AHDH_DB_HOST = os.getenv('AHDH_DB_HOST', 'localhost')
AHDH_DB_PORT = os.getenv('AHDH_DB_PORT', 3306)
AHDH_DB_USER = os.getenv('AHDH_DB_USER', 'root')
AHDH_DB_PASSWORD = os.getenv('AHDH_DB_PASSWORD', 'anakamak')
AHDH_DB_NAME = os.getenv('AHDH_DB_NAME', 'ahdh_db')

# connect to database
db = mysql.connect(host=AHDH_DB_HOST,
                   port=AHDH_DB_PORT,
                   user=AHDH_DB_USER,
                   passwd=AHDH_DB_PASSWORD,
                   db=AHDH_DB_NAME)

cur = db.cursor()

# set max range
MAX_RANGE = 100

# user id that will be randomly picked
RANDOM_ID = [1, 2, 3, 4, 5]

# generate list within range 1-99
RANDOM_URL_ID = xrange(MAX_RANGE)

# set default URL
DEFAULT_URL = "https://news.ycombinator.com/item?id={}"

# remove existing ahdh_url table
cur.execute('''DROP TABLE IF EXISTS ahdh_url''')

# commit changes
db.commit()

# create ahdh_table
cur.execute('''CREATE TABLE ahdh_url (id int NOT NULL, user_id int NOT NULL, url VARCHAR(40) NOT NULL);''')

# default query
QUERY = '''
        INSERT INTO ahdh_url(`id`, `user_id`, `url`) VALUES ("{}", "{}", "{}");
        '''

# commit changes
db.commit()

for item in xrange(MAX_RANGE):

    # select random id in range 1-5
    user_id = random.choice(RANDOM_ID)

    # select random url id within range 1-99
    url_id = random.choice(RANDOM_URL_ID)

    # set url ID with randomly picked id
    url = DEFAULT_URL.format(url_id)

    # set QUERY with random user_id and random url_id
    sql = QUERY.format(item, user_id, url)

    # execute query
    cur.execute(sql)

    # commit changes
    db.commit()
