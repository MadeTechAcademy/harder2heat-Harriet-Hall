import json
from flask import Flask, render_template
from src.utils import generate_property_class_list
app = Flask(__name__)

properties = None
with open('properties.json') as json_properties:
   data = json.load(json_properties)
   properties = generate_property_class_list(data)

@app.route("/")
def home():
   return render_template("home.html", properties=properties)