import os
from together import Together

client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
    messages=[ {"role": "user", "content": [{ "type": "text", "text": "No canto inferior esquerdo,existe uma mensagem em roxo,eu quero que voce me retorne como resposta apenas o conteudo dessa mensagem em roxo,as demais mensagens das cores verde,amarelo e branca devem ser ignoradas.A sua resposta deve ser apenas o conteudo da mensagem em branco que contem as palavras 'found' e 'Rat King'." },{ "type": "image_url", "image_url": { "url": 
            "https://raw.githubusercontent.com/HerisonDev/Rucoy-Bosses/refs/heads/main/img/1.jpg" }}]} ])

print(response.choices[0].message.content)
