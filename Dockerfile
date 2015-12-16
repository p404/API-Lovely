# Lovely API Container
FROM p404/python3.4:latest
MAINTAINER Pablo Opazo "p@sequel.ninja"

# Run pip install in a cache efficient way
COPY requirements.txt /tmp/
RUN pip3.4 install -r /tmp/requirements.txt

# Add init script's
RUN mkdir -p /etc/my_init.d
ADD bash_scripts/django_tasks.sh /etc/my_init.d/django_tasks.sh
RUN chmod +x /etc/my_init.d/django_tasks.sh
ADD bash_scripts/webserver.sh /etc/my_init.d/webserver.sh
RUN chmod +x /etc/my_init.d/webserver.sh

