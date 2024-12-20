FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas pyarrow sqlalchemy psycopg2
# RUN pip install pyarrow
# RUN pip install sqlalchemy
# RUN pip install psycopg2

WORKDIR /app
COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]
