const textarea = document.getElementById('inputMessage');
const sendBtn = document.getElementById('sendBtn');
const chatContainer = document.getElementById('chatContainer');

function addMessage(text, fromUser = true) {
  const msgDiv = document.createElement('div');
  msgDiv.classList.add('message', fromUser ? 'user' : 'bot');
  msgDiv.textContent = text;
  chatContainer.appendChild(msgDiv);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

async function sendMessage() {
  const msg = textarea.value.trim();
  if (!msg) return;

  addMessage(msg, true);
  textarea.value = '';

  try {
    const response = await fetch('/api/consulta', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ pergunta: msg })
    });
    const data = await response.json();
    addMessage(data.resposta || data.erro || 'Erro desconhecido', false);
  } catch (e) {
    addMessage('Erro ao se comunicar com o servidor.', false);
  }
}

sendBtn.addEventListener('click', sendMessage);
textarea.addEventListener('keydown', e => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});