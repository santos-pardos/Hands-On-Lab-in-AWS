FROM openjdk
RUN useradd -ms /bin/bash ojdk
RUN mkdir -p /home/ojdk/app/ && chown -R ojdk:ojdk /home/ojdk/app
WORKDIR /home/ojdk/app
COPY *.java ./
COPY junit-* ./
USER ojdk
RUN javac -cp "junit-4.10.jar:." *.java
COPY --chown=ojdk:ojdk . .
CMD [ "java", "-cp", "junit-4.10.jar:.","org.junit.runner.JUnitCore","TestAdd","TestSub"]
