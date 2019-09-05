#!/usr/bin/python3

import getopt, sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Sut!'

if __name__ == '__main__':
    argList = sys.argv[1:]
    unixOptions = "p:"
    gnuOptions = []
    try:
        arguments, values = getopt.getopt(argList, unixOptions, gnuOptions)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)
    for currentArg, currentVal in arguments:
        if currentArg in ("-p"):
            app.run(host='0.0.0.0', debug=True, port=currentVal)