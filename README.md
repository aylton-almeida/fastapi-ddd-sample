# FastAPI DDD Sample APP

A simple fast api app using DDD folder structure

## Structure

<!-- TODO: Add -->

## Running

To run this app use the following commands:

```bash
  # Install dependencies
  pip install -r requirements.txt

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

## Author

- Aylton Almeida
