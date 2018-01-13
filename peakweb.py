# This is the Peak front-end.

from flask import Flask, render_template, flash, redirect

from forms import TestSuiteForm

import requests
import json

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test_suite/', methods=('GET', 'POST'))
def test_suite():
    form = TestSuiteForm()

    if form.validate_on_submit():
        resp = requests.post("http://localhost:8080/test_suite/new",
                             headers={'test-url': str(form.url.data),
                                      'nodes': str(form.nodes.data),
                                      'node-requests': str(form.requests_node.data),
                                      'description': str(form.description.data)})

        test_id = resp.json()['id']
        return redirect('/suite_view/'+test_id)

    return render_template('testsuite.html', form=form)

@app.route('/suite_view/<suite_uuid>', methods=('GET','POST'))
def view_test(suite_uuid):
    resp = requests.get('http://localhost:8080/suites/'+suite_uuid)
    num_requests = resp.json()['requests']
    return render_template('testview.html', suite_uuid=suite_uuid,
                           requests=num_requests)


@app.route('/suite_time_data/<suite_uuid>', methods=('GET','POST'))
def get_data(suite_uuid):
    resp = requests.get("http://localhost:8080/time_data/"+suite_uuid)
    return json.dumps(resp.json())


@app.route('/history/', methods=('GET', 'POST'))
def history():

    return render_template('history.html')
