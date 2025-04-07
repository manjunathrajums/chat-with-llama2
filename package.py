#Download th ollama package and llama2 model using the command line:
# pip install ollama
# ollama pull llama2
import ollama
from httpx import ReadError
client = ollama.Client()
model = "llama2"  
prompt = "What is Python?"
try:
    response = client.generate(model=model, prompt=prompt)
    print("Response from Ollama:")
    print(response.response)
except ReadError as e:
    print("Failed to connect to the Ollama server:", e)