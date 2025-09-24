#############################
# Builder
#############################
FROM gradle:8.7-jdk17 AS builder

WORKDIR /app

COPY . /app

RUN gradle build --no-daemon

#############################
# Java Runtime
#############################
FROM openjdk:17

WORKDIR /app

COPY --from=builder /app/build/libs/java-grpc-lab-1.0-SNAPSHOT.jar app.jar

CMD ["java", "-jar", "app.jar"]
