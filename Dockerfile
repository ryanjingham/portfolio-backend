FROM python:3.11.9

ENV PYTHONUNBUFFERED=1

WORKDIR /Back-end/django-project

COPY requirements.txt /Back-end/django-project/requirements.txt

RUN pip install -r requirements.txt

COPY . /Back-end/django-project

EXPOSE 8000

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT base.wsgi"]