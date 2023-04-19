from flask import Flask, redirect
from Person.homer import Homer
from flask_swagger_ui import get_swaggerui_blueprint

# Select implementation of model for user
person = Homer()

# Webservice for communication with controllers and views
app = Flask(__name__)

# Swagger UI blueprint
SWAGGER_URL = '/swaggerui'
API_URL = '/swagger.json'
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Model for a concentrating person"
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


# Redirect to swaggerui on base url
@app.route('/')
def swaggerui():
    return redirect("/swaggerui")


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


# Swagger API definition
@app.route('/swagger.json', methods=['GET'])
def swagger():
    return {
        "swagger": "2.0",
        "info": {
            "title": "Model for a concentrating person",
            "version": "1.0",
        },
        "basePath": "/",
        "schemes": [
            "http",
            "https"
        ],
        "paths": {
            "/view/should_learn": {
                "get": {
                    "tags": [
                        "View"
                    ],
                    "summary": "Check if the person should learn",
                    "responses": {
                        "200": {
                            "description": "Returns how much the person should start concentrating",
                            "schema": {
                                "type": "number",
                                "format": "float",
                                "minimum": -1,
                                "maximum": 1
                            }
                        }
                    }
                }
            },
            "/model/is_learning": {
                "get": {
                    "tags": [
                        "Model"
                    ],
                    "summary": "Set the person to learning mode",
                    "responses": {
                        "200": {
                            "description": "Returns 'ok' if successful",
                            "schema": {
                                "type": "string"
                            }
                        }
                    }
                }
            },
            "/model/is_relaxing": {
                "get": {
                    "tags": [
                        "Model"
                    ],
                    "summary": "Set the person to relaxing mode",
                    "responses": {
                        "200": {
                            "description": "Returns 'ok' if successful",
                            "schema": {
                                "type": "string"
                            }
                        }
                    }
                }
            },
            "/model/is_distracted": {
                "get": {
                    "tags": [
                        "Model"
                    ],
                    "summary": "Set the person to distracted mode",
                    "responses": {
                        "200": {
                            "description": "Returns 'ok' if successful",
                            "schema": {
                                "type": "string"
                            }
                        }
                    }
                }
            },
            "/model/is_concentrated": {
                "get": {
                    "tags": [
                        "Model"
                    ],
                    "summary": "Set the person to concentrated mode",
                    "responses": {
                        "200": {
                            "description": "Returns 'ok' if successful",
                            "schema": {
                                "type": "string"
                            }
                        }
                    }
                }
            },
            "/model/is_leaving": {
                "get": {
                    "tags": [
                        "Model"
                    ],
                    "summary": "Set the person to leaving mode",
                    "responses": {
                        "200": {
                            "description": "Returns 'ok' if successful",
                            "schema": {
                                "type": "string"
                            }
                        }
                    }
                }
            },
            "/model/is_back": {
                "get": {
                    "tags": [
                        "Model"
                    ],
                    "summary": "Set the person to back mode",
                    "responses": {
                        "200": {
                            "description": "Returns 'ok' if successful",
                            "schema": {
                                "type": "string"
                            }
                        }
                    }
                }
            },
            "/model/is_happy": {
                "get": {
                    "tags": [
                        "Model"
                    ],
                    "summary": "Set the person to happy mode",
                    "responses": {
                        "200": {
                            "description": "Returns 'ok' if successful",
                            "schema": {
                                "type": "string"
                            }
                        }
                    }
                }
            },
            "/model/is_mad": {
                "get": {
                    "tags": [
                        "Model"
                    ],
                    "summary": "Set the person to mad mode",
                    "responses": {
                        "200": {
                            "description": "Returns 'ok' if successful",
                            "schema": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        }
    }


# Start webservice in debug mode
if __name__ == '__main__':
    app.run(debug=True, port=1110)
