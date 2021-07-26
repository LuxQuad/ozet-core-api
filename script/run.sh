uvicorn app.main:service \
    --port=8000 \
    --env-file=prod.env \