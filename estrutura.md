# Iris Project - Assistente Jurídico Inteligente

Este é o repositório principal do **Iris Project**, um sistema de assistente jurídico baseado em IA com backend em Python (FastAPI), integração com a API da OpenAI, e um frontend simples para interação. Os dados são mantidos em arquivos locais (PDF, CSV, TXT), com suporte a indexação e painel administrativo para gestão de conteúdo.

---

## 🌍 Estrutura Geral do Projeto

```bash
IRIS_PROJECT/
├── .env
├── requirements.txt
├── README.md
│
├── assistente/
│   ├── backend/
│   │   ├── main.py
│   │   ├── documentos.py
│   │   ├── database.py
│   │   └── __init__.py
│   ├── public/
│   │   ├── index.html
│   │   ├── style.css
│   │   └── app.js
│
├── painel_admin/
│   ├── backend/
│   │   ├── admin_api.py
│   │   └── utils.py
│   ├── public/
│   │   ├── index.html
│   │   ├── painel.js
│   │   └── painel.css
│
├── dados/
│   ├── sao_paulo/
│   │   ├── casamento.pdf
│   │   ├── nascimento.csv
│   │   └── resumo.txt
│   ├── minas_gerais/
│   │   └── escritura.txt
│   └── metadados.json
│
└── scripts/
    └── atualizar_metadados.py
```

---

## 🔍 Explicação dos Diretórios e Arquivos

### `.env`
Contém chaves e segredos como a `OPENAI_API_KEY`.

### `requirements.txt`
Lista das dependências Python do projeto:
```
fastapi
uvicorn
openai
python-dotenv
PyMuPDF
pandas
```

### `README.md`
Este arquivo. Contém instruções e estrutura do projeto.

---

## 🧱 Pasta `assistente/` - Site principal (usuário final)

### `backend/main.py`
API principal FastAPI que recebe perguntas, busca dados, chama a OpenAI e retorna respostas.

### `documentos.py`
Funções para ler PDFs, arquivos `.txt`, `.csv`, `.xlsx` etc.

### `database.py`
(opcional) Leitura de `metadados.json` ou acesso a um banco SQLite.

### `public/`
Frontend simples com HTML, CSS e JS. Interface de chat parecida com o ChatGPT.

---

## 📅 Pasta `painel_admin/` - Painel interno para edição de dados

### `backend/admin_api.py`
API que permite uploads, edição de metadados, deleção de arquivos.

### `public/`
Interface web para painel administrativo com botões de upload, formulários e gerenciamento.

---

## 📂 Pasta `dados/` - Base de documentos da IA

Organizada por estado/cartório, com arquivos reais:
- `PDFs`: regulamentos, leis
- `TXTs`: transcrições
- `CSVs`: tabelas

### `metadados.json`
Lista estruturada com informações sobre cada arquivo (tipo, estado, cartório, data, assunto).
Usado para busca e indexação inteligente.

---

## 📃 Pasta `scripts/`

### `atualizar_metadados.py`
Script que varre a pasta `dados/` e atualiza o `metadados.json` automaticamente, baseado no nome dos arquivos ou estrutura de pastas.

---

## 🚀 Como executar localmente

```bash
# Crie ambiente virtual e ative (opcional)
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instale dependências
pip install -r requirements.txt

# Execute o backend da assistente
uvicorn assistente.backend.main:app --reload

# Execute (opcional) o painel admin
uvicorn painel_admin.backend.admin_api:app --reload --port 8001
```

---

## 🌐 Deploy sugerido
- Render, Railway ou VPS (ambos sites + API)
- Usar repositório Git com CI/CD opcional
- Armazenar dados localmente ou com sincronização em nuvem

---

## ✨ To-do futuro
- Autenticação no painel admin
- Validação de uploads e arquivos
- Histórico de perguntas do usuário
- Interface responsiva mobile
- Sistema de versionamento dos dados

---

Se você quiser, posso gerar esse esqueleto inicial completo com arquivos e estrutura já prontos para rodar. É só pedir! 🚀
