import json
from flask import Flask, render_template
from src.council import Council
app = Flask(__name__)


with open('properties.json') as json_properties:
   data = json.load(json_properties)
   council = Council("any", "UK")
   council.generate_property_class_list(data)
   council.get_hardest_to_heat_properties()
   
@app.route("/")
def home():
   return render_template("home.html", properties=council.list_of_properties)

@app.route("/<int:uprn>")
def property(uprn):
    property = None
    for property_i in council.list_of_properties:
        if property_i.uprn == uprn:
            property = property 

    return render_template("property.html", property=property)