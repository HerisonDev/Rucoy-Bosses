import os
from together import Together

client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
    messages=[ {"role": "user", "content": [{ "type": "text", "text": "Ola,voce pode descrever essa imagem??" },{ "type": "image_url", "image_url": { "url": 
            "https://cursos.alura.com.br/assets/images/immersion/logo_imersao_dev_gemini.png" }}]} ])

print(response.choices[0].message.content)
