FROM python:3 as python-base
COPY requirements.txt .
RUN pip3 install -r requirements.txt

FROM python:3-alpine
COPY --from=python-base /root/.cache /root/.cache
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt && rm -rf /root/.cache

CMD gunicorn wsgi:application -b 0.0.0.0:8080
EXPOSE 8080
