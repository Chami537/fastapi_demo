from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello from my cloud server!",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello/{name}")
def hello(name: str):
    return {
        "message": f"Hello, {name}!"
    }

@app.get("/server")
def server():
    return{
        "server":"Alibaba Cloud",
        "deployed_with":"Docker",
        "status":"online"

    }

@app.get("/xubi")
def xubi():
    return {
        "xubi":"xubimeiyouma"
    }
