const API_BASE_URL = "http://127.0.0.1:8000";

async function ingest() {
    const url = document.getElementById('url').value;
    const response = await fetch(`${API_BASE_URL}/ingest/?url=${encodeURIComponent(url)}`, {
        method: 'POST'
    });
    const data = await response.json();
    alert(data.message || "Indexing complete");
}

async function ask() {
    const question = document.getElementById('question').value;
    const response = await fetch(`${API_BASE_URL}/chat/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: question })
    });
    const data = await response.json();
    document.getElementById('response').innerText = data.answer;
}