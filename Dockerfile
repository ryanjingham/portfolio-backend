FROM python:3.11.9

ENV PYTHONDUFFERED=1

WORKDIR /Back-end/django-project

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "base.wsgi"]
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT base.wsgi"]
