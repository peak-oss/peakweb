# peakweb

`peakweb` provides the front-end web interface for `peak` API performance testing. From here, users can create new test suites, and view the results of previous tests.

![peakweb](https://i.imgur.com/g4Lculh.png)

## running peakweb

Create a virtualenv and install the requirements for peakweb

Set a secret key for the app:

```
>>> import os
>>> os.urandom(24)
'7`\xde+a\xbcs\xac\xbe\x881\xec\xf3@\x9a\t8\x8f\x8f\xbb\xf5\xdb\xe1c'

$ export PEAK_SECRET='7`\xde+a\xbcs\xac\xbe\x881\xec\xf3@\x9a\t8\x8f\x8f\xbb\xf5\xdb\xe1c'
```

You can then use `gunicorn` to start a `peak-web` instance:

```
gunicorn --bind 0.0.0.0:5000 peakweb:app
```
