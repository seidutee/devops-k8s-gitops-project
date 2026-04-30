from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
