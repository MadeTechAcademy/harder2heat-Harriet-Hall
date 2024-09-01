import json
from flask import Flask, render_template
from src.property_manager import PropertyManager
from src.generate_properties import GenerateProperties

app = Flask(__name__)

with open('properties.json') as json_properties:
   data = json.load(json_properties)
   properties = GenerateProperties.generate_property_class_list(data)
   ordered_properties = PropertyManager.get_hardest_to_heat_properties(properties)
   
@app.route("/")
def home():
   return render_template("home.html", properties=ordered_properties)

@app.route("/<int:uprn>")
def property(uprn):
    property = None
    for property in properties:
        if property.uprn == uprn:
            property = property

    return render_template("property.html", property=property)