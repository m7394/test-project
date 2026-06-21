from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

FILE_NAME = "records.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([], f)


@app.route("/records", methods=["GET"])
def get_records():

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    return jsonify(data)


@app.route("/records", methods=["POST"])
def add_record():

    new_record = request.json

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    data.append(new_record)

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    return jsonify({"message": "success"})


@app.route("/balance")
def get_balance():

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    balance = 0

    for item in data:

        if item["type"] == "income":
            balance += item["amount"]

        else:
            balance -= item["amount"]

    return jsonify({"balance": balance})


app.run(debug=True)