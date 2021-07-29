#!/bin/bash

python -m grpc_tools.protoc -I./app/grpc/protos --python_out=./app/grpc --grpc_python_out=./app/grpc ./app/grpc/protos/helloworld.proto