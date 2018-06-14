Version 0.1 documentation

# high level design

## openICTa main flow

## openICTA Ticket Connector flow
The Ticket connector is used for the connection between the openICTA implementation and a ticket system. In in theorie it is possible to have multiple ticket connectors connecting to multiple ticket systems working with a single openICTA implementation. The Ticket Connector is used to (A) collect new tickets for analysis, (B) update existing tickets with enriched information and (C) gather closed tickets to be put into the learing set of openICTA. The Ticket Connector will run by default in a Oracle Linux based Docker Container. 
![openICTA ticket connector](https://raw.githubusercontent.com/OracleLinuxWorld/inControlTicketAi/master/openICTA/documentation/docs/v01/openICTA_ticketConnector.png "openICTA ticket connector")

## openICTA NLP classifier flow
The NLP classifier is used to undertake NLP based actions on newly created tickets and forward the outcome in the form of a JSON object to the AI classifier. The NLP classifier is mainly based upon spaCy based python code and will be hosted in a "openICTA NLP" Oracle Linux based Docker container.
![NLP classifier](https://raw.githubusercontent.com/OracleLinuxWorld/inControlTicketAi/master/openICTA/documentation/docs/v01/openICTA_NLPclassifier.png "NLP classifier")

## openICTA  classifier flow
The AI classifier is used to undertake AI based actions on newly created tickets and return the results (predictions) back to the connector.




# dependencies
In case you run into an issue make sure you have all dependencies available on the system you try to run the code. Below is a list of all dependencies you will require to run all aspects of the openICTA

* spaCy     : pip install -U spacy
* spaCy-CLD : pip install spacy_cld
