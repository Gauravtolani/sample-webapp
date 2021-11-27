from flask import Flask, render_template, request
from RtmTokenBuilderTest import test
app = Flask(__name__)

@app.route("/")
def index():
    userAccount = request.args.get('userAccount', default='test', type=str)
    count = test(userAccount)
    return count  # render_template("index.html", count=count)


if __name__ == "__main__":
    app.run()
