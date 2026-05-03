"""
RAG Pipeline for Smart City Citizen Assistant

This module handles the core RAG functionality:
1. Loading documents from the data folder
2. Creating text embeddings
3. Storing embeddings in FAISS vector database
4. Retrieving relevant chunks based on user query
5. Generating answers using LLM
"""

import os
import warnings
warnings.filterwarnings('ignore')

from typing import List
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain.chains import RetrievalQA
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline


class RAGPipeline:
    """Manages the RAG pipeline for document-based question answering."""
    
    def __init__(self, data_path: str = "data", use_openai: bool = False):
        """
        Initialize the RAG pipeline.
        
        Args:
            data_path: Path to the data folder containing text documents
            use_openai: Whether to use OpenAI (True) or HuggingFace (False)
        """
        self.data_path = data_path
        self.use_openai = use_openai
        self.vectorstore = None
        self.qa_chain = None
        
    def load_documents(self) -> List:
        """Load all text documents from the data folder."""
        documents = []
        
        # Check if data folder exists
        if not os.path.exists(self.data_path):
            print(f"Data folder '{self.data_path}' not found!")
            return documents
        
        # Iterate through all files in the data folder
        files = os.listdir(self.data_path)
        if not files:
            print("No files found in data folder.")
            return documents
        
        for filename in files:
            if filename.endswith(".txt") or filename.endswith(".pdf"):
                file_path = os.path.join(self.data_path, filename)
                try:
                    loader = TextLoader(file_path, encoding='utf-8')
                    docs = loader.load()
                    documents.extend(docs)
                    print(f"✓ Loaded: {filename}")
                except Exception as e:
                    # Try with different encoding
                    try:
                        loader = TextLoader(file_path, encoding='latin-1')
                        docs = loader.load()
                        documents.extend(docs)
                        print(f"✓ Loaded: {filename} (with latin-1 encoding)")
                    except Exception as e2:
                        print(f"✗ Could not load {filename}: {e2}")
        
        print(f"\nTotal documents loaded: {len(documents)}")
        return documents
    
    def create_embeddings(self, documents: List):
        """Create text embeddings and store in FAISS vector database."""
        if not documents:
            print("No documents to process.")
            return None
        
        print("\nSplitting documents into text chunks...")
        
        # Split documents into smaller chunks for better retrieval
        text_splitter = CharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separator="\n"
        )
        text_chunks = text_splitter.split_documents(documents)
        print(f"✓ Created {len(text_chunks)} text chunks")
        
        print("\nGenerating embeddings (this may take a moment)...")
        print("Using sentence-transformers/all-MiniLM-L6-v2 model")
        
        # Use HuggingFace embeddings (free and doesn't require API key)
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        print("Building FAISS vector database...")
        
        # Create FAISS vector store
        self.vectorstore = FAISS.from_documents(text_chunks, embeddings)
        print("✓ FAISS database created successfully!")
        
        return self.vectorstore
    
    def setup_qa_chain(self):
        """Set up the question-answering chain with LLM."""
        print("\nSetting up question-answering system...")
        
        llm = None

        if self.use_openai:
            # Use OpenAI if API key is available
            try:
                import openai
                from langchain_openai import OpenAI
                llm = OpenAI(temperature=0.7)
                print("Using OpenAI GPT model")
            except Exception as e:
                print(f"OpenAI not available ({e}), using HuggingFace instead")
                self.use_openai = False
        
        if not self.use_openai:
            # Use HuggingFace local pipeline (works offline, no API key needed)
            try:
                print("Loading local text generation model...")
                print("Model: google/flan-t5-small")
                print("(This may take a moment for first-time download)")
                
                generator = pipeline(
                    'text2text-generation',
                    model='google/flan-t5-small',
                    device=-1,  # Use CPU (-1) or GPU (0)
                    max_length=512,
                    temperature=0.7
                )
                llm = HuggingFacePipeline(pipeline=generator)
                print("✓ Local pipeline loaded successfully")
            except Exception as e:
                print(f"Error loading HuggingFace model: {e}")
                print("Falling back to simple retrieval without LLM")
                llm = None
        
        # Create the QA chain
        if self.vectorstore and llm:
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=self.vectorstore.as_retriever(
                    search_kwargs={"k": 3}  # Retrieve top 3 relevant chunks
                ),
                return_source_documents=True,
                chain_type_kwargs={
                    "verbose": False
                }
            )
            print("✓ QA chain setup complete!")
        elif self.vectorstore and not llm:
            # Fallback: return retrieved documents directly
            self.qa_chain = None
            print("⚠ QA chain setup incomplete, using document retrieval only")
        
        return self.qa_chain
    
    def answer_question(self, question: str) -> str:
        """Answer a question using the RAG pipeline."""
        if not self.vectorstore:
            return "Error: Vector database not initialized. Please run create_embeddings() first."
        
        try:
            if self.qa_chain:
                # Use LLM for answer generation
                result = self.qa_chain({"query": question})
                answer = result.get("result", "I couldn't generate an answer.")
            else:
                # Fallback: retrieve and summarize documents directly
                docs = self.vectorstore.similarity_search(question, k=3)
                if docs:
                    answer = "Based on the following city service information:\n\n"
                    for i, doc in enumerate(docs, 1):
                        # Extract first 500 chars of each document
                        text = doc.page_content[:500]
                        if len(doc.page_content) > 500:
                            text += "..."
                        answer += f"{i}. {text}\n\n"
                    answer += "\nFor more details, please refer to the official city service documents."
                else:
                    answer = "I couldn't find relevant information in the city service documents."
            
            # Extract source documents if available
            if hasattr(self, 'qa_chain') and self.qa_chain:
                result = self.qa_chain({"query": question})
                sources = result.get("source_documents", [])
            else:
                sources = self.vectorstore.similarity_search(question, k=3)
            
            if sources:
                source_texts = []
                for i, doc in enumerate(sources[:3], 1):
                    source_name = doc.metadata.get('source', 'Unknown')
                    # Extract just the filename
                    if '/' in source_name:
                        source_name = source_name.split('/')[-1]
                    source_texts.append(f"{source_name}")
                
                # Add sources to answer for transparency
                answer = f"{answer}\n\n{'─' * 50}\nℹ Based on city records:"
                for source in source_texts:
                    answer = f"{answer}\n  • {source}"
            
            return answer
        except Exception as e:
            return f"Error generating answer: {str(e)}"
    
    def initialize(self):
        """Initialize the complete RAG pipeline."""
        print("=" * 60)
        print("🚀 Initializing Smart City Citizen Assistant RAG System")
        print("=" * 60)
        
        # Load documents
        documents = self.load_documents()
        if not documents:
            print("\n❌ No documents found. Please add text files to the data/ folder.")
            return False
        
        # Create embeddings
        vs = self.create_embeddings(documents)
        if not vs:
            print("\n❌ Failed to create embeddings.")
            return False
        
        # Setup QA chain
        self.setup_qa_chain()
        
        print("\n" + "=" * 60)
        print("✅ RAG System Ready!")
        print("=" * 60)
        print("\nYou can now ask questions about city services.")
        print("Example: 'Where can I get my city ID card?'")
        return True

