from flask import Flask, jsonify
application = Flask(__name__)

# global variables used throuout the application
appVersion = "0.0.1" 


# Provide the API endpoint / for the end user to
# request. the function returnRoute is the main
# function used to facilitate the request on this
# specific endpoint
@application.route("/")
def returnRoot():
    return "cora-ai"


# provide the API endpoint /version for the end 
# user to request. The function returnVersion is
# used primarily to returnt the response to the 
# requesting party. The main use for this 
# specific endpoint is to provide the versions 
# of both the applcaition as well as the version 
# of the API definition which is used within this
# specific release. 
@application.route("/version")
def returnVersion():
#    return appVersion
#     return "{ {version}}"
    return jsonify(
        username="johan",
        email="xxatyy",
        id="someid"
    )


@application.route("/swagger")
def returnSwagger():
    return "<h1 style='color:blue'>hallo!</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
