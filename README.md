# RAG-Project
# 📄 RAG PDF Summarizer (Streamlit App)

A simple and powerful **RAG (Retrieval-Augmented Generation)** project that allows users to:

* Upload a PDF 📄
* Extract and embed content
* Store it in a vector database
* Ask questions or generate summaries using an LLM 🤖

---

## 🚀 Features

* 📂 Upload any PDF file
* 🔍 Semantic search using embeddings
* 🧠 Context-aware answers using RAG
* ✨ Text summarization
* ⚡ Fast and interactive UI with Streamlit
* 💾 Persistent vector database using Chroma

---

## 🧠 Tech Stack

* **Frontend:** Streamlit
* **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
* **Vector DB:** Chroma
* **LLM:** Mistral (via API or local)
* **Framework:** LangChain

---

## 📁 Project Structure

```
RAG-PDF-Summarizer/
│
├── app.py                # Streamlit UI
├── main.py               # Core RAG logic
├── requirements.txt      # Dependencies
├── .env                  # API keys (not pushed to GitHub)
├── chroma_db/            # Vector database
└── README.md             # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/rag-pdf-summarizer.git
cd rag-pdf-summarizer
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key_here
```

⚠️ **Important:** Never push `.env` to GitHub.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🧩 How It Works

1. User uploads a PDF
2. Text is extracted and split into chunks
3. Chunks are converted into embeddings
4. Stored in Chroma vector database
5. User asks a question or requests summary
6. Relevant chunks are retrieved
7. LLM generates context-aware response

---

## 🧪 Example Use Cases

* 📚 Study notes summarization
* 📄 Research paper understanding
* 🏢 Document analysis
* 🧾 Legal or business document Q&A

---

## 🔐 API Key Security (Important)

* Use `.env` file for secrets
* Add `.env` to `.gitignore`

Example `.gitignore`:

```
.env
chroma_db/
__pycache__/
```

---

## 🌍 Deployment

### Option 1: Streamlit Cloud

1. Push code to GitHub
2. Go to Streamlit Cloud
3. Connect your repo
4. Add environment variables

---

### Option 2: Render

* Use `web service`
* Add start command:

```bash
streamlit run app.py --server.port 10000 --server.address 0.0.0.0
```

---

## ⚠️ Known Issues

* Large PDFs may take time to process
* API limits depending on LLM provider
* First load may be slow (embedding generation)

---

## 🔮 Future Improvements

* Chat history memory
* Multi-PDF support
* Better UI/UX
* Local LLM support (offline mode)
* Advanced summarization modes

---

## 🤝 Contributing

Pull requests are welcome!
Feel free to fork this repo and improve it 🚀

---



## 🙌 Acknowledgements

* LangChain
* HuggingFace
* ChromaDB
* Streamlit

---

## 💡 Author

**Shashank Singh**



⭐ If you like this project, don’t forget to star the repo!

