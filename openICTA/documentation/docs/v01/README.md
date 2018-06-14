Version 0.1 documentation

# high level design

## openICTa main flow

## openICTA NLP classifier flow
Ticket connector
![openICTA ticket connector](https://raw.githubusercontent.com/OracleLinuxWorld/inControlTicketAi/master/openICTA/documentation/docs/v01/openICTA_ticketConnector.png "openICTA ticket connector")

## openICTA NLP classifier flow
The NLP classifier is used to undertake NLP based actions on newly created tickets and forward the outcome in the form of a JSON object to the AI classifier. The NLP classifier is mainly based upon spaCy based python code and will be hosted in a "openICTA NLP" docker container.
![NLP classifier](https://raw.githubusercontent.com/OracleLinuxWorld/inControlTicketAi/master/openICTA/documentation/docs/v01/openICTA_NLPclassifier.png "NLP classifier")

## openICTA  classifier flow
The AI classifier is used to undertake AI based actions on newly created tickets and return the results (predictions) back to the connector.




# dependencies
In case you run into an issue make sure you have all dependencies available on the system you try to run the code. Below is a list of all dependencies you will require to run all aspects of the openICTA

* spaCy     : pip install -U spacy
* spaCy-CLD : pip install spacy_cld
