FROM openjdk:8-jre-alpine3.9
 
# copy the packaged jar file into our docker image
COPY target/palindromeCount-1.0-SNAPSHOT-jar-with-dependencies.jar /server.jar
 
# set the startup command to execute the jar
CMD ["java", "-jar", "/server.jar"]