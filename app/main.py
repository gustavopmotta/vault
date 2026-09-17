from fastapi import FastAPI

app = FastAPI(
	title="Vault API",
	version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "Vault API is running!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
