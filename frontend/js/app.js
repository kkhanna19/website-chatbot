const API_BASE_URL = "http://127.0.0.1:8000";
let currentSessionId = "session-" + Math.random().toString(36).substring(7);
let activeWebsite = "Unknown"; // Tracks the website for this session

// Audit Log to store conversation for traceability and auditability
let conversationAuditLog = {
    sessionId: currentSessionId,
    website: "",
    startTime: new Date().toISOString(),
    interactions: []
};

async function ingest() {
    const urlInput = document.getElementById('url');
    const indexBtn = document.getElementById('indexBtn');
    const statusBox = document.getElementById('indexStatus');
    const statusText = statusBox.querySelector('.status-text');
    const url = urlInput.value.trim();

    if (!url) return alert("Please enter a URL");

    statusBox.classList.add('active');
    statusText.innerText = "Searching the website...";
    indexBtn.disabled = true;

    try {
        const response = await fetch(`${API_BASE_URL}/ingest/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url })
        });
        const data = await response.json();
        
        // Update Audit Log Meta
        activeWebsite = url;
        conversationAuditLog.website = url;

        // UI: Lock the field
        statusText.innerText = `Success: Indexed ${data.chunks} chunks.`;
        urlInput.disabled = true;
        urlInput.style.opacity = "0.5";
        indexBtn.innerHTML = "Locked";
    } catch (error) {
        statusText.innerText = "Error indexing website";
        indexBtn.disabled = false;
    }
}

async function ask() {
    const questionInput = document.getElementById('question');
    const loader = document.getElementById('loader');
    const question = questionInput.value.trim();

    if (!question) return;

    appendMessage('user', question);
    questionInput.value = "";
    loader.classList.add('active');

    try {
        const response = await fetch(`${API_BASE_URL}/chat/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                question: question,
                session_id: currentSessionId 
            })
        });
        
        const data = await response.json();
        loader.classList.remove('active');

        // Audit Logging for Traceability
        const auditEntry = {
            timestamp: new Date().toISOString(),
            query: question,
            response: data.answer,
            retrievedSources: data.sources // Traceability: what data was used?
        };
        conversationAuditLog.interactions.push(auditEntry);

        appendMessage('ai', data.answer, data.sources);
        
    } catch (error) {
        loader.classList.remove('active');
        appendMessage('ai', "Error: Could not connect to the server.");
    }
}

// Function to export logs for auditability
function downloadAuditLog() {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(conversationAuditLog, null, 2));
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    downloadAnchorNode.setAttribute("download", `audit_log_${activeWebsite.replace(/[^a-z0-9]/gi, '_')}.json`);
    document.body.appendChild(downloadAnchorNode);
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
}

function appendMessage(sender, text, sources = []) {
    const chatFeed = document.getElementById('chat-feed');
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', sender);
    
    if (sender === 'user') {
        msgDiv.innerHTML = `<strong>You:</strong><br>${text}`;
    } else {
        const formattedText = marked.parse(text);
        let sourceHtml = sources.map((s, i) => 
            `<span class="source-tag">[Source ${i+1}: ${s.substring(0, 50)}...]</span>`
        ).join("");
        msgDiv.innerHTML = `<strong>Bot:</strong><div>${formattedText}</div>${sourceHtml}`;
    }

    chatFeed.appendChild(msgDiv);
    chatFeed.scrollTop = chatFeed.scrollHeight;
}