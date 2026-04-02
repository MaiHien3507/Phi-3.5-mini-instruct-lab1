import requests

# Link chạy local hoặc thay bằng link Pinggy 
BASE_URL = "http://127.0.0.1:8000" 

def test_root():
    print("--- Testing GET / ---")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Result: {response.json()}\n")

def test_health():
    print("--- Testing GET /health ---")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Result: {response.json()}\n")

def test_generate():
    print("--- Testing POST /generate ---")
    payload = {"prompt": "How is rice made?"}
    response = requests.post(f"{BASE_URL}/generate", json=payload)
    if response.status_code == 200:
        print(f"AI Response: {response.json().get('response')}\n")
    else:
        print(f"Error: {response.text}\n")

if __name__ == "__main__":
    test_root()
    test_health()
    test_generate()