from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# ✅ Embedding model
embedding_function = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# ✅ Load existing vector DB
vectorstore = Chroma(
    embedding_function=embedding_function,
    persist_directory="chroma-db"
)

# ✅ Retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)

# ✅ LLM (Mistral)
llm = ChatMistralAI(
    model="mistral-small-latest",   # updated model name
    temperature=0.3
)

# ✅ Prompt Template (FIXED)
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

print("✅ RAG system fully working")
print("Press 0 to exit")

# ✅ Chat loop
while True:
    query = input("\nYou: ")

    if query == "0":
        break

    # Retrieve docs
    docs = retriever.invoke(query)

    # Combine context
    context = "\n".join([doc.page_content for doc in docs])

    # Create prompt
    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    # Get response
    response = llm.invoke(final_prompt)

    print(f"\nAI: {response.content}")
