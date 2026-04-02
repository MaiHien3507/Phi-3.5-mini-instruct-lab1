from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
import uvicorn
import threading
from chatbot_logic import Phi3Chatbot

chatbot = Phi3Chatbot("./config.yaml")

class ChatRequest(BaseModel):
    prompt: str

app = FastAPI()
nest_asyncio.apply()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
async def root():
    return {
        "system_name": "Hệ thống Chatbot Hướng dẫn du lịch Phi-3.5",
        "description": "API này sử dụng mô hình Phi-3.5-mini-instruct để tư vấn về du lịch Việt Nam."
    }

@app.get('/health')
async def health_check():
  try:
    is_alive= torch.cuda.is_available()
    return {
        "status": "ready" if is_alive else "error",
        "gpu_connected": is_alive,
        "model_name": "Phi-3.5-mini-instruct"
    }
  except:
      return {"status": "not ready", "reason": "Model not loaded"}

@app.post('/generate')
async def generate_api(request: ChatRequest):
    # Kiểm tra dữ liệu đầu vào cơ bản (Yêu cầu: Xử lý thiếu dữ liệu)
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt không được để trống")
    try:
      response = chatbot(request.prompt)
      return {"status": "success", "response": response}
    except Exception as e:
        # Xử lý lỗi trong quá trình suy luận (Yêu cầu: Xử lý lỗi hợp lý)
        raise HTTPException(status_code=500, detail=f"Lỗi mô hình: {str(e)}")

# Hàm chạy server trong luồng riêng
def run_api():
    # Giải phóng cổng 8000 nếu bị kẹt
    !fuser -k 8000/tcp
    uvicorn.run(app, host="0.0.0.0", port=8000)

threading.Thread(target=run_api, daemon=True).start()
