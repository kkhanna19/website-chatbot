# Website-Based RAG Chatbot

## 📌 Project Overview

This project implements a **website-based conversational chatbot** using **Retrieval-Augmented Generation (RAG)** technology. The system enables users to provide a website URL, automatically crawls and extracts the content, generates embeddings, stores them in a vector database, and allows users to ask natural language questions that are answered **strictly using the website's content**.

**Key Feature**: If the answer to a question is not available in the indexed website content, the chatbot responds with:
> _"The answer is not available on the provided website."_

This ensures **zero hallucination** and maintains strict grounding to the source material.

---

## 🎯 Core Features

✅ **URL-based Website Indexing** - Accept any website URL and automatically index its content  
✅ **Intelligent Content Extraction** - Crawl and clean website text with advanced preprocessing  
✅ **Semantic Chunking** - Split content into optimized chunks for better retrieval  
✅ **Vector Embeddings** - Generate and persist embeddings using state-of-the-art models  
✅ **Similarity Search** - Fast vector-based retrieval using FAISS  
✅ **LLM-Powered Responses** - Generate accurate answers using Hugging Face Mistral  
✅ **Hallucination Prevention** - Strict prompt guardrails ensure grounded responses  
✅ **Session Memory** - Short-term conversational context for follow-up questions  
✅ **Clean Web UI** - Simple, intuitive interface built with HTML/CSS/JavaScript  

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────┐
│          Frontend (HTML/CSS/JS)                 │
│  • URL Input Interface                          │
│  • Chat Interface                               │
│  • Response Display                             │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│          FastAPI Backend                        │
│  • /ingest - Index website endpoint             │
│  • /chat - Question answering endpoint          │
│  • /health - Service health check               │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│          RAG Pipeline                           │
│                                                 │
│  1. Web Crawler → Extract website content       │
│  2. Text Cleaner → Remove noise, normalize      │
│  3. Chunker → Split into semantic segments      │
│  4. Embeddings → Generate vector representations│
│  5. Vector Store → Persist in FAISS             │
│  6. Retriever → Similarity search               │
│  7. LLM → Generate grounded answer              │
└─────────────────────────────────────────────────┘
```

---

## 🧠 Technology Stack

### Backend
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **API Framework** | FastAPI | RESTful API endpoints |
| **Language** | Python 3.10+ | Core development |
| **RAG Orchestration** | LangChain | RAG pipeline management |
| **Vector Database** | FAISS | Fast similarity search |
| **Embeddings** | SentenceTransformers | Text-to-vector conversion |
| **LLM** | Hugging Face Mistral-7B | Answer generation |
| **Web Scraping** | BeautifulSoup4 / Scrapy | Content extraction |

### Frontend
| Component | Technology |
|-----------|-----------|
| **Markup** | HTML5 |
| **Styling** | CSS3 |
| **Scripting** | Vanilla JavaScript |

---

## 📁 Project Structure

```
website-chatbot/
│
├── backend/
│   ├── app/
│   │   ├── main.py                    # FastAPI application entry point
│   │   │
│   │   ├── api/                       # API layer (routes)
│   │   │   ├── routes/
│   │   │   │   ├── ingest.py         # Website indexing endpoint
│   │   │   │   ├── chat.py           # Q&A endpoint
│   │   │   │   └── health.py         # Health check endpoint
│   │   │
│   │   ├── services/                  # Business logic (RAG components)
│   │   │   ├── crawler.py            # Website content extraction
│   │   │   ├── chunker.py            # Text chunking logic
│   │   │   ├── embeddings.py         # Embedding generation
│   │   │   ├── vectorstore.py        # Vector database operations
│   │   │   ├── retriever.py          # Similarity search
│   │   │   └── llm.py                # LLM integration
│   │   │
│   │   ├── core/                      # Core system configuration
│   │   │   ├── config.py             # Environment configuration
│   │   │   ├── prompt.py             # System prompts
│   │   │   └── memory.py             # Conversation memory
│   │   │
│   │   ├── schemas/                   # Request/Response models
│   │   │   ├── ingest.py             # Ingestion schemas
│   │   │   └── chat.py               # Chat schemas
│   │   │
│   │   └── utils/                     # Helper functions
│   │       ├── validators.py         # Input validation
│   │       └── text_cleaning.py      # Text preprocessing
│   │
│   ├── data/                          # Data storage
│   │   ├── raw/                      # Raw crawled content
│   │   ├── processed/                # Processed chunks
│   │   └── vector_store/             # FAISS index files
│   │
│   ├── requirements.txt               # Python dependencies
│   └── .env.example                   # Environment template
│
├── frontend/
│   ├── index.html                     # Main UI
│   ├── css/
│   │   └── style.css                 # Styling
│   └── js/
│       └── app.js                    # Frontend logic
│
├── README.md                          # This file
└── .gitignore                         # Git ignore rules
```

---

## 🔄 How It Works

### **Phase 1: Website Indexing**

1. **User Input** - User provides a website URL
2. **Crawling** - System crawls the website and extracts text content
3. **Cleaning** - HTML tags, scripts, and noise are removed
4. **Chunking** - Text is split into semantic chunks (300-800 tokens)
5. **Embedding** - Each chunk is converted to a vector using SentenceTransformers
6. **Storage** - Vectors are stored in FAISS for fast retrieval

### **Phase 2: Question Answering**

1. **Question Input** - User asks a natural language question
2. **Question Embedding** - Question is converted to a vector
3. **Retrieval** - Top-K most similar chunks are retrieved via cosine similarity
4. **Context Assembly** - Retrieved chunks are combined as context
5. **LLM Query** - Context + question sent to Mistral-7B with strict prompt
6. **Answer Generation** - LLM generates answer grounded in context
7. **Response** - Answer displayed to user

### **Anti-Hallucination Mechanism**

The system uses a carefully crafted system prompt:

```
You are a helpful assistant that answers questions ONLY based on the provided context.

Rules:
1. Answer ONLY using information from the context below
2. If the answer is not in the context, respond with: "The answer is not available on the provided website."
3. Do NOT use your general knowledge
4. Be concise and accurate

Context:
{retrieved_chunks}

Question:
{user_question}
```

---

## ⚙️ Setup Instructions

### **Prerequisites**
- Python 3.10 or higher
- pip (Python package manager)
- Hugging Face account (for API token)

### **1. Clone the Repository**

```bash
git clone https://github.com/kkhanna19/website-chatbot.git
cd website-chatbot
```

### **2. Backend Setup**

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### **3. Configure Environment**

Create a `.env` file in the `backend` directory:

```env
# Hugging Face API Token
HF_API_TOKEN=your_huggingface_token_here

# Model Configuration
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
LLM_MODEL=mistralai/Mistral-7B-Instruct-v0.2

# Vector Store Configuration
VECTOR_STORE_PATH=./data/vector_store
CHUNK_SIZE=500
CHUNK_OVERLAP=50

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
```

**Get your Hugging Face token**: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### **4. Run the Backend**

```bash
# Make sure you're in the backend directory with venv activated
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### **5. Open Frontend**

Simply open `frontend/index.html` in your web browser, or use a local server:

```bash
# Using Python's built-in server
cd frontend
python -m http.server 3000
```

Then navigate to `http://localhost:3000`

---

## 🧪 Usage Example

### **Step 1: Index a Website**

1. Open the frontend in your browser
2. Enter a website URL (e.g., `https://example.com`)
3. Click **"Index Website"**
4. Wait for the indexing process to complete

### **Step 2: Ask Questions**

1. Type your question in the chat input
2. Press Enter or click Send
3. Receive an answer based on the website content

**Example:**

```
User: "What is the main topic of this website?"
Bot: "This website focuses on providing examples and demonstrations for developers..."

User: "What is the company's phone number?"
Bot: "The answer is not available on the provided website."
```

---

## 🔍 API Endpoints

### **POST `/ingest`**
Index a website

**Request:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Website indexed successfully",
  "chunks_created": 42,
  "url": "https://example.com"
}
```

### **POST `/chat`**
Ask a question

**Request:**
```json
{
  "question": "What is this website about?",
  "session_id": "user-123"
}
```

**Response:**
```json
{
  "answer": "This website is about...",
  "sources": ["chunk_1", "chunk_5"],
  "confidence": 0.89
}
```

### **GET `/health`**
Check service health

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

---

## 🎨 Embedding Strategy

### **Model Choice**
- **Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Dimension**: 384
- **Speed**: Fast inference
- **Quality**: Balanced performance for semantic search

### **Chunking Strategy**
- **Chunk Size**: 500 tokens
- **Overlap**: 50 tokens (for context continuity)
- **Method**: Semantic-aware splitting at sentence boundaries

### **Retrieval**
- **Top-K**: 5 most relevant chunks
- **Similarity Metric**: Cosine similarity
- **Threshold**: 0.7 (configurable)

---

## 🛡️ Security & Best Practices

✅ **No Hardcoded Secrets** - All sensitive data in `.env`  
✅ **Input Validation** - URL and query sanitization  
✅ **Rate Limiting** - Prevents abuse (configurable)  
✅ **CORS Configuration** - Secure cross-origin requests  
✅ **Error Handling** - Graceful failure with informative messages  

---

## ⚠️ Limitations

| Limitation | Description |
|------------|-------------|
| **Crawling Depth** | Currently supports single-page or limited depth crawling |
| **Authentication** | No support for password-protected sites |
| **Dynamic Content** | JavaScript-heavy sites may not be fully indexed |
| **Scale** | Designed as a POC, not optimized for very large websites |
| **Rate Limits** | Subject to Hugging Face API rate limits |

---

## 🚀 Future Enhancements

- [ ] **Multi-site Indexing** - Support multiple websites simultaneously
- [ ] **Advanced Crawling** - Sitemap-based crawling with depth control
- [ ] **Hybrid Search** - Combine BM25 (keyword) + Vector (semantic) search
- [ ] **User Authentication** - Multi-user support with isolated sessions
- [ ] **Docker Support** - Containerization for easy deployment
- [ ] **Evaluation Metrics** - Answer quality tracking and analytics
- [ ] **Streaming Responses** - Real-time answer generation display
- [ ] **Document Upload** - Support PDF, DOCX, TXT file ingestion
- [ ] **Advanced Memory** - Long-term conversation history
- [ ] **Custom Models** - Support for other LLMs (GPT-4, Claude, etc.)

---

## 🐛 Troubleshooting

### **Issue: "ModuleNotFoundError"**
**Solution**: Ensure virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### **Issue: "Hugging Face API Error"**
**Solution**: Verify your API token in `.env` is valid and has proper permissions

### **Issue: "Website Indexing Failed"**
**Solution**: Check if:
- The URL is accessible
- The website doesn't block crawlers
- You have internet connectivity

### **Issue: "CORS Error in Browser"**
**Solution**: Ensure backend CORS settings allow your frontend origin

---

## 📚 Dependencies

### **Core Libraries**
```
fastapi==0.109.0
uvicorn==0.27.0
langchain==0.1.0
sentence-transformers==2.3.1
faiss-cpu==1.7.4
huggingface-hub==0.20.0
beautifulsoup4==4.12.0
requests==2.31.0
pydantic==2.5.0
python-dotenv==1.0.0
```

See `backend/requirements.txt` for the complete list.

---

## 📖 References & Resources

- [LangChain Documentation](https://python.langchain.com/)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [Hugging Face Models](https://huggingface.co/models)
- [Sentence Transformers](https://www.sbert.net/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Karan Khanna** - [GitHub](https://github.com/kkhanna19)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🙏 Acknowledgments

- Hugging Face for providing excellent models and APIs
- LangChain for the RAG framework
- FastAPI for the modern web framework
- The open-source community for various tools and libraries

---

## 📞 Support

For questions or issues, please:
- Open an issue on [GitHub](https://github.com/kkhanna19/website-chatbot/issues)
- Reach out via email or social media

---

**Happy Chatting! 🤖💬**