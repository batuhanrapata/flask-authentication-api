# flask-authentication-api
Flask authentication api mongoDB with using JWT token and password hashing

Application Structure
```
.
└── flask-authentication/
    ├── src/
    │   ├── blueprints/
    │   │   └── endpoints.py
    │   ├── app.py
    │   ├── routes.py
    │   ├── db.py
    │   └── .env
    └── wsgi.py 
```

## Register Endpoint *register_endpoint.py*
The request data is validated to ensure that the username, password, and email address are valid. If any of the validation checks fail, an appropriate error message is returned. If all checks pass, the user's data is inserted into a MongoDB database using the PyMongo library.

The response is returned in JSON format with a "status" key indicating whether the operation was successful or not, and an optional "error" key containing an error message if the operation was unsuccessful. If the operation was successful, a unique ID for the user is also returned in the response.

## Login Endpoint *login_endpoint.py*
The request data is validated by checking if the provided username and password exist in the MongoDB database using PyMongo library. If the username and password combination is correct, a JWT token is generated using the PyJWT library, containing the unique ID of the user from the MongoDB database.

The response is returned in JSON format with a "status" key indicating whether the operation was successful or not, and an optional "error" key containing an error message if the operation was unsuccessful. If the operation was successful, the unique ID for the user and a JWT access token is also returned in the response.

## List Users Endpoint *list_users_endpoint.py*
This is a Flask blueprint that defines a route for retrieving a list of all users from a MongoDB database. The route is protected by a token authentication system implemented using the token_required decorator. The token_required decorator checks if the request contains a valid access token in the x-access-token header. If the token is missing or invalid, it returns a 401 unauthorized error with a message. If the token is valid, it decodes the token to get the user ID, retrieves the user document from the database using the ID, and passes the user document to the decorated function as the current_user argument.

The get_all_users function retrieves all user documents from the MongoDB collection and constructs a JSON response containing an array of user data. For each user document, it extracts the username field and creates a dictionary containing only the username field. The dictionaries for all users are appended to the output list, which is then returned as part of the JSON response. If the current_user argument is None, the function returns a JSON response with an error message stating that the user is not authorized to perform the operation.

## Health Check Endpoint *health_check_endpoint.py*
When a GET request is made to this endpoint, the function returns a JSON response containing a success status message ('status': 'success'), an OK message ('message': 'OK'), and the current timestamp ('timestamp': datetime.datetime.now(timezone.utc)). This is a simple way to check if the API is running and responding to requests.

## Database Connection *db.py*
This code connects to a MongoDB database using the pymongo library and the credentials stored in a .env file. The get_db() function creates a MongoClient object using the MONGO_URI environment variable, and returns the database object specified by the MONGO_DBNAME and MONGO_COLLECTION environment variables.

The .env file is used to store sensitive information such as passwords and API keys, and is not pushed to version control. In this code, the load_dotenv() function is used to load environment variables from the .env file into the Python environment. The os.getenv() function is used to retrieve the values of the environment variables specified in the .env file.


## App.py
This code sets up a Flask application instance named app and loads routes defined in routes.py using the initialize_routes function. It also sets the Flask app's SECRET_KEY from an environment variable named SECRET_KEY loaded from a .env file using the load_dotenv() function from the python-dotenv library.

The SECRET_KEY is used by Flask to sign and verify cookies and sessions, and to generate secure tokens, among other things. It is important to keep this value secret and not share it publicly.

## Web Service Application Gateaway *wsgi.py*
This wsgi.py file is a script that is used to launch the Flask application as a WSGI application. WSGI (Web Server Gateway Interface) is a standard interface between web servers and Python web applications or frameworks. The wsgi.py file is executed by the web server and it loads the Flask application object from src.app module and runs it using a web server.

The if __name__ == "__main__": statement checks if the script is being run directly from the command line or not. If it is being run directly, then the Flask application is started using the app.run() method. In this case, the Flask application will be accessible at http://localhost:5000/ with debugging enabled (debug=True). The host parameter specifies the IP address of the machine where the application will be run, and port parameter specifies the port number on which the application will be listening for incoming requests.
