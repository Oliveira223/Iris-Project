# Projeto Iris - Assistente Jurídico com Memória Temporária

Este projeto é um assistente jurídico baseado em IA, construído com **FastAPI** no backend e um site simples com HTML/CSS/JS no frontend. A IA responde com base no modelo da **OpenAI** e agora tem suporte a **memória temporária** de conversa, igual ao ChatGPT.

> A memória dura apenas enquanto o usuário mantém o site aberto. Se atualizar (F5), a conversa reinicia.

---

## 🔧 Estrutura de arquivos e explicações detalhadas

```
IRIS_PROJECT/
├── .env                          # Chave da API da OpenAI
├── assistente/
│   ├── backend/
│   │   ├── main.py               # Backend FastAPI que recebe e responde perguntas
│   │   └── documentos.py         # Lê os arquivos da pasta 'dados/' para gerar contexto
│   └── public/
│       ├── index.html            # Interface do chat
│       ├── app.js                # Lógica do chat com memória temporária
│       └── style.css             # Estilos visuais do chat
├── dados/                        # Pasta onde ficam os arquivos de referência (.pdf, .txt)
│   └── exemplo.txt / guia.pdf
```

---

### 📄 `.env`

Contém a chave da API da OpenAI:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```
Essa chave é usada para autenticar chamadas à IA.

---

### 📄 `main.py`

Arquivo principal do backend (FastAPI). Ele:
- Expõe a rota `/api/consulta` que recebe perguntas do frontend
- Recebe uma lista de mensagens (`messages[]`) simulando uma conversa
- Chama a OpenAI com esse histórico e retorna a resposta
- Serve o site (HTML/CSS/JS) via `StaticFiles`

**Exemplo de mensagens enviadas:**
```json
[
  { "role": "system", "content": "Você é um assistente jurídico..." },
  { "role": "user", "content": "Oi!" },
  { "role": "assistant", "content": "Olá! Como posso ajudar?" },
  { "role": "user", "content": "Qual o prazo para registro de nascimento?" }
]
```

---

### 📄 `documentos.py`

Arquivo que lê automaticamente todos os documentos da pasta `dados/`, incluindo:
- `.pdf` (usando PyMuPDF)
- `.txt`

Ele retorna um texto longo com o conteúdo desses arquivos. Esse texto pode ser usado para alimentar o prompt da IA futuramente.

---

### 📄 `index.html`

Interface básica do chat:
- Uma caixa de entrada (textarea)
- Botão para enviar a mensagem
- Área de exibição das mensagens do usuário e da IA

---

### 📄 `app.js`

Contém toda a lógica do chat no navegador:
- Armazena um array chamado `chatHistory` com todas as mensagens
- A cada envio, envia **todo o histórico** para o backend
- Adiciona a resposta da IA ao histórico para manter a conversa
- Se o site for recarregado, esse histórico se perde (memória temporária)

---

### 📄 `style.css`

Define a aparência do chat:
- Fundo escuro (modo noturno)
- Diferencia mensagem do usuário e da IA por cor e alinhamento
- Estiliza textarea, botão e espaçamento

---

### 📄 Pasta `dados/`

Contém arquivos usados como base para as respostas do assistente.
- Ex: `guia_cartorio.pdf`, `documentos_exigidos.txt`
- Esses arquivos são lidos automaticamente (via `documentos.py`)

---

## 🌐 Como rodar

1. Instale as dependências:
```bash
pip install fastapi uvicorn openai python-dotenv PyMuPDF
```

2. Rode o backend:
```bash
uvicorn assistente.backend.main:app --reload
```

3. Acesse o site:
```
http://localhost:8000
```

---

Se quiser, você pode evoluir para:

- **Memória persistente por usuário** (em banco de dados)
- **Busca inteligente nos arquivos com embeddings (RAG)**
- **Painel administrativo para gerenciar os dados**

> Para isso, continue usando o `documentos.py` e ampliando o fluxo no `main.py`.

