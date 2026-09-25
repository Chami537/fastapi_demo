from fastapi import FastAPI
import os
import psycopg
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



@app.get("/db-health")
def db_health():
    database_url = os.getenv("DATABASE_URL")

    with psycopg.connect(database_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            version = cur.fetchone()[0]

    return {
        "status": "connected",
        "database": version
    }