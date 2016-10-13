#!/usr/bin/python

import MySQLdb as mysql
import os
from flask import (
    Flask,
    jsonify,
    redirect,
    url_for
)

# get environment variables, if none use default value instead
AHDH_DB_HOST = os.getenv('AHDH_DB_HOST', 'localhost')
AHDH_DB_PORT = os.getenv('AHDH_DB_PORT', 3306)
AHDH_DB_USER = os.getenv('AHDH_DB_USER', 'root')
AHDH_DB_PASSWORD = os.getenv('AHDH_DB_PASSWORD', 'anakamak')
AHDH_DB_NAME = os.getenv('AHDH_DB_NAME', 'ahdh_db')
AHDH_PORT = os.getenv('AHDH_PORT', 8080)

# connect to database
db = mysql.connect(host=AHDH_DB_HOST,
                   port=AHDH_DB_PORT,
                   user=AHDH_DB_USER,
                   passwd=AHDH_DB_PASSWORD,
                   db=AHDH_DB_NAME)

cur = db.cursor()

# use "app" as flask instance
app = Flask(__name__)


@app.route('/')
def index():
    '''
    :rtype: JSON
    '''
    return redirect(url_for('index_router'))


@app.route('/api/v1')
def index_router():
    '''
    ahdh index router
    :rtype: string
    '''
    return jsonify({'message': '200 OK'}), 200


@app.route('/api/v1/user/<int:id>', methods=['GET'])
def get_url_by_id(id):
    '''
    :type id: int
    :rtype: json
    '''

    # prevent 404 error
    if id:
        # convert user id to integer
        USER_ID = int(id)

        # SQL query for fetching url by given user id
        QUERY = '''
                    SELECT url FROM ahdh_url WHERE user_id={}'''

        # use string formatting to prevent
        # tedious converting data-type
        sql_query = QUERY.format(USER_ID)

        # execute query
        cur.execute(sql_query)

        # get all query based on given user id
        url_by_id = cur.fetchall()

        if len(url_by_id) > 0:
            # convert fetched data into dict and
            # do list comprehension for each item in tupples
            url_by_id_json = {'user_id': USER_ID,
                              'urls': [url for url in url_by_id]}

            # return result in JSON with jsonify
            return jsonify(url_by_id_json), 200

        # if data not found
        # data not found indicated by
        # the length of url_by_id is 0
        return jsonify({'message': 'user not found!'})
    else:

        # if user id not given
        # redirect to /api/v1/
        return redirect(url_for('index_router')), 200

# if executed as a script, run flask app
if __name__ == '__main__':
    # run flask apps on 0.0.0.0:AHDH_PORT
    app.debug = True
    app.run(host='0.0.0.0', port=AHDH_PORT, threaded=True)
