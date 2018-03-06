FROM python:3.6

WORKDIR /app
COPY ./ /app

RUN pip3 install gunicorn && \
    python3 setup.py install

EXPOSE 8080
CMD ['env', '`cat config.env`', \
    'gunicorn', 'cp_fake:create_app()', \
    '--bind=0.0.0.0:8080', \
    '--worker-class=aiohttp.GunicornWebWorker', \
    '--workers=5']