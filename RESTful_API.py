from flask import Flask, request, jsonify
import unsplash_img as unImg
import mysql_connect

# CONNECT WITH SQL Server
mc = mysql_connect.ConnectSql()

# FLASK
app = Flask(__name__)


# home
@app.route('/')
def home():
    return "home"


# CRUD Methods
# Create
@app.route("/create", methods=["POST"])  # id, toy, price
def create_user():
    data = request.get_json()
    id = data["toy_id"]
    name = data["toy_name"]
    price = data["toy_price"]
    mc.insertToy(id, name, price)

    url = unImg.GETUnsplashImg().getUrl(name)
    print(url)
    mc.updateImg(id, url)

    return jsonify(mc.showToy(id)), 200


# Read
@app.route("/read/<toy_id>", methods=["GET"])
def read(toy_id):
    mc.showToy(int(toy_id))

    return jsonify(mc.showToy(int(toy_id))), 200


# Update
@app.route("/update", methods=["PUT", "POST"])  # id, price
def update_user():
    data = request.get_json()
    id = data["toy_id"]
    price = data["toy_price"]
    print(id, price)
    mc.updateToy(id, price)
    return jsonify({"message": f"updating price of id: {id} to {price}"})


# Delete
@app.route("/delete/<id>", methods=["DELETE"])  # id
def delete_user(id):
    print(id)
    mc.deleteToy(id)
    return jsonify({"message": f"deleting toy id: {id}"})


@app.route("/show-all", methods=["GET"])
def show_all_flask():
    return jsonify(mc.showToyAll())


if __name__ == '__main__':
    app.run(debug=True)
