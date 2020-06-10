import json
import requests
from pprint import pprint
from urllib.parse import quote
import flask
from flask import request
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def search_azure_cognitive(project_name):
    endpoint = 'https://<api-path>.search.windows.net/'
    api_version = 'api-version=2019-05-06'
    headers = {'Content-Type': 'application/json',
            'api-key': '<api-key>' }
    url = endpoint + "indexes/azureblob-index/docs?" + api_version + "&search=*&"+quote("$filter")+"=" + quote("project_name eq ")+"'"+project_name+"'"
    print(url)
    response  = requests.get(url, headers=headers)
    index_list = response.json()
    pprint(index_list["value"][0]["project_type"])
    #return index_list["value"][0]["project_type"]
    return index_list

@app.route('/getresult', methods=['GET'])
def getresult():
    project_name = request.args.get('project_name')
    return search_azure_cognitive(project_name)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

app.run(debug=True, host='0.0.0.0')



