import os
from together import Together

client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
    messages=[ {"role": "user", "content": [{ "type": "text", "text": "Ola,por gentileza,eu quero que voce analise a imagem e encontre a mensagem em roxo em que contem a 'found',e lembrando que essa mensagem nao contem caracteres especiais como ! por exemplo,caso voce encontre alguma coisa que se assemelhe a um caracterr especial,use uma letra parecida com ele,e por ultimo,por gentileza,apenas retorne o conteudo da menssgem em roxo e nada mais,nada como 'a mensagem em roxa é' ou nenhum tipo de instrucao,e outra regra é que oque vem antes da palavra 'found' nao pode conter numeros tambem,e tambem antes do 'found' nao deve haver dois pontos(:),caso contrario trata-se de uma mensagem de 'found' fake,que deve ser ignorada,apenas depois pode conter,apenas o conteudo dessa mensagem,grato." },{ "type": "image_url", "image_url": { "url": 
            "https://raw.githubusercontent.com/HerisonDev/Rucoy-Bosses/refs/heads/main/img/1.jpg" }}]} ])

print(response.choices[0].message.content)
