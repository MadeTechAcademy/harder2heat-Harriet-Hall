import json
from flask import Flask, render_template
from src.generate_properties import GenerateProperties
from src.utils import SortProperties
app = Flask(__name__)

with open('properties.json') as json_properties:
   data = json.load(json_properties)
   properties = GenerateProperties.generate_property_class_list(data)
   
   for property in properties:
      property.calculate_score()

   sorted_properties = SortProperties.get_hardest_to_heat_properties(properties) 
   
@app.route("/")
def home():
   return render_template("home.html", properties=sorted_properties)

@app.route("/<int:uprn>")
def property(uprn):
    property = None
    for property_instance in properties:
        if property_instance.uprn == uprn:
            property = property_instance

    return render_template("property.html", property=property)