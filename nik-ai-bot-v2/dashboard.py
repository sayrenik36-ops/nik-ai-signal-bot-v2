from flask import Flask, render_template, jsonify

from database import db

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/api/dashboard")
def api_dashboard():

    stats = db.statistics()

    trades = db.get_all_trades()

    trade_list = []

    for trade in trades:

        trade_list.append({

            "id": trade["id"],

            "pair": trade["pair"],

            "signal": trade["signal"],

            "entry": trade["entry"],

            "entry_time": trade["entry_time"],

            "result": trade["result"] if trade["result"] else "",

            "status": trade["status"]

        })

    return jsonify({

        "stats": stats,

        "trades": trade_list

    })


if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=False

    )
