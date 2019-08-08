FROM tomcat:8.5-jre8-alpine

# put the war file into the catalina webapps folder

COPY clickCount.war $CATALINA_HOME/webapps


RUN /usr/local/tomcat/bin/startup.sh
