if   [  $SERVER_PORT  ];
then
   /usr/local/src/jdk-11.0.9/bin/java -Dserver.port=$SERVER_PORT -jar /usr/local/src/tailbaseSampling-1.0-SNAPSHOT.jar &
else
   /usr/local/src/jdk-11.0.9/bin/java -Dserver.port=8000 -jar /usr/local/src/tailbaseSampling-1.0-SNAPSHOT.jar &
fi
tail -f /usr/local/src/start.sh
