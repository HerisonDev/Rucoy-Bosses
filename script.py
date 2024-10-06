import os
from together import Together

client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
    messages=[ {"role": "user", "content": [{ "type": "text", "text": "Envolva entre asteristicos o conteudo da mensagem em roxo,mas a mensagem em roxo deve conter as palavras 'found' e 'The Rat King',e a mensagem em roxo tambem nao deve conter 2 pontos(:),qualquer outra mensagem em roxo que nao tiver essas caracteristicas devem ser ignoradas.Eu nao quero que voce passe nenhuma instrucao e nenhuma outra mensagem,apenas o conteudo da mensagem em roxo e nada mais,seja direto!" },{ "type": "image_url", "image_url": { "url": 
            "https://raw.githubusercontent.com/HerisonDev/Rucoy-Bosses/refs/heads/main/img/1.jpg" }}]} ])

print(response.choices[0].message.content)
