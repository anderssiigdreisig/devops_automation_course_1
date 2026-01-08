from flask import Flask
import json
import logging

app = Flask(__name__)

# Stream logs to a file, and set the default log level to DEBUG
logging.basicConfig(filename="app.log", level=logging.INFO)


@app.route("/")
def hello():
    app.logger.info("Main request successfull")
    return "Hello World!"


@app.route("/status")
def status():
    app.logger.info("Grabbing status of the application...")
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json",
    )
    if response:
        app.logger.info("Status extracted succesfully!")

    return response


@app.route("/metrics")
def metrics():
    app.logger.info("Grabbing metrics of the application...")
    response = app.response_class(
        response=json.dumps(
            {
                "status": "success",
                "code": 0,
                "data": {"UserCount": 140, "UserCountActive": 23},
            }
        ),
        status=200,
        mimetype="application/json",
    )
    if response:
        app.logger.info("Metrics extracted succesfully!")
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0")
