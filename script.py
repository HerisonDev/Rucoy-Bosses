import os
from together import Together

client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
    messages=[ {"role": "user", "content": [{ "type": "text", "text": "Analise a imagem e me retorne apenas a mensagem em roxo,que tem uma fonte baseada em 8-bits,que fica no canto inferior,porem eu quero que voce pegue apenas a mensagem que nao possui caracteres especiais como '!',':' e numeros,,e se tiver mais de uma mensagem roxa,analise bem as mensagens e retorne apenas a mensagem que contem a dewcricao passada,e eu quero que voce retorne apenas uma mensagem roxa,pois se voce analisar na inagem,cada mensagem fica embaixo da outra,entao retorne apenas uma,e por ultimo,eu quero que voce seja direto na resposta,apenas retornando a mensagem roxa.E se voce analisar a imagem e nao encontrar nenhuma mensagem roxa que tenha essas caracteristicas,retorne a mensagem 'not found'."},{ "type": "image_url", "image_url": { "url": 
            "https://raw.githubusercontent.com/HerisonDev/Rucoy-Bosses/refs/heads/main/img/2.jpg" }}]} ])

print(response.choices[0].message.content)
