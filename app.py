from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

mongo_host = os.environ.get("MONGO_HOST", "localhost")
client = MongoClient(f"mongodb://{mongo_host}:27017/")
db = client["mydb"]
collection = db["items"]

@app.route("/")
def index():
    items = list(collection.find())
    return render_template("index.html", items=items)

# 예시
# @app.route("/login", methods=["GET"])
# def login_page():
#     return render_template("login.html")
#
# @app.route("/login", methods=["POST"])
# def login_submit():
#     # 로그인 처리
#     return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
