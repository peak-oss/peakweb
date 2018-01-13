# peakweb

`peakweb` provides the front-end web interface for `peak` API performance testing. From here, users can create new test suites, and view the results of previous tests.

![peakweb](https://i.imgur.com/g4Lculh.png)

## running peakweb

Create a virtualenv and install the requirements for peakweb

You can then use `gunicorn` to start a `peak-web` instance:

```
gunicorn --bind 0.0.0.0:5000 peakweb:app
```
