import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Uttam Tiwari | ML Engineer",
    page_icon="",
    layout="wide"
)


st.sidebar.title("Uttam Tiwari")
st.sidebar.markdown("AI Engineer | ML Engineer | GenAI Developer")

st.sidebar.markdown("### 🔗 Connect")
st.sidebar.markdown("[GitHub](https://github.com/Uttamxalpha)")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/uttam-tiwari)")
st.sidebar.markdown("📧 uttamt2006@gmail.com")


resume_path = Path("assets/resume.pdf")
if resume_path.exists():
    with open(resume_path, "rb") as f:
        st.sidebar.download_button(
            label="📄 Download Resume",
            data=f,
            file_name="Uttam_Tiwari_Resume.pdf",
            mime="application/pdf"
        )

# -----------------------

# -----------------------

col1, col2 = st.columns([2, 1])

with col1:
    st.title("Uttam Tiwari")
    st.subheader("Data scientist | GenAI Developer | AI Systems Builder")

    st.markdown("""
    I build **production-ready AI systems** using LLMs, RAG pipelines, 
    and scalable backend architectures.

    Focused on Retrieval-Augmented Generation, Agentic AI, 
    and intelligent document processing systems.
    """)

   
    st.markdown("""
    **📍 Indore, India**  
    **🎓 B.Tech CS & AI (2023–2027)**  
    ** Specialized in RAG, GenAI & Agentic AI Systems**
    """)

with col2:
    st.image("/Users/uttamtiwari/Desktop/untitled folder 2/project/assets/profile.jpeg", width=250)

# -----------------------
# PROJECTS
# -----------------------
st.header(" Featured Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Enterprise RAG System")
    st.markdown("""
    - Multi-document QA system  
    - Vector search + LLM reasoning  
    - Production-ready pipeline  
    - FastAPI backend  
    """)

    st.markdown("[GitHub Repository](https://github.com/Uttamxalpha)")

    st.subheader("Resume ↔ JD Matching Engine")
    st.markdown("""
    - Semantic similarity scoring  
    - Embeddings-based ranking  
    - Skill gap analysis  
    """)

    st.markdown("[GitHub Repository](https://github.com/Uttamxalpha)")


with col2:
    st.subheader("Agentic AI System (LangGraph)")
    st.markdown("""
    - Multi-step reasoning agents  
    - Tool-calling workflow  
    - State-based execution graph  
    """)

    st.markdown("[GitHub Repository](https://github.com/Uttamxalpha)")

    st.subheader("Generative AI Document Intelligence")
    st.markdown("""
    - Intelligent PDF parsing  
    - Information extraction  
    - LLM-driven summarization  
    """)

    st.markdown("[GitHub Repository](https://github.com/Uttamxalpha)")

st.divider()


# SKILLS

st.header(" Technical Skills")

st.markdown("""
###  Programming
- Python (Advanced)
- SQL 
- Java (Intermediate)

###  Machine Learning & Deep Learning
- Supervised & Unsupervised Learning
- ANN, CNN, RNN, LSTM
- Model Evaluation & Hyperparameter Tuning
- Feature Engineering
- End-to-End ML Pipelines

###  Generative AI & NLP
- Retrieval-Augmented Generation (RAG)
- Advanced RAG (Multi-query, Re-ranking, Hybrid Search)
- Agentic AI Systems (LangGraph)
- Transformers, BERT, LLMs
- Prompt Engineering & Prompt Optimization
- Embeddings (BGE, OpenAI, HuggingFace)
- Semantic Search & Vector Databases (FAISS, ChromaDB)

### Backend & Deployment
- FastAPI (REST APIs for AI systems)
- Streamlit (AI App Development)
- Docker (Containerization)
- API Integration & Model Deployment

### Data & Analytics
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Pandas, NumPy, Matplotlib
- Business Insight Extraction

###  Tools & Ecosystem
- Hugging Face
- Git & GitHub
- LangChain
- LangGraph
- OpenCV
- Scikit-learn
""")
st.divider()


st.header("💼 Experience")

st.markdown("""
**Machine Learning Intern — Robotronix Tech Pvt. Ltd. (Indore)**  
- Built ML models for classification tasks  
- Data preprocessing and model evaluation  
- Worked on real-world datasets  
""")

st.divider()


st.header("Ask My Portfolio (Demo)")

question = st.text_input("Ask something about my projects or skills")

if question:
    st.info("This is a demo response. ")
    st.write("In production, this section can connect to our FastAPI RAG backend.")