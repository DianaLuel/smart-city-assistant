"""
Smart City Citizen Assistant - Main Application

A RAG-based chatbot for answering citizen questions about city services.

Equipped to answer questions coming from the citizens correctly.
"""

import os
import sys
import streamlit as st

# Add utils to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.rag_pipeline import RAGPipeline

# Page configuration
st.set_page_config(
    page_title="Smart City Citizen Assistant",
    page_icon="🏙️",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stApp {
        background-color: #f0f2f6;
    }
    .chat-container {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .user-message {
        background-color: #0066cc;
        color: white;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 0;
        display: inline-block;
        max-width: 80%;
    }
    .bot-message {
        background-color: #e8e8e8;
        color: #333;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 0;
        display: inline-block;
        max-width: 80%;
        white-space: pre-wrap;
    }
    .stTitle {
        color: #0066cc;
    }
    .header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'rag_system' not in st.session_state:
    st.session_state.rag_system = None

if 'system_initialized' not in st.session_state:
    st.session_state.system_initialized = False

# Header
st.markdown("""
    <div class="header">
        <h1>🏙️ Smart City Citizen Assistant</h1>
        <p>Your AI-powered guide to city services and information</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar for system status and examples
with st.sidebar:
    st.header("🤖 System Status")
    
    if st.session_state.system_initialized:
        st.success("RAG System Active")
        st.info("Ready to answer your questions!")
    else:
        st.warning("Initializing system...")
    
    st.markdown("---")
    
    st.header("📚 Quick Questions")
    example_questions = [
        "Where can I get my city ID card?",
        "What are the bus fares?",
        "What hospital services are available?",
        "What is the emergency number?",
        "How do I apply for a passport?"
    ]
    
    for question in example_questions:
        if st.button(question, key=question):
            st.session_state.messages.append({"role": "user", "content": question})
            st.rerun()
    
    st.markdown("---")
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Main chat area
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Chat container
    chat_container = st.container()
    
    with chat_container:
        # Display chat history
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"""
                    <div style="text-align: right; margin: 10px 0;">
                        <div class="user-message">
                            {message['content']}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style="text-align: left; margin: 10px 0;">
                        <div class="bot-message">
                            🤖 {message['content']}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        
        # Initialize RAG system on first run
        if not st.session_state.system_initialized:
            with st.spinner("Loading city service documents and initializing AI system..."):
                try:
                    rag_system = RAGPipeline(data_path="data", use_openai=False)
                    success = rag_system.initialize()
                    
                    if success:
                        st.session_state.rag_system = rag_system
                        st.session_state.system_initialized = True
                        
                        # Add welcome message
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": "Hello! I'm your Smart City Assistant. I've loaded all city service documents and I'm ready to help you with questions about hospitals, transportation, ID cards, emergency services, and more. How can I help you today?"
                        })
                        st.rerun()
                    else:
                        st.error("Could not load documents. Please check the data folder.")
                except Exception as e:
                    st.error(f"Error initializing RAG system: {str(e)}")
                    st.info("Please ensure all required packages are installed.")

# Chat input
with col2:
    st.markdown("---")
    
    user_input = st.chat_input("Type your question about city services here...")
    
    if user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get and display response
        with st.spinner("Analyzing city documents and generating response..."):
            if st.session_state.rag_system:
                response = st.session_state.rag_system.answer_question(user_input)
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })
                
                st.rerun()
            else:
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "Error: RAG system not initialized. Please refresh the page."
                })
                st.rerun()

# Footer
with col2:
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666; font-size: 0.9em;'>" +
        "⚡ Powered by RAG Technology | Built with LangChain & Streamlit" +
        "</div>",
        unsafe_allow_html=True
    )
