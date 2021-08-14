#!/bin/bash
DOCKER_IMAGE_NAME=bartkim07120/ozet-core-api

docker buildx build --platform linux/x86_64 -t ${DOCKER_IMAGE_NAME}:latest .
docker push ${DOCKER_IMAGE_NAME}:latest