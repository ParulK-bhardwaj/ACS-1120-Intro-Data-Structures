"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
import markov_higher

app = Flask(__name__)

@app.route("/")
def home():
    sentence = markov_higher.main()
    return render_template('index.html', sentence=sentence)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
