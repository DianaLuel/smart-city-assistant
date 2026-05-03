# Setup Instructions Guide

## Quick Setup (Estimated Time: 10-15 minutes)

### Step 1: Python Installation Check

Make sure Python is installed:

```bash
python --version
# or
python3 --version
```

You need Python 3.8 or higher.

### Step 2: Navigate to Project Directory

```bash
cd path/to/smart-city-assistant
```

### Step 3: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv

# Activate it
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` before your command prompt.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will download and install:
- Streamlit (web framework)
- LangChain (RAG framework)
- FAISS (vector database)
- Sentence-Transformers (embeddings)
- Transformers (HuggingFace models)
- PyTorch (deep learning framework)

**Note**: This may take 5-10 minutes and requires ~1GB disk space.

### Step 5: Run the Application

```bash
streamlit run app.py
```

The app will open in your browser automatically at `http://localhost:8501`

If it doesn't open automatically, copy and paste the URL into your browser.

## Troubleshooting Common Issues

### Issue: "ModuleNotFoundError: No module named 'langchain'"

**Solution**: Make sure you activated the virtual environment and ran `pip install -r requirements.txt`

### Issue: "CUDA out of memory" or GPU errors

**Solution**: The code uses CPU by default. If you have CUDA installed and it's causing issues, make sure the `device=-1` parameter is set in the pipeline (it is).

### Issue: "Could not load documents"

**Solution**: 
1. Check that the `data/` folder exists in the same directory as `app.py`
2. Make sure there are `.txt` files in the `data/` folder
3. Check file permissions

### Issue: "Port 8501 already in use"

**Solution**: 
```bash
streamlit run app.py --server.port 8502
```

### Issue: Very slow on first run

**Solution**: This is normal. The first run downloads pretrained models (~500MB). Subsequent runs will be much faster as models are cached.

## Testing Without Streamlit (CLI Testing)

You can test the RAG system directly:

```bash
python test_system.py
```

This will:
1. Initialize the RAG pipeline
2. Load all documents
3. Create embeddings
4. Test with sample questions
5. Display answers

## Understanding the Output

### First Run Output

```
============================================================
🚀 Initializing Smart City Citizen Assistant RAG System
============================================================
✓ Loaded: hospital_services.txt
✓ Loaded: transport_system.txt
✓ Loaded: id_card_services.txt
✓ Loaded: emergency_contacts.txt

Total documents loaded: 4

Splitting documents into text chunks...
✓ Created 28 text chunks

Generating embeddings (this may take a moment)...
Using sentence-transformers/all-MiniLM-L6-v2 model
Building FAISS vector database...
✓ FAISS database created successfully!

Setting up question-answering system...
Loading local text generation model...
Model: google/flan-t5-small
✓ Local pipeline loaded successfully
✓ QA chain setup complete!

============================================================
✅ RAG System Ready!
============================================================
```

### What Each Step Means

1. **Loading Documents**: Reads all `.txt` files from the `data/` folder
2. **Splitting**: Breaks documents into smaller pieces for better matching
3. **Embeddings**: Converts text to numbers (vectors) that capture meaning
4. **FAISS Database**: Builds a fast search index
5. **QA System**: Sets up the question-answering AI model

## Using the Web Interface

1. Open `http://localhost:8501` in your browser
2. Wait for "RAG System Ready!" message
3. Type questions in the chat box
4. View answers with source documents

### Example Questions to Try

- "Where can I get my city ID card?"
- "What are the bus fares?"
- "What hospital services are available?"
- "What should I do in a medical emergency?"
- "How do I apply for a passport?"
- "What public transportation options are available?"

## File Structure Reference

```
smart-city-assistant/
├── app.py                  # Main web application
├── test_system.py          # CLI test script
├── requirements.txt        # Python dependencies
├── README.md              # Main documentation
├── .env.example           # Environment config template
├── data/                  # City service documents
│   ├── hospital_services.txt
│   ├── transport_system.txt
│   ├── id_card_services.txt
│   └── emergency_contacts.txt
└── utils/
    └── rag_pipeline.py    # RAG system code
```

## Performance Tips

1. **Keep the app running**: Don't close the terminal while using
2. **First run is slow**: Model downloads and caching happen once
3. **Subsequent runs are fast**: Models load from cache
4. **RAM usage**: ~2GB during operation (normal)

## Adding New Documents

1. Add a `.txt` or `.pdf` file to the `data/` folder
2. Restart the application
3. The system will automatically load new documents

## Stopping the Application

Press `Ctrl+C` in the terminal where you ran `streamlit run app.py`

## Advanced Configuration

### Using OpenAI Instead of Local Models

1. Get an API key from https://platform.openai.com/
2. Edit `.env.example` → `.env`
3. Set `USE_OPENAI=true` and add your API key
4. Restart the app

### Changing the Model

Edit `utils/rag_pipeline.py` and change:
- `model_name` in `HuggingFaceEmbeddings()` for embeddings
- `repo_id` or `model` in the pipeline for LLM

## Getting Help

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all files are in the correct locations
3. Ensure Python version is 3.8+
4. Check that all dependencies are installed (`pip list`)
5. Review the error messages carefully

## System Requirements

- Python 3.8+
- 2GB+ RAM (4GB recommended)
- 2GB+ free disk space
- Internet connection (for first-time model downloads)

## Offline Usage

After the first run, the application can work offline because:
- Models are downloaded and cached locally
- All processing happens on your machine
- No API calls are needed (with local models)

## Security Notes

- All processing is local (no data sent to external servers)
- Documents are only used locally for generating answers
- No user data is collected or stored
- Safe for sensitive information (stays on your machine)
