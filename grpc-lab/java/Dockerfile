#############################
# Builder
#############################
FROM gradle:8.7-jdk17 AS builder

WORKDIR /app

COPY . /app

RUN gradle clean build --no-daemon

#############################
# Java Runtime
#############################
FROM openjdk:17

WORKDIR /app

COPY --from=builder /app/build/libs/app-all.jar thelol.jar

CMD ["java", "-jar", "thelol.jar"]
