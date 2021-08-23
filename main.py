import os
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import random
import mistune
from dotenv import load_dotenv


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/favicon.ico")
async def favicon(): return FileResponse('./static/favicon.ico')

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    with open('README.md', 'r') as readme:
        readme_content = readme.read()
        return templates.TemplateResponse("index.html", {
            "request": request,
            "readme": mistune.html(readme_content)
        })

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', "8000")))
