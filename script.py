import os
from together import Together

client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
    messages=[ {"role": "user", "content": [{ "type": "text", "text": "Ola,voce pode descrever essa imagem??" },{ "type": "image_url", "image_url": { "url": 
            "https://raw.githubusercontent.com/HerisonDev/Rucoy-Bosses/refs/heads/main/img/Screenshot_20241005-231949.jpg" }}]} ])

print(response.choices[0].message.content)
