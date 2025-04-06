from fastapi import FastAPI
import random

app = FastAPI()

# http://127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

# http://127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"message": "função de teste 1"}


# http://127.0.0.1:8000/outrospontos
@app.get("/outrospontos")
async def funcaoteste():
    return {"message": "outrospontos"}
=======
# http://127.0.0.1:8000/randnum
@app.get("/randnum")
async def funcaoteste2():
    return {"message": True, "Numero Random": random.randint(0, 1000)}

