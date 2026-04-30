from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    patient = request.form.get("patient")
    age = request.form.get("age")

    return f"""
    <h2>Registration Successful ✅</h2>
    <p>Guardian: {name}</p>
    <p>Resident: {patient}</p>
    <p>Age: {age}</p>
    <a href="/">Go back</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)