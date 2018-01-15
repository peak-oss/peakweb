# peakweb

`peakweb` provides the front-end web interface for `peak` API performance testing. From here, users can create new test suites, and view the results of previous tests.

![peakweb](https://i.imgur.com/g4Lculh.png)

## running peakweb

Create a virtualenv and install the requirements for peakweb

Set the `PEAKORC` environment variable:

```
# this value should be set to the peakorc API
$ export PEAKORC=http://peakorc-ip:8080
```

You can then use `gunicorn` to start a `peak-web` instance:

```
gunicorn --bind 0.0.0.0:5000 peakweb:app
```
