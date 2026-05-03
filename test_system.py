"""
Quick Test Script for Smart City Assistant
Run this to verify the installation works correctly.
"""

import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_rag_system():
    """Test the RAG pipeline with sample questions."""
    print("\n" + "=" * 70)
    print("🔍 TESTING SMART CITY CITIZEN ASSISTANT")
    print("=" * 70)
    
    try:
        from utils.rag_pipeline import RAGPipeline
        
        # Initialize the system
        print("\n[1/4] Initializing RAG pipeline...")
        rag = RAGPipeline(data_path="data", use_openai=False)
        
        success = rag.initialize()
        
        if not success:
            print("❌ Initialization failed!")
            return False
        
        print("\n[2/4] System initialized successfully!")
        
        # Test questions
        test_questions = [
            "Where can I get my city ID card?",
            "What are the bus fares?",
            "What is the emergency contact number?"
        ]
        
        print("\n[3/4] Testing with sample questions...\n")
        
        for i, question in enumerate(test_questions, 1):
            print(f"{'─' * 70}")
            print(f"Q{i}: {question}")
            print(f"{'─' * 70}")
            
            answer = rag.answer_question(question)
            print(f"A: {answer}\n")
        
        print("\n[4/4] All tests completed!")
        print("\n" + "=" * 70)
        print("✅ TEST SUCCESSFUL")
        print("=" * 70)
        print("\nThe system is ready to use!")
        print("Run 'streamlit run app.py' to start the web interface.")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Smart City Citizen Assistant - Quick Test")
    print("Make sure you're in the project root directory.")
    print("-" * 70)
    
    # Check if data folder exists
    if not os.path.exists("data"):
        print("❌ Error: 'data' folder not found. Please run from project root.")
        sys.exit(1)
    
    # Check data files
    data_files = os.listdir("data")
    if not data_files:
        print("❌ Error: No files in 'data' folder.")
        sys.exit(1)
    
    print(f"Found {len(data_files)} data files: {', '.join(data_files)}")
    print("-" * 70)
    
    success = test_rag_system()
    sys.exit(0 if success else 1)
