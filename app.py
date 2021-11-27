from flask import Flask, render_template
from RtmTokenBuilderTest import test
app = Flask(__name__)

@app.route("/")
def index():
    count = test()
    return render_template("index.html", count=count)


if __name__ == "__main__":
    app.run()