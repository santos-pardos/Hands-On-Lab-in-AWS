FROM ruby:2.5
EXPOSE 8080
COPY helloworld.rb .
CMD ruby helloworld.rb
