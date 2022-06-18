FROM python:3.10

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

ARG APP_ENV $APP_ENV

ENV APP_ENV $APP_ENV

# Run the application
COPY . .
CMD uvicorn main:app --host="127.0.0.1" --port=5000 --log-level=info
