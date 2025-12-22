from flask import Flask, jsonify, request, render_template
from utils import get_owner_details

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/check-number', methods=['POST'])
def check_number():
    data = request.get_json()
    number = data.get("number_plate")
    if not number:
        return jsonify({"error": "Number plate not provided"}), 400

    owner = get_owner_details(number)
    if owner:
        return jsonify({
            "number_plate": number,
            "owner": owner["owner_name"],
            "phone_number": owner["phone_number"],
            "address": owner["Address"]
        })
    else:
        return jsonify({
            'number_plate': number,
            "message": "No owner found in DB"
        })

@app.route("/db-test")
def db_test():
    owner = get_owner_details("DL9CAT0789")
    return str(owner)
