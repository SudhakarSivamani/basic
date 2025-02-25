from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

@app.get("/")
async def index(request: Request):
    """Asynchronous function that returns a JSON response with the message 
    "Hello, FastAPI with Bootstrap!"."""
    return templates.TemplateResponse(request=request,name="index.html",context={"message": "Hello, FastAPI with Bootstrap!"}, status_code=status.HTTP_200_OK)