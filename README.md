# Before starting
We'll be making an API that simulates flipping a coin. First we must gather all required dependencies in case we do not already have it on our computer
- Install FastAPI by running `pip install fastapi`
- Install uvicorn by running `pip install uvicorn`

# Getting started
At the top of our code, we need to define the imports. FastAPI is used for creating API endpoints, and uvicorn allows FastAPI to handle the browser requests. Random is for simulating the coin flipping.

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
With this code, it allows us to run the server if it is executed as a script, similar to a main method in Java. It will run on port 8000 of your computer and will watch for any changes to the code to reload the server.
```
if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, reload=True)
```

By now the code should look like:
```
from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get("/")
def root():
    return({ "message": "hello world" })

if __name__ == "__main__":
uvicorn.run("server:app", port=8000, reload=True)
```

Now open a terminal in the project directory and run `python {file_name}.py`, which is running on port 8000. Open a browser and go to `localhost:8000`. You should see the JSON output we defined at the "/" endpoint.

# Flip Coin Endpoint
Just like before, we'll define another GET endpoint. This time, it will have the functionality of simulating a coin flip when we access the `"/flip-coin"` endpoint. 
```
@app.get("/flip-coin")
def flip_coin():
```

For the coin flipping logic, we can use the `random` library we imported earlier to generate a number between 0 and 1. Less than 0.5 will mean heads, otherwise it will mean tails. Once we generate the random number and check the value, we can assign it to a `head_tail` variable as a string which we will return later. The JSON return value will be the word "value" followed by the variable that holds the result of the random coin flip.
```
@app.get("/flip-coin")
def flip_coin():
    val = random.random()
    head_tail = ""
    if(val <= 0.5):
        head_tail = "heads"
    else:
        head_tail = "tails"
    return({ "value": head_tail })
```

The endpoint should automatically reload every time you save a change to the code, so if it is still running from our previous test then the new endpoint should be active. Otherwise, run the server again by doing `python {file_name}.py` in the project directory. In the browser, go to `localhost:8000/flip-coin` and you should see a JSON response of either heads or tails. Reload the page (you can spam Ctrl+R) and it will flip a coin every time!!

# Flip Coins (plural) Endpoint
Now we'll make a third endpoint that uses query parameters to determine how many times we will flip a coin. Query parameters are key-value pairs in a URL that follow an endpoint. For example, in `www.domain.com/endpoint?variable=value`, the parameter name `variable` holds the parameter value of `value` which we access through the parameter name. Query parameters can also be chained using `&`, for example `www.domain.com/endpoint?var1=val1&var2=val2`.

Accessing query parameters from an endpoint varies on the language and framework, but for FastAPI, we define the query parameters we want to access in the function's parameters. Declaring the data type also allows the endpoint to convert the value to that type and validate against it. Our new `"/flip-coins` endpoint will have a `times` parameter that we give a value to, such as `?times=10`. 
```
@app.get("/flip-coins")
def flip_coins(times: int):
```

We want to make sure that the number from the query parameter is something we can work with, so before we start flipping coins, let's make sure it's greater than 0. The JSON response will be in the format of `{"heads": 5, "tails": 5}`, so we will have a head_count and tail_count that increments as we go along. Using the same logic from before, we'll flip a coin and increment `head_count` if the random number is less than 0.5, otherwise increment `tail_count`. We do that `times` times. The return JSON will be 2 key-value pairs this time, one for heads and one for tails using the variables we incremented.
```
@app.get("/flip-coins")
def flip_coins(times: int):
    if times and times > 0:
        head_count = 0
        tail_count = 0
        for _ in range(times):
            val = random.random()
            if(val <= 0.5):
                head_count += 1
            else:
                tail_count += 1
        return({ "heads": head_count, "tails": tail_count })
    else:
        return({ "message": "you need to send valid times" })
```

Run the server like before and go to `localhost:8000/flip-coins`. It will give an error both in the browser and in the terminal logs that the endpoint is not valid since we require a times to be sent in order to run our endpoint. Now go to `localhost:8000/flip-coins?times=10`. It will generate a different output every time you refresh the page, and you can also change the number of coins flipped in the query parameter. 

One way to bypass the error at `localhost:8000/flip-coins` would be to add a default value to the `times` parameter. If we set the default value to something like 10, such as:
```
@app.get("/flip-coins")
def flip_coins(times: int = 10):
```
If we try going to `localhost:8000/flip-coins` with no query parameters, it will default to flipping 10 coins.