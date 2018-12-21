# This is the Peak front-end.

from flask import Flask, render_template, flash, redirect, request

from peakweb.forms import TestSuiteForm

import requests
import json
import os

application = Flask(__name__)
application.secret_key = os.environ['FLASK_SECRET']
peakorc = os.environ['PEAKORC']


@application.route('/healthz')
def healthz():
    """
    Check the health of this peakweb instance. OCP will hit this endpoint to verify the readiness
    of the peakweb pod.
    """
    return 'OK'

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/stop_suite', methods=('GET','POST'))
def stop_suite():
    test_uuid = request.args.get("uuid")
    requests.post(peakorc+'/suites/'+str(test_uuid)+'/stop')
    flash("Successfully stopped peak suite %s" % test_uuid)
    return redirect('/test_suite/')


@application.route('/test_suite/', methods=('GET', 'POST'))
def test_suite():
    form = TestSuiteForm()

    if form.validate_on_submit():
        resp = requests.post(peakorc+'/suites/',
                             headers={'test-url': str(form.url.data),
                                      'nodes': str(form.nodes.data),
                                      'node-requests': str(form.requests_node.data),
                                      'description': str(form.description.data)})

        test_id = resp.json()['id']
        flash("Successfully submitted peak suite \"%s\" (%s)" % (form.description.data, test_id))
        return redirect('/test_suite/')

    return render_template('testsuite.html', form=form)


@application.route('/history/', methods=('GET', 'POST'))
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
