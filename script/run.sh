#!/bin/bash
PORT=8000
ENV=prod.env
SERVICE=app.main:service

uvicorn ${SERVICE} --port=${PORT} --reload --env-file=${ENV}
