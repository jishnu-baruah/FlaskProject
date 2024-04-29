from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

random_facts = [
    "WHO BHADWA.",
    "Yeh LOH BACKEND",
    "YEH LOH FLASK MEIN BACKEND.",
]

@app.route("/")
def index():
    fact = random.choice(random_facts)
    return render_template("index.html", fact=fact)

@app.route("/allfacts")
def show_all_facts():
    return jsonify({"facts": random_facts})
@app.route("/randomfact")
def show_random_fact():
    fact = random.choice(random_facts)
    return jsonify({"fact": fact})
@app.route("/post_fact", methods=["POST"])
def post_fact():
    new_fact = request.form.get("new_fact")
    if new_fact:
        random_facts.append(new_fact)
    return index()

if __name__ == "__main__":
    app.run(debug=True)
