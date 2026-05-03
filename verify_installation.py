"""
Installation Verification Script
Checks if all dependencies are installed correctly
"""

import os
import sys
import subprocess

def check_python():
    """Check Python version."""
    print("Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"  ✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"  ❌ Python 3.8+ required (found {version.major}.{version.minor}.{version.micro})")
        return False

def check_file(filepath, description):
    """Check if a file exists."""
    print(f"Checking {description}...")
    if os.path.exists(filepath):
        print(f"  ✅ {filepath} - OK")
        return True
    else:
        print(f"  ❌ {filepath} - NOT FOUND")
        return False

def check_directory(dirpath, description):
    """Check if a directory exists and has files."""
    print(f"Checking {description}...")
    if os.path.exists(dirpath):
        files = os.listdir(dirpath)
        if files:
            print(f"  ✅ {dirpath} - OK ({len(files)} files)")
            for f in files:
                print(f"    • {f}")
            return True
        else:
            print(f"  ❌ {dirpath} - EMPTY")
            return False
    else:
        print(f"  ❌ {dirpath} - NOT FOUND")
        return False

def check_import(module_name, friendly_name=None):
    """Check if a module can be imported."""
    if friendly_name is None:
        friendly_name = module_name
    print(f"Checking {friendly_name}...")
    try:
        __import__(module_name)
        print(f"  ✅ {module_name} - OK")
        return True
    except ImportError as e:
        print(f"  ❌ {module_name} - NOT INSTALLED ({e})")
        return False

def main():
    print("=" * 70)
    print("🔍 Smart City Assistant - Installation Verification")
    print("=" * 70)
    print()
    
    results = {}
    
    # Check Python
    results['python'] = check_python()
    print()
    
    # Check project files
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    results['app'] = check_file(
        os.path.join(base_dir, 'app.py'),
        'Main application file'
    )
    print()
    
    results['rag'] = check_file(
        os.path.join(base_dir, 'utils', 'rag_pipeline.py'),
        'RAG pipeline module'
    )
    print()
    
    results['req'] = check_file(
        os.path.join(base_dir, 'requirements.txt'),
        'Requirements file'
    )
    print()
    
    results['data_dir'] = check_directory(
        os.path.join(base_dir, 'data'),
        'Data directory'
    )
    print()
    
    results['utils_dir'] = check_directory(
        os.path.join(base_dir, 'utils'),
        'Utils directory'
    )
    print()
    
    # Check imports
    print("-" * 70)
    print("Checking Python Packages")
    print("-" * 70)
    print()
    
    results['streamlit'] = check_import('streamlit')
    results['langchain'] = check_import('langchain')
    results['faiss'] = check_import('faiss', 'FAISS')
    results['sentence_transformers'] = check_import('sentence_transformers', 'Sentence Transformers')
    results['transformers'] = check_import('transformers')
    results['torch'] = check_import('torch', 'PyTorch')
    print()
    
    # Summary
    print("=" * 70)
    print("📊 Verification Summary")
    print("=" * 70)
    
    all_checks = list(results.values())
    passed = sum(1 for r in all_checks if r)
    total = len(all_checks)
    
    print(f"\nChecks Passed: {passed}/{total}")
    print()
    
    if all(all_checks):
        print("✅ All checks passed! You can run the application.")
        print("\nNext steps:")
        print("  1. Run: streamlit run app.py")
        print("  2. Open: http://localhost:8501")
        return 0
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        print("\nCommon issues:")
        print("  • Run: pip install -r requirements.txt")
        print("  • Make sure you're in the project directory")
        print("  • Check that all files are present")
        return 1

if __name__ == "__main__":
    sys.exit(main())
