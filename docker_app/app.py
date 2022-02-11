from typing import TYPE_CHECKING
import os

import json

from flask import Flask, render_template, request


if TYPE_CHECKING:
    from werkzeug.datastructures import FileStorage

# configure application
flask_app = Flask(__name__)


@flask_app.route("/")
def index():
    return render_template("index.html", msg="")


@flask_app.route("/test", methods=["GET"])
def test():
    data = {"response": "This is the Docker event"}
    response = flask_app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(debug=True, port=port)
