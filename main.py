import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app_db_api:app", host="localhost", port=8000, reload=True)
