FROM nginx:latest

# Delete Defaul Conf file
RUN rm /etc/nginx/conf.d/default.conf
#Copy custom conf file to directory
COPY default.conf /etc/nginx/conf.d

# SSL Cert Setup

# Delete Defaul Sources.List
RUN rm /etc/apt/sources.list
#Copy custom Sources.list
COPY sources.list /etc/apt/sources.list

#update apt
RUN apt-get update

#install Certbot
RUN apt-get install certbot python-certbot-nginx -t stretch-backports -y

