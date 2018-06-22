# wsgi will be called to start the core functionality. This 
# will be done with a gunicorn --bind 0.0.0.0:8000 wsgi as
# part of the container startup. You will have to ensure 
# that a appcore.py file is available which will contain 
# all the main code that needs to run. From appcore(.py) 
# we will import application and gunicorn will ensure the
# code runs. 

from appcore import application

if __name__ == "__main__":
    application.run()
