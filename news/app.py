from flask import Flask,render_template
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    dirList = []
    jsonList = []
    os.chdir('/home/shiyanlou/files/')
    for dir in os.listdir('/home/shiyanlou/files/'):
        dirList.append(os.path.abspath(dir))
    for dir in dirList:
        with open(dir) as file:
            jsonList.append(json.loads(file.read()))
    return render_template('index.html',list=jsonList)

@app.route('/files/<filename>')
def file(filename):
    os.chdir('/home/shiyanlou/files/')
    filename = filename+'.json'
    if os.path.exists(filename):
        with open(filename) as file:
            paper = json.loads(file.read())
        return render_template('file.html',paper=paper)
    else:
        return render_template('404.html'),404

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
