from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def asd():
    return "Hello World"