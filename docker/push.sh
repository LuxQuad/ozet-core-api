#!/bin/bash
docker buildx build --platform linux/x86_64 -t luxquad/esume-api:latest .
docker push luxquad/esume-api:latest