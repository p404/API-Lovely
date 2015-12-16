# Lovely API Container
FROM p404/python3.4:latest
MAINTAINER Pablo Opazo "p@sequel.ninja"

# Installing application pip packages
RUN mkdir /djangoapp
ADD . /djangoapp
RUN pip3.4 install -r /djangoapp/requirements.txt

# Add custom script's
RUN mkdir -p /etc/my_init.d
#ADD bash_scripts/webserver.sh /etc/my_init.d/webserver.sh
ADD bash_scripts/migrations.sh /etc/my_init.d/migrations.sh


