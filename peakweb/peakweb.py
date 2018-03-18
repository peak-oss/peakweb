# This is the Peak front-end.

from flask import Flask, render_template, flash, redirect, request

from forms import TestSuiteForm

import requests
import json
import os

app = Flask(__name__)
app.secret_key = 'some_secret'
peakorc = os.environ['PEAKORC']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test_suite/', methods=('GET', 'POST'))
def test_suite():
    form = TestSuiteForm()

    if form.validate_on_submit():
        resp = requests.post(peakorc+'/suites/',
                             headers={'test-url': str(form.url.data),
                                      'nodes': str(form.nodes.data),
                                      'node-requests': str(form.requests_node.data),
                                      'description': str(form.description.data)})

        test_id = resp.json()['id']
        flash("Successfully submitted peak suite %s" % test_id)
        return redirect('/test_suite/')

    return render_template('testsuite.html', form=form)

@app.route('/suite_view/<suite_uuid>', methods=('GET','POST'))
def view_test(suite_uuid):
    resp = requests.get(peakorc+'/suites/'+suite_uuid)
    num_requests = resp.json()['requests']
    return render_template('testview.html', suite_uuid=suite_uuid,
                           requests=num_requests)


@app.route('/suite_time_data/<suite_uuid>', methods=('GET','POST'))
def get_data(suite_uuid):
    resp = requests.get(peakorc+'/suites/'+suite_uuid+'/metrics/raw_response_counts')
    return json.dumps(resp.json())

@app.route('/avg_time/<suite_uuid>', methods=('GET','POST'))
def get_avg(suite_uuid):
    resp = requests.get(peakorc+'/suites/'+suite_uuid+'/metrics/avg_response_times')
    return json.dumps(resp.json())

@app.route('/history/', methods=('GET', 'POST'))
def history():
    try:
        page = request.args.get("page") or "1"
        resp = requests.get(peakorc+'/suites/?page='+page).json()
        suites = resp['suites']
        pages = resp['total_pages']
        return render_template('history.html',suites=suites, pages=pages, page=int(page))
    except ValueError:
        msg = "Attempted to decode a non-integer value when accessing the 'page' URL parameter.\n\n"\
              "The value for the 'page' parameter was %s" % page
        return render_template("500.html", msg = msg), 500
