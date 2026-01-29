const API_BASE_URL = "http://127.0.0.1:8000";

async function ingest() {
    const urlInput = document.getElementById('url');
    const statusText = document.querySelector('#indexStatus .status-text');
    const url = urlInput.value.trim();

    if (!url) return alert("Please enter a URL");

    try {
        // Updated to send JSON body to match the new backend IngestRequest schema
        const response = await fetch(`${API_BASE_URL}/ingest/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url })
        });
        const data = await response.json();
        statusText.innerText = `Success: Indexed ${data.chunks} chunks`;
    } catch (error) {
        statusText.innerText = "Error indexing website";
    }
}

async function ask() {
    const question = document.getElementById('question').value;
    const responseDiv = document.getElementById('response');
    const loader = document.getElementById('loader');

    if (!question) return;

    // UI Feedback
    responseDiv.innerText = "";
    loader.classList.add('active');

    try {
        const response = await fetch(`${API_BASE_URL}/chat/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: question })
        });
        const data = await response.json();
        
        loader.classList.remove('active');
        responseDiv.innerText = data.answer;
    } catch (error) {
        loader.classList.remove('active');
        responseDiv.innerText = "Error: Could not connect to the server.";
    }
}