import code
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def getTwilioMessage():
    sms = request.args.getlist('Body')
    print sms[0].encode("utf-8")

    return ""

    # code.interact(local=dict(globals(), **locals()))

if __name__ == "__main__":
    app.run()
