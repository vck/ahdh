#!/usr/bin/python

import os
from flask import (
    Flask
)

# flask instance
app = Flask(__name__)

# get port value from os environment, if none use default port instead
AHDH_PORT = os.getenv('AHDH_PORT', 8080)

@app.route('/')
def index_router():
    """
    ahdh index router
    :rtype: string
    """
    return '200 OK'

# if executed as a script, run apps
if __name__ == '__main__':
    # run flask apps on 0.0.0.0:AHDH_PORT
    app.run(host='0.0.0.0', port=AHDH_PORT)
