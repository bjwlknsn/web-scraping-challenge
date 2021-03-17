from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars 

# Create an instance of Flask
app = Flask(__name__)

#Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Create the index/home page route that will connect to the MongoDB with scraped data and then define it for html code
@app.route("/")
def index():
    # connect no-sql database with PyMongo
    mars_data = mongo.db.mars_data.find_one()
    # Use render_templates() to connect your database with your html file and render the desired data into dashboard
    return render_template("index.html", mars=mars_data)

# Create a route to your scrape function you created scrape_mars.py and upload the returned dictionary to the mongodb database
@app.route("/scrape")
def scraper():
    # define the database collection and connect to mongo db
    mars_data = mongo.db.mars_data
    # call the scrape() function you imported above 
    scraped_data = scrape_mars.scrape()
    # load the scraped dictionary into mongodb using ".update()" 
    mars_data.update({}, scraped_data, upsert=True)
    # afterwards we redirected it to our home/index dashboard to populate the HTML 
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)