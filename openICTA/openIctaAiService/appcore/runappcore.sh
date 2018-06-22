!/bin/bash
# runappcore.sh is used as a script which is started by
# the container to ensure you start gunicorn and the 
# correct appcore code. The start of the appcore is done
# in 3 stages as marked in the code below. 

# STAGE 0
# source the Python virtualenv to ensure we can run Gunicorn,
# as part of the base docker image that is used you will have 
# a fixed location for you virtualenv. This is also the location
# where you will have to deploy your Python aplication
source /myprojectenv/bin/activate


# STAGE 1
# A placeholder where you can do things like loading a learning
# set or other things you need to have activated before you start 
# the actual appcore. At this stage you can use the virtualenv 
# (if required) or you can use any other (availabel) command. The
# reason for this position of the placeholder is that you can use
# all functions within the context of the virtualenv. 


# STAGE 2
# start gunicorn and bind this on all interfaces on port 8000.
# do note that this command expects to have a wsgi.py file in
# the virtualenv (in this case /myprojectenv). Within the logic
# of wsgi.py you will need to define the flask project .py file
# that you want to start. 
cd /myprojectenv
gunicorn --bind 0.0.0.0:8000 wsgi
