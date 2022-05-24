FROM python:3.9.2

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install --upgrade pip
RUN pip install psycopg2 
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt
RUN pip install gunicorn
#RUN python3 django_kali/manage.py migrate
#RUN python3 django_kali/manage.py makemigrations
#RUN python3 django_kali/manage.py collectstatic
CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "django_kali", "django_kali.wsgi:application"]
