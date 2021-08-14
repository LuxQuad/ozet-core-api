import uvicorn

HOST = "127.0.0.1"
PORT = 8000
ENV = ".misc/env/prod.env"
SERVICE = "app.main:service"
LOG_LEVEL = "info"

if __name__ == "__main__":
    uvicorn.run(SERVICE, host=HOST, port=PORT, log_level=LOG_LEVEL, workers=8, env_file=ENV, reload=False)
