from flask import Flask
from celery_tasks import slow_reverse

app = Flask(__name__)


@app.route("/")
def hello_world():
    result = slow_reverse.delay("Matt")
    print(result.status)

    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
