FROM python:3.10

ENV PYTHONUNBUFFERED=1 \
PORT=5000 \
FLASK_DEBUG="false" \
TIMEOUT=120 \
WORKERS=1 \
TRANSFORMERS_CACHE="/app/cache" \
LOGLEVEL=info

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:$PORT --workers $WORKERS --access-logfile - --error-logfile - --log-level LOGLEVEL --timeout $TIMEOUT wsgi:app