import sys

from flask import Flask, redirect, request, jsonify, url_for, render_template

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def index():
     return 'Hello Zappa!'

if __name__ == '__main__':
 if len(sys.argv) > 1:
     app.debug = True
     app.jinja_env.auto_reload = True
     app.config['TEMPLATES_AUTO_RELOAD'] = True
     app.run(host='0.0.0.0', port=4000)
 else:
     app.run(host='0.0.0.0')