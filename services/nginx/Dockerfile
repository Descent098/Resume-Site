FROM nginx:latest

# Delete Defaul Conf file
RUN rm /etc/nginx/conf.d/default.conf
#Copy custom conf file to directory
COPY default.conf /etc/nginx/conf.d

RUN apt-get update