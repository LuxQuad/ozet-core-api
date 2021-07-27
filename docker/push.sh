#!/bin/bash
docker buildx build --platform linux/x86_64 -t bartkim07120/esume-core-api:latest .
docker push bartkim07120/esume-core-api:latest