# Lab 1: Building a Web API with Phi-3.5

## Sinh viên thực hiện
- **Họ tên:** Mai Văn Hiển
- **MSSV:** 24120308
- **Môn học:** Tư duy tính toán (Computational Thinking)

## Thông tin mô hình
- **Model:** Phi-3.5-mini-instruct
- **Hugging Face Link:** [https://huggingface.co/microsoft/Phi-3.5-mini-instruct](https://huggingface.co/microsoft/Phi-3.5-mini-instruct)
- **Chức năng:** Chatbot hỗ trợ trả lời câu hỏi và tư vấn thông tin tổng quát.

## Hướng dẫn cài đặt
1. Clone repository: `git clone https://github.com/MaiHien3507/Phi-3.5-mini-instruct-lab1.git`
2. Cài đặt thư viện: `pip install -r requirements.txt`

## Cách chạy chương trình
1. Chạy Server: `uvicorn main:app --host 0.0.0.0 --port 8000`
2. Mở đường hầm (Tunnel) để có link Public bằng Pinggy:
   `ssh -p 443 -R0:localhost:8000 qr@a.pinggy.io`

## Hướng dẫn gọi API
- **Endpoint:** `POST /generate`
- **Request Body:**
```json
{
  "prompt": "Your question here"
}

## Video demo
<div align="center">
  <video src="https://github.com/user-attachments/assets/f39c408c-34e5-4fa2-90c1-bba83af2001c" width="100%" controls autoplay muted loop>
  </video>
</div>

