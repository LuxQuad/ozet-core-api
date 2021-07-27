#!/bin/bash
docker buildx build --platform linux/x86_64 -t luxquad/esume-core-api:latest .
docker push luxquad/esume-core-api:latest