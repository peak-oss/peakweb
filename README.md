# peakweb

`peakweb` provides the front-end web interface for `peak` API performance testing. From here, users can create new test suites, and view the results of previous tests.

![peakweb](https://i.imgur.com/g4Lculh.png)

## running peakweb (development)

Create a virtualenv and use pip to install the latest `peakweb` from source:
```
$ virtualenv peakenv
$ source peakenv/bin/activate
(peakenv)$ git clone https://github.com/peak-oss/peakweb.git
(peakenv)$ cd peakweb
(peakenv)$ pip install -e .
```

Set the `PEAKORC` environment variable:
```
# this value should be set to the peakorc API
$ export PEAKORC=http://peakorc-ip:8080
```

You can then use the local script to start an instance of `peakweb`:
```
(peakenv)$ peakweb
[2018-03-18 13:55:56 +0000] [29020] [INFO] Starting gunicorn 19.7.1
[2018-03-18 13:55:56 +0000] [29020] [INFO] Listening at: http://0.0.0.0:5000 (29020)
[2018-03-18 13:55:56 +0000] [29020] [INFO] Using worker: sync
[2018-03-18 13:55:56 +0000] [29025] [INFO] Booting worker with pid: 29025
```
Note that you can optionally provide a bind host and port for the service:
```
(peakenv)$ peakweb -b 0.0.0.0 -p 4000
```
