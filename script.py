import os
from together import Together

# Lê o conteúdo do arquivo txt e armazena o nome do arquivo
with open("/tmp/ultimo_arquivo_renomeado.txt", "r") as file:
    nome_do_arquivo = file.read().strip()  # Remove qualquer espaço ou nova linha extra

# Cria a URL com o nome do arquivo lido
url_da_imagem = f"https://raw.githubusercontent.com/HerisonDev/Rucoy-Bosses/refs/heads/main/img/{nome_do_arquivo}"

# Inicializa o cliente
client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

# Realiza a requisição com a URL dinâmica
response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Me retorne o texto roxo,que tem as palavras 'found',qie tem colchetes,e que não possue dois pontos antes da palavra 'found',e se atente no que esta escrito dentro dos colchetes,pois é o servidor,é nescessario que ele esteja correto,e uma regra que esse texto em roxo tem é antes da palavra 'found',oque vier nao pode conter caractere especial como exclamacao ou colchetes e nem numeros,apenas letras,obrigado"},
            {"type": "image_url", "image_url": {"url": url_da_imagem}}
        ]
    }]
)

# Imprime a resposta
print(response.choices[0].message.content)
