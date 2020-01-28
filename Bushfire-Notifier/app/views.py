from app import app 

from flask import render_template, request, redirect, jsonify, make_response

@app.route("/")
def index():
    return render_template("Australia.html")

#@app.route("/receive-data", methods=["POST"])
#def receive_data():
#    req = request.get_json()
#    print(req)
#    print(type(req))
#    print(req)
#    return "Thanks"
#    res = make_response(jsonify({"message: JSON received"}), 200)
#    return res