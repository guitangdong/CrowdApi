FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uwsgi

COPY . .

#CMD [ "python", "./app.py" ]
CMD [ "uwsgi", "uwsgiConfig.ini" ]
