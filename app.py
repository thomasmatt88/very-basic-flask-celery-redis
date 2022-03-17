from flask import Flask
from celery_tasks import slow_reverse

app = Flask(__name__)


@app.route("/<forward>")
def publish_task(forward):
    result = slow_reverse.delay(forward)
    print(result.status)

    return f"<p>Navigate to /result/{result.id} to see {forward} in reverse.</p>"


@app.route("/result/<task_id>")
def show_result(task_id):
    result = slow_reverse.AsyncResult(task_id).get(timeout=1.0)
    return f"<p>Result: {result}!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
