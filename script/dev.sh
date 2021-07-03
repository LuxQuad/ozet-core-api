uvicorn app.main:app \
    --port=8000 \
    --reload-dir=app \
    --env-file .env \
