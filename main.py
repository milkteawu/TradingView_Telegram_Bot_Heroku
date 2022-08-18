# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : main.py                 #
# ----------------------------------------------- #

from flask import Flask, request
from handler import *

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        if request.method == "POST":
            data = request.get_json()
            key = data["key"]
            if key == os.environ.get("sec_key"):
                print(get_timestamp(), "Alert Received & Sent!")
                send_alert(data)
                return "Sent alert", 200

            else:
                print("[X]", get_timestamp(), "Alert Received & Refused! (Wrong Key)")
                return "Refused alert", 400

    except Exception as e:
        print("[X]", get_timestamp(), "Error:\n>", e)
        return "Error", 400

@app.route("/test", methods=["GET","HEAD"])
def test():
        return "Test Successful!", 200

def get_port():
  return int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=get_port())
