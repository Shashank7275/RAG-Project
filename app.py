import streamlit as st
import oss

from dotenv import load_doten

# LangChain imports
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# ---------------- UI CONFIG ----------------
st.set_page_config(page_title="RAG PDF Chatbot", layout="wide")
st.title("📚 RAG PDF Chatbot (Mistral + Chroma)")

# ---------------- SESSION STATE ----------------
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# ---------------- EMBEDDING ----------------
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# ---------------- LLM ----------------
llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.3
)

# ---------------- PROMPT ----------------
prompt = ChatPromptTemplate.from_messages([
    ("system",
     """You are a helpful AI assistant.
Use ONLY the provided context to answer the question.
If the answer is not present in the context,
say: "I could not find the answer in the document."
"""),
    ("human",
     """Context:
{context}

Question:
{question}
""")
])

# ---------------- FILE UPLOAD ----------------
st.sidebar.header("📄 Upload PDF")

uploaded_file = st.sidebar.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.sidebar.success("✅ PDF uploaded!")

    # Load PDF
    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()

    # Split
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(docs)

    # Create vector DB
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma-db"
    )

    vectorstore.persist()

    # Save in session
    st.session_state.vectorstore = vectorstore

    st.sidebar.success("✅ Embeddings created & stored!")

# ---------------- CHAT ----------------
st.subheader("💬 Ask Questions")

query = st.text_input("Enter your question:")

if query:
    if st.session_state.vectorstore is None:
        st.warning("⚠️ Please upload a PDF first.")
    else:
        retriever = st.session_state.vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 4,
                "fetch_k": 10,
                "lambda_mult": 0.5
            }
        )

        # Retrieve docs
        docs = retriever.invoke(query)

        # Combine context
        context = "\n".join([doc.page_content for doc in docs])

        # Prompt
        final_prompt = prompt.invoke({
            "context": context,
            "question": query
        })

        # LLM response
        response = llm.invoke(final_prompt)

        st.markdown("### 🤖 Answer")
        st.write(response.content)
