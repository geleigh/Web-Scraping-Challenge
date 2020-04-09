from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route('/')
def index():
    mars = mongo.db.mars_app.find_one()
    return render_template('index2.html', mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars_app
    mars = scrape_mars.scrape()
    mars_app.update({}, mars, upsert=True)
    return redirect("/", code=302)
    
if __name__ == "__main__":
    app.run(debug=True)
