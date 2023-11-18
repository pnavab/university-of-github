# Before starting
We'll be making an API that simulates flipping a coin. First we must gather all required dependencies in case we do not already have it on our computer
- Install FastAPI by running `pip install fastapi`
- Install uvicorn by running `pip install uvicorn`

# Getting started
At the top of our code, we need to define the imports. FastAPI is used for creating API endpoints, and uvicorn allows FastAPi to handle the browser requests. Random is for simulating the coin flipping.

```
from fastapi import FastAPI
import uvicorn
import random
```

We must also create an instance of the FastAPI class, which we will call `app`
```
app = FastAPI()
```

# First API endpoint
We will make an HTTP GET endpoint, which fetches data we choose to return. Using the `@app.get` decorator, we define the endpoint at which we want it to be accessible at. Since this is our first one, let's make it accessible at "/". This is just the default URL, such as `google.com` or `localhost:8000`
```
@app.get("/")
def root():
    return({ "message": "hello world" })
```
In our `root()` function, we define a simple "hello world" JSON response as the return value.

# Running the server
With this code, it allows us to run the server if it is executed as a script, similar to a main method in Java. 
```
if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, reload=True)
```
Now open a terminal in the project directory and run `python {name}.py`