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
            "owner": owner[0],
            "phone_number": owner[1],
            "House_Number": owner[2],
            "Floor": owner[3]
        }), 200
    else:
        return jsonify({
            "error": "No owner found in DB"
        }), 404