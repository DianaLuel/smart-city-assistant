# Smart City Citizen Assistant

A production-ready RAG-based Intelligent Citizen Assistance System for Smart City Digital Services 🏙️

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-green)](https://langchain.com)

## 📋 Overview

This is a complete, beginner-friendly chatbot system that allows citizens to ask questions about city services (hospitals, transportation, ID cards, emergency services) and receive accurate answers based **ONLY** on official city documents using Retrieval-Augmented Generation (RAG).

## 🎯 Key Features,

✅ **RAG-Based Architecture** - Answers generated from official documents only  
✅ **User-Friendly Web Interface** - Built with Streamlit  
✅ **No API Keys Required** - Uses free local models  
✅ **Fast Setup** - Runs in less than 15 minutes  
✅ **Transparent** - Shows which documents were used for each answer  
✅ **Extensible** - Easy to add new documents  
✅ **Privacy-Friendly** - All processing happens locally  

## 🔍 How RAG Works (In Simple Words)

**RAG = Retrieval-Augmented Generation**

Think of it as a smart assistant that:
1. **Reads** all city service documents
2. **Understands** their content using AI embeddings
3. **Remembers** where each piece of information is stored
4. **Finds** the most relevant information when you ask a question
5. **Reads** only that relevant information
6. **Generates** a clear, accurate answer

**Why this is better:**
- ✨ No hallucinations - answers come from real documents
- 📚 Always up-to-date - just update the documents
- 🔍 Transparent - see which document provided the answer
- ⚡ Fast - instant retrieval from thousands of documents

## 📁 Project Structure

```
smart-city-assistant/
├── app.py                  # Main Streamlit application
├── test_system.py          # CLI testing script
├── verify_installation.py  # Installation checker
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── SETUP_GUIDE.md         # Detailed setup instructions
├── .env.example           # Environment config template
│
├── /data                   # City service documents
│   ├── hospital_services.txt      # Hospital info
│   ├── transport_system.txt       # Public transport info
│   ├── id_card_services.txt       # ID/passport services
│   └── emergency_contacts.txt     # Emergency contacts
│
└── /utils                  # RAG pipeline code
    └── rag_pipeline.py     # Core RAG functionality
```

## 🚀 Quick Start (Under 15 Minutes)

### Prerequisites
- Python 3.8 or higher
- About 2GB free disk space
- Internet connection (for first-time setup)

### Installation Steps

#### 1. Open Terminal/Command Prompt

Navigate to where you want to install the project:

```bash
cd Desktop  # or your preferred location
```

#### 2. Clone or Download the Project

If using Git:
```bash
git clone https://github.com/DianaLuel/smart-city-assistant.git
cd smart-city-assistant
```

Or just download and extract the files to a folder.

#### 3. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

#### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

This downloads ~500MB of packages. Takes 5-10 minutes.

#### 5. Run the Application

```bash
streamlit run app.py
```

The app opens automatically at http://localhost:8501

If it doesn't open, copy and paste that URL into your browser.

## 🧪 Testing the System

### First Launch

1. Open http://localhost:8501 in your browser
2. Wait for "RAG System Ready!" message (1-2 minutes first time)
3. Start chatting!

### Test Questions

Try these in the chat box:

1. **"Where can I get my city ID card?"**
   - Returns all City Clerk Office locations

2. **"What are the bus fares?"**
   - Shows bus ticket prices and passes

3. **"What hospital services are available?"**
   - Lists hospitals, urgent care, and specialized services

4. **"What is the emergency number?"**
   - Shows 911 and other emergency contacts

5. **"How do I apply for a passport?"**
   - Explains passport application process

### Quick CLI Test (Optional)

```bash
python test_system.py
```

Tests the RAG system from command line.

### Verify Installation

```bash
python verify_installation.py
```

Checks all files and dependencies.

## 📝 Sample Documents Included

### 1. Hospital Services
- General hospitals with 24/7 emergency care
- Urgent care centers for non-life-threatening issues
- Specialized services (cardiology, pediatrics, mental health)
- Appointment booking info
- Insurance and cost details

### 2. Transportation System
- 25 bus routes citywide
- Metro/Light Rail 3 lines
- Fare information ($2.50 single ride, $85 monthly pass)
- Operating hours (5 AM - 1 AM)
- Bike sharing program
- Parking information

### 3. ID Card & Passport Services
- City ID card application process
- 3 office locations with hours
- Passport application and fees
- Required documents list
- Processing times

### 4. Emergency Contacts
- 911 for life-threatening emergencies
- Non-emergency police, fire numbers
- Poison control, mental health hotline
- Natural disaster contacts
- Utility emergency numbers
- Community support services

## 💻 Example Questions & Answers

### Hospital Services

**Q:** "Where can I get medical care for a non-emergency?"

**A:** Based on city records:
• Visit Downtown Urgent Care at 789 Central Plaza (8 AM - 10 PM)
• North District Clinic at 321 North Road (7 AM - 9 PM)
• Both offer walk-in appointments for minor injuries and illnesses

### Transportation

**Q:** "How much does it cost to ride the bus?"

**A:** Based on city records:
• Single ride: $2.50
• Day pass (unlimited rides): $7.00
• Monthly pass: $85.00
• Students/seniors: 50% discount with valid ID
• Children under 12: Free with adult

### ID Cards

**Q:** "Where can I renew my city ID card?"

**A:** Based on city records:
• Main Office: 100 City Hall Plaza, (555) 100-0100 (Mon-Fri 8 AM - 6 PM, Sat 9 AM - 2 PM)
• North Branch: 555 North Plaza, (555) 200-0200 (Mon-Fri 9 AM - 5 PM)
• South Branch: 777 South Street, (555) 300-0300 (Tue-Sat 10 AM - 4 PM)

### Emergency

**Q:** "What should I do in a medical emergency?"

**A:** Based on city records:
• Call 911 immediately for life-threatening emergencies
• This connects you to police, fire, and ambulance services
• Stay on the line until told to hang up
• For non-emergency medical issues, call (555) 555-0160 Nurse Advice Line

### Passports

**Q:** "Can I get a passport at the city clerk office?"

**A:** Based on city records:
• Yes, the City Clerk's Office is a full-service passport agency
• Appointment required (call or book online at www.city.gov/book)
• Walk-ins accepted Wednesdays 1:00 PM - 4:00 PM
• Fees: $130 adult passport book, $30 passport card
• Processing time: 6-8 weeks standard, 2-3 weeks expedited (+$60)

## ⚙️ Technical Details

### Technology Stack

- **Python 3.8+**: Programming language
- **Streamlit 1.28+**: Web interface framework
- **LangChain 0.1+**: RAG pipeline orchestration
- **FAISS 1.7.4**: Vector similarity search
- **Sentence-Transformers 2.2.0**: Text embeddings
  - Model: `all-MiniLM-L6-v2` (22.8M parameters, 384-dim embeddings)
- **Transformers 4.30.0**: HuggingFace model integration
- **PyTorch 2.0.0**: Deep learning backend
- **HuggingFace Pipeline**: Local LLM execution
  - Model: `google/flan-t5-small` (instruction-following)

### Architecture

```
User Question
      ↓
[Streamlit UI]
      ↓
[RAG Pipeline]
      ├─ Document Loading → /data/*.txt files
      ├─ Text Splitting → 500-char chunks
      ├─ Embedding Generation → Sentence-Transformers
      ├─ Vector Search → FAISS (top 3 chunks)
      └─ Answer Generation → HuggingFace LLM
      ↓
Formatted Answer + Sources
      ↓
[Streamlit UI]
      ↓
User
```

### Data Flow

1. **Loading Phase** (once at startup):
   - Read all `.txt` files from `/data`
   - Split into 500-character chunks
   - Generate embeddings using sentence-transformers
   - Build FAISS vector index
   - Load HuggingFace LLM (flan-t5-small)

2. **Query Phase** (for each question):
   - Convert question to embedding
   - Search FAISS for top 3 similar chunks
   - Pass context + question to LLM
   - Return formatted answer
   - Display source documents

## 📊 Performance

| Metric | Value |
|--------|-------|
| First run time | 2-3 minutes (model downloads) |
| Subsequent starts | 30-60 seconds |
| Query response | 2-5 seconds |
| Memory usage | ~2 GB RAM |
| Disk space | ~1 GB (including models) |
| CPU usage | Moderate (single core) |

## 🔧 Configuration

### Using OpenAI (Optional)

1. Get API key from [OpenAI Platform](https://platform.openai.com/)
2. Edit `.env` file:
   ```
   USE_OPENAI=true
   OPENAI_API_KEY=your-key-here
   ```
3. Restart the app

### Adding New Documents

1. Create `.txt` or `.pdf` file in `/data` folder
2. Restart the application
3. System auto-loads new documents

### Changing Models

Edit `utils/rag_pipeline.py`:
- Line ~53: Change `model_name` in `HuggingFaceEmbeddings()`
- Line ~111: Change `model` in `pipeline()`

## 🌟 Use Cases

1. **City Website**: Embed as citizen help widget
2. **Mobile App**: On-the-go service information
3. **Kiosks**: Self-service information stations
4. **Call Centers**: Quick lookup for operators
5. **Community Centers**: Digital help desk

## 🛠️ Troubleshooting

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "CUDA out of memory"
The app uses CPU by default. If you see this error, restart and ensure no GPU is being used.

### "Could not load documents"
- Check `/data` folder exists
- Verify `.txt` files are present
- Check file permissions

### "Port 8501 already in use"
```bash
streamlit run app.py --server.port 8502
```

### Very slow first run
Normal - models download once (~500MB). Subsequent runs are fast.

### Out of RAM
- Close other applications
- Use a machine with 4GB+ RAM
- Reduce chunk_size in rag_pipeline.py (line 61)

## 🔐 Security & Privacy

- ✅ All processing happens locally
- ✅ No data sent to external servers
- ✅ No user tracking or logging
- ✅ Safe for sensitive information
- ✅ Works offline after setup
- ✅ No API keys required (by default)

## 📝 License & Attribution

This is a demonstration project for educational purposes.

Models used (under their respective licenses):
- Sentence-Transformers: Apache 2.0
- FLAN-T5: Apache 2.0
- FAISS: MIT License

## 🤝 Contributing

To add new features:
1. Add new document types to `/data`
2. Modify `rag_pipeline.py` for custom logic
3. Update `app.py` for UI changes
4. Test with `test_system.py`

## 📚 Learn More

- [Streamlit Documentation](https://docs.streamlit.io)
- [LangChain Documentation](https://python.langchain.com)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [Sentence-Transformers Documentation](https://www.sbert.net)
- [RAG Explained](https://python.langchain.com/v0.1/docs/expression_language/how_to/rag)

## 🆘 Support

For issues:
1. Check SETUP_GUIDE.md for detailed instructions
2. Run `python verify_installation.py`
3. Review error messages
4. Check all files are in correct locations

## 🎉  Success Criteria

You know it's working when:
- ✅ App opens in browser at localhost:8501
- ✅ "RAG System Ready!" message appears
- ✅ You can ask questions
- ✅ Answers reference document sources
- ✅ Response time is 2-5 seconds

---

**Built with ❤️ for Smart Cities**  
*Privacy-First • Local AI • Open Source*   
