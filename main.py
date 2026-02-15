from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5-coder"
history = []

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask(prompt: str = Form(...)):
    history.append({"role": "user", "content": prompt})
    
    # Keep history manageable (last 10 messages)
    context = history[-10:]

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                OLLAMA_URL, 
                json={"model": MODEL, "messages": context, "stream": False}
            )
            data = response.json()
            answer = data.get("message", {}).get("content", "No response from model.")
            history.append({"role": "assistant", "content": answer})
            return {"output": answer}
    except Exception as e:
        return JSONResponse(status_code=500, content={"output": f"Error: {str(e)}"})