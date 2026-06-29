from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "application": "Alpha Apparel",
        "status": "online"
    }