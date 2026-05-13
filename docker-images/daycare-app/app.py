from flask import Flask, render_template, request

# ✅ ADDED: Prometheus imports
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# ✅ ADDED: Create a metric
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')

@app.route("/")
def home():
    # ✅ ADDED: Count requests
    REQUEST_COUNT.inc()
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    # ✅ ADDED: Count requests
    REQUEST_COUNT.inc()

    parent_name = request.form.get("parent_name")
    child_name = request.form.get("child_name")
    age = request.form.get("age")

    return f"""
    <h2>Signup Successful 🎉</h2>
    <p>Parent: {parent_name}</p>
    <p>Child: {child_name}</p>
    <p>Age: {age}</p>
    <a href="/">Go back</a>
    """

# ✅ ADDED: Metrics endpoint
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)