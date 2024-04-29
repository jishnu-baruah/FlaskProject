from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Sample list of random facts
random_facts = [
    "WHO BHADWA.",
    "Yeh LOH BACKEND",
    "YEH LOH FLASK MEIN BACKEND.",
]

@app.route("/")
def index():
    # Get a random fact
    fact = random.choice(random_facts)
    return render_template("index.html", fact=fact)

@app.route("/post_fact", methods=["POST"])
def post_fact():
    new_fact = request.form.get("new_fact")
    if new_fact:
        random_facts.append(new_fact)
    return index()

if __name__ == "__main__":
    app.run(debug=True)
