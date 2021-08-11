#!/bin/bash
TEST_RESULT_PATH=.pytest_results
py.test \
    -v \
    --cov=./ \
    --cov-report html:${TEST_RESULT_PATH}/htmlcov \
    --junitxml=${TEST_RESULT_PATH}/junit.xml