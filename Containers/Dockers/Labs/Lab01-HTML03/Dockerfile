FROM amazonlinux:latest

# Install dependencies
RUN yum update -y && \
    yum install -y httpd && \
    yum search wget && \
    yum install wget -y && \
    yum install unzip -y

# change directory
RUN cd /var/www/html

# download webfiles
RUN wget https://s3.eu-west-1.amazonaws.com/www.profesantos.cloud/jupiter-website.zip

# unzip folder
RUN unzip jupiter-website.zip

# copy files into html directory
RUN cp -r jupiter-main/* /var/www/html/

# remove unwanted folder
RUN rm -rf jupiter-main main.zip

# exposes port 80 on the container
EXPOSE 80

# set the default application that will start when the container start
ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]