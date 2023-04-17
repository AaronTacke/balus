from flask import Flask
from Person.homer import Homer

# Select implementation of model for user
person = Homer()

# Webservice for communication with controllers and views
app = Flask(__name__)


@app.route('/view/should_learn', methods=['GET'])
def should_learn():
    return str(person.should_learn())


@app.route('/model/is_learning', methods=['GET'])
def is_learning():
    person.is_learning()
    return "ok"


@app.route('/model/is_relaxing', methods=['GET'])
def is_relaxing():
    person.is_relaxing()
    return "ok"


@app.route('/model/is_distracted', methods=['GET'])
def is_distracted():
    person.is_distracted()
    return "ok"


@app.route('/model/is_concentrated', methods=['GET'])
def is_concentrated():
    person.is_concentrated()
    return "ok"


@app.route('/model/is_leaving', methods=['GET'])
def is_leaving():
    person.is_leaving()
    return "ok"


@app.route('/model/is_back', methods=['GET'])
def is_back():
    person.is_back()
    return "ok"


@app.route('/model/is_happy', methods=['GET'])
def is_happy():
    person.is_happy()
    return "ok"


@app.route('/model/is_mad', methods=['GET'])
def is_mad():
    person.is_mad()
    return "ok"


# Start webservice in debug mode
if __name__ == '__main__':
    app.run(debug=True, port=1110)
