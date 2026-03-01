import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Uttam Tiwari | ML Engineer",
    page_icon="🚀",
    layout="wide"
)

st.sidebar.title("Uttam Tiwari")
st.sidebar.markdown("ML Engineer | GenAI Developer | AI Systems Builder")
st.sidebar.markdown("[GitHub](https://github.com/Uttamxalpha)")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/uttam-tiwari)")
st.sidebar.markdown("uttamt2006@gmail.com")

resume_path = Path("assets/resume.pdf")
if resume_path.exists():
    with open(resume_path, "rb") as f:
        st.sidebar.download_button(
            label="Download Resume",
            data=f,
            file_name="Uttam_Tiwari_Resume.pdf",
            mime="application/pdf"
        )

col1, col2 = st.columns([2, 1])

with col1:
    st.title("Uttam Tiwari")
    st.subheader("ML Engineer | GenAI Developer | AI Systems Builder")

    st.markdown("""
I build production-ready AI systems using LLMs, RAG pipelines, and scalable backend architectures.

Focused on Retrieval-Augmented Generation, Agentic AI, and intelligent document processing systems.
""")

    st.markdown("""
Indore, India  
B.Tech CS & AI (2023–2027)  
Specialized in RAG, GenAI & Agentic AI Systems
""")

with col2:
    image_path = Path("assets/profile.jpeg")
    if image_path.exists():
        st.image(image_path, width=250)

st.divider()

st.header("Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Enterprise RAG System")
    st.markdown("""
- Multi-document QA system  
- Vector search + LLM reasoning  
- FastAPI backend  
""")

    st.subheader("Resume ↔ JD Matching Engine")
    st.markdown("""
- Semantic similarity scoring  
- Embeddings-based ranking  
- Skill gap analysis  
""")

with col2:
    st.subheader("Agentic AI System (LangGraph)")
    st.markdown("""
- Multi-step reasoning agents  
- Tool-calling workflow  
- State-based execution graph  
""")

    st.subheader("Generative AI Document Intelligence")
    st.markdown("""
- Intelligent PDF parsing  
- LLM-driven summarization  
""")

st.divider()

st.header("Technical Skills")

st.markdown("""
Programming: Python, SQL, Java  

Machine Learning: ANN, CNN, RNN, LSTM, Model Evaluation, Feature Engineering  

Generative AI: RAG, Advanced RAG, LangGraph, Transformers, BERT, Embeddings, FAISS, ChromaDB  

Backend & Deployment: FastAPI, Streamlit, Docker  

Data: Pandas, NumPy, Matplotlib, Scikit-learn
""")

st.divider()

st.header("Experience")

st.markdown("""
Machine Learning Intern — Robotronix Tech Pvt. Ltd., Indore  
Worked on real-world ML models, preprocessing pipelines, and evaluation workflows.
""")