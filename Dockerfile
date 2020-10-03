FROM  python:3.7-slim-buster
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN python setup_db.py
CMD python app.py
