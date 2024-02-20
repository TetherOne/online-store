from fastapi import Request
from fastapi import FastAPI

import uvicorn



app = FastAPI()



@app.get('/')
def hello_world(request: Request):
    return {'message': 'hello world'}



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)