TEST_RESULT_PATH=.pytest_results
py.test \
    -v \
    --cov=apps \
    --cov=utils \
    --cov-report html:${TEST_RESULT_PATH}/htmlcov \
    --junitxml=${TEST_RESULT_PATH}/junit.xml
