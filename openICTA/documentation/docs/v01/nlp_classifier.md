# openICTA NLP classifier

## openICTA NLP classifier flow
The NLP classifier is used to undertake NLP based actions on newly created tickets and forward the outcome in the form of a JSON object to the AI classifier. The NLP classifier is mainly based upon spaCy based python code and will be hosted in a "openICTA NLP" Oracle Linux based Docker container.
![NLP classifier](https://raw.githubusercontent.com/OracleLinuxWorld/inControlTicketAi/master/openICTA/documentation/docs/v01/openICTA_NLPclassifier.png "NLP classifier")

## REST API
The NLP classifier has a REST API endpoint to ensure other components can communicate with the NLP classifier using REST calls. The primary user of the NLP classifier REST API will be the ticket connector or ticket connectors. Due to the use of a REST API and by ensuring the NLP classifier can run in a Docker container the number of NLP classifiers (containers) can be scaled up or down based upon the number of tickets that need be analyzed. To ensure propper routing and balancing of requests a loadbalancer and/or API gateway need to be put in place to ensure propper handling of request routing. 

The REST API will be primarily using Flask (a python project) to provide the required REST API endpoints. The REST API definition will be done using a Swagger definition. 

### REST API endpoints

