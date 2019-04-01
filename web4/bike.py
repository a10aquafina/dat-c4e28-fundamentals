from pymongo import MongoClient
from flask import *
app = Flask(__name__)
uri = "mongodb+srv://admin:admin@c4e28-cluster-8dtuq.mongodb.net/test?retryWrites=true"
client = MongoClient(uri)
db = client.db_service
bikes = db["bike"]


@app.route('/new_bike', methods = ["GET", "POST"])
def index():
  if(request.method == "GET"):
    return render_template("bike.html")
  elif(request.method == "POST"):
        form = request.form
        new_bike = {
            "model": form["model"],
            "fee": form["fee"],
            "image": form["image"],
            "year": form["year"]
        }
        bikes.insert_one(new_bike)
  return redirect("/new_bike")

if __name__ == '__main__':
  app.run( debug=True)
 