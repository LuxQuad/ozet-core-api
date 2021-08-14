#!/bin/bash

PROTO_FILE_FOLDER_PATH=./app/grpc/protos
PROTO_FILE_PATH=./app/grpc/protos/helloworld.proto
PROTO_BUILD_OUT=./app/grpc/protos_python

python -m grpc_tools.protoc -I${PROTO_FILE_FOLDER_PATH} --python_out=${PROTO_BUILD_OUT} --grpc_python_out=${PROTO_BUILD_OUT} ${PROTO_FILE_PATH}