#!/bin/bash
docker buildx build --platform linux/x86_64 -t bart07120/esume-api:latest .
docker push bart07120/esume-api:latest