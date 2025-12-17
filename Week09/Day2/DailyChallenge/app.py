import os
from dotenv import load_dotenv
import streamlit as st

# Load .env if present
load_dotenv()

# Read keys (these may be empty in the example)
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')

# LangSmith / LangChain tracing flags
if os.getenv('LANGCHAIN_TRACING_V2'):
    os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGCHAIN_TRACING_V2')
if os.getenv('LANGCHAIN_ENDPOINT'):
    os.environ['LANGCHAIN_ENDPOINT'] = os.getenv('LANGCHAIN_ENDPOINT')

st.title('Agentic RAG — Demo App')
st.write('A minimal Streamlit scaffold that loads keys and returns a simulated response.')

prompt = st.text_area('Enter your question', height=120)

if st.button('Submit'):
    if not prompt.strip():
        st.warning('Please enter a question.')
    else:
        st.info('Running (simulated) agent...')
        # Try to load the notebook as text for inspection
        nb_text = None
        try:
            with open('agentic_rag.ipynb', 'r', encoding='utf-8') as f:
                nb_text = f.read()
        except Exception as e:
            nb_text = None
        
        # Simulated response: echo with basic attribution and which keys are present
        sources = []
        if nb_text:
            sources.append('local:notebook')
        if GROQ_API_KEY:
            sources.append('groq')
        if TAVILY_API_KEY:
            sources.append('tavily')
        if GOOGLE_API_KEY:
            sources.append('google')

        simulated_answer = f"Simulated answer for: {prompt[:200]}"
        st.subheader('Answer')
        st.write(simulated_answer)

        st.subheader('Debug')
        st.write({'keys_present': {k: bool(os.getenv(k)) for k in ['GROQ_API_KEY','TAVILY_API_KEY','GOOGLE_API_KEY','LANGCHAIN_API_KEY']},
                 'notebook_loaded': bool(nb_text),
                 'sources': sources})

        if nb_text:
            st.subheader('Preview of agentic_rag.ipynb (first 1000 chars)')
            st.code(nb_text[:1000])
