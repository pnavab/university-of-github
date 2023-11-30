from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import random

app = FastAPI()

origins = ["*"]  # You can replace "*" with your frontend domain(s)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return({ "message": "hello world" })

@app.get("/flip-coin")
def flip_coin():
    val = random.random()
    head_tail = ""
    if(val <= 0.5):
        head_tail = "heads"
    else:
        head_tail = "tails"
    return({ "value": head_tail })

@app.get("/flip-coins")
def flip_coins(times: int = 10):
    if times and times > 0:
        head_count = 0
        tail_count = 0
        for i in range(times):
            val = random.random()
            if(val <= 0.5):
                head_count += 1
            else:
                tail_count += 1
        return({ "heads": head_count, "tails": tail_count })
    else:
        return({ "message": "you need to send valid times" })

if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, reload=True)