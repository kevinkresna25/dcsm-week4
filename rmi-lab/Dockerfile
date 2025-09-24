FROM openjdk:17

WORKDIR /app
COPY . /app

RUN javac thelol/hello/*.java

CMD ["java", "thelol.hello.Server"]
