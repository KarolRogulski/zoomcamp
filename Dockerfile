FROM python:3.9.1

RUN pip install pandas
RUN pip install pyarrow
RUN pip install sqlalchemy
RUN pip install psycopg2


