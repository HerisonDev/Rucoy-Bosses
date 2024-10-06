import os
from together import Together

client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
    messages=[ {"role": "user", "content": [{ "type": "text", "text": "Pegue o texto em roxo no canto inferior esquerdo,e escreva apenas o texto que esta a esquerda dos 2 pontos da mensagem,apenas isso,tudo que estiver a direito dos : deve ser ignorado." },{ "type": "image_url", "image_url": { "url": 
            "https://raw.githubusercontent.com/HerisonDev/Rucoy-Bosses/refs/heads/main/img/Screenshot_20241005-231949.jpg" }}]} ])

print(response.choices[0].message.content)
