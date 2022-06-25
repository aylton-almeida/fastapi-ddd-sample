# FastAPI DDD Sample APP

A simple fast api app using DDD folder structure

## Structure

### Application

All app rules are contained in this folder. Entry points for the application, such as `Queues` or `Routes` should be here in their own folders. Also the main `app` is also defined here.

### Domain

All domain rules are contained in this folder. Domain rules should be defined in their own folders. Ex.: The `user` domain may contain `services`, `models` and `enums`.

### Infrastructure

All infrastructure rules are contained in this folder. Infrastructure rules should be defined in their own folders. Ex.: The `connection` and `entities` for the `postgresql` database should be here. Also `configs` for a `RabbitMQ` connection should have their own folder here.

## Running

To run this app use the following commands:

```bash
  # Install dependencies
  pip install -r requirements/prod.txt

  # Run the app
  uvicorn main:app --host="127.0.0.1" --port=5000 --log-level=debug --reload
```

You can also build the docker image and run it, like the following:

```bash
  # Build image
  docker build -t fastapi-ddd-sample .

  # Run the container
  docker run -p 5000:5000 --name fastapi-ddd-sample fastapi-ddd-sample
```

If you're using `vscode` you can also press `F5` to run in debug mode

## Documentation

If you want to check the routes docs you can can run the app and go to either `http://localhost:5000/docs` or `http://localhost:5000/redoc`

## Author

- Aylton Almeida
