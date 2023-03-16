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

# Register Endpoint
The request data is validated to ensure that the username, password, and email address are valid. If any of the validation checks fail, an appropriate error message is returned. If all checks pass, the user's data is inserted into a MongoDB database using the PyMongo library.

The response is returned in JSON format with a "status" key indicating whether the operation was successful or not, and an optional "error" key containing an error message if the operation was unsuccessful. If the operation was successful, a unique ID for the user is also returned in the response.

# Login Endpoint
The request data is validated by checking if the provided username and password exist in the MongoDB database using PyMongo library. If the username and password combination is correct, a JWT token is generated using the PyJWT library, containing the unique ID of the user from the MongoDB database.

The response is returned in JSON format with a "status" key indicating whether the operation was successful or not, and an optional "error" key containing an error message if the operation was unsuccessful. If the operation was successful, the unique ID for the user and a JWT access token is also returned in the response.

# List Users Endpoint
This is a Flask blueprint that defines a route for retrieving a list of all users from a MongoDB database. The route is protected by a token authentication system implemented using the token_required decorator. The token_required decorator checks if the request contains a valid access token in the x-access-token header. If the token is missing or invalid, it returns a 401 unauthorized error with a message. If the token is valid, it decodes the token to get the user ID, retrieves the user document from the database using the ID, and passes the user document to the decorated function as the current_user argument.

The get_all_users function retrieves all user documents from the MongoDB collection and constructs a JSON response containing an array of user data. For each user document, it extracts the username field and creates a dictionary containing only the username field. The dictionaries for all users are appended to the output list, which is then returned as part of the JSON response. If the current_user argument is None, the function returns a JSON response with an error message stating that the user is not authorized to perform the operation.

# Health Check Endpoint
When a GET request is made to this endpoint, the function returns a JSON response containing a success status message ('status': 'success'), an OK message ('message': 'OK'), and the current timestamp ('timestamp': datetime.datetime.now(timezone.utc)). This is a simple way to check if the API is running and responding to requests.
