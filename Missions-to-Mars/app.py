from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = 'mongodb://localhost:27017'
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route('/')
def index():
    mars_app = mongo.db.mars.find_one()
    return render_template('index2.html', mars_app=mars_app)

@app.route("/scrape")
def scrape():
    mars_app = mongo.db.mars_app
    mars = scrape_mars.scrape()
    mars_app.update({}, mars, upsert=True)
    return redirect("/", code=302)
    
if __name__ == "__main__":
    app.run(debug=True)

