#cria a aplicação web
from fastapi import FastAPI

#Permite que o site (HTML) acesse a API, mesmo que esteja em outra porta/domínio
from fastapi.middleware.cors import CORSMiddleware

#Cria um “modelo de dados” que descreve como a pergunta chega
from pydantic import BaseModel

#Biblioteca oficial para se comunicar com a API do ChatGPT
from openai import OpenAI

#Lê o arquivo .env onde está sua chave da OpenAI
import os
from dotenv import load_dotenv

#Permite servir arquivos HTML/CSS/JS (seu site)
from fastapi.staticfiles import StaticFiles

#Função criada em documentos.py para ler os arquivos da pasta dados/
from documentos import extrair_todos_dados


#carrega a chave do openai
load_dotenv()
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#cria o app (objeto principal)
app = FastAPI()

#Habilita CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#modelo de pergunta que o site envia
class Pergunta(BaseModel):
    pergunta: str

dados_cartorio = extrair_todos_dados("dados")

#Rota principal da API
@app.post("/api/consulta")
async def consultar(pergunta: Pergunta):
    prompt = f"""
        Você é um assistente jurídico. Responda apenas com base nas informações abaixo.
Se não souber, diga que não encontrou a resposta nos dados fornecidos.

[DADOS DISPONÍVEIS]
{dados_cartorio}

[PERGUNTA]
{pergunta.pergunta}
"""

    try:
        resposta = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente jurídico útil e claro."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=700,
            temperature=0.3
        )
        return {"resposta": resposta.choices[0].message.content.strip()}
    except Exception as e:
        return {"erro": f"Erro ao consultar IA: {str(e)}"}

# Servir arquivos estáticos (frontend)
app.mount("/", StaticFiles(directory="assistente/public", html=True), name="site")
