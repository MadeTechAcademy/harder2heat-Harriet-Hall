# Harder2Heat

Use the following commands to run this flask application in you local machine:

Set-up

Clone this repo:
- git clone https://github.com/MadeTechAcademy/harder2heat-Harriet-Hall.git

Navigate into the projects root directory:
- cd harder2heat-Harriet-Hall

Set up a python virtual environment:
- python3 -m venv . 

Activate the virtual environment:
- Source bin/activate 

Install the dependencies:
- pip install -r requirements.txt

----------------------------------------------

Run the flask app - (this step should be done in a seperate terminal):

- flask --app app.py --debug run

----------------------------------------------

To run the tests:

E2e tests:

- python -m coverage run -m behave tests/e2e_testing/features


Unit tests: 

- coverage run -m pytest tests/unit_testing


Integration tests:

Navigate to the mocking branch:

- git checkout mocking 

Navigate to the integration directory:

 cd tests/integration_testing  

Run the tests:

- coverage run -m pytest test_client.py   

