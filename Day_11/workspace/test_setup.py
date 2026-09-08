"""
test_setup.py
Run this script to verify that your environment is ready for Day 11.
"""
import sys

def verify():
    print("Checking Python environment...")
    print(f"Python: {sys.version.split()[0]}")
    
    missing = []
    for pkg in ["pandas", "matplotlib", "seaborn", "openpyxl"]:
        try:
            mod = __import__(pkg)
            print(f"  [OK] {pkg:<12} (version: {getattr(mod, '__version__', 'unknown')})")
        except ImportError:
            print(f"  [MISSING] {pkg:<12}")
            missing.append(pkg)
            
    if missing:
        print(f"\nPlease install missing packages with:\n  pip install {' '.join(missing)}")
    else:
        print("\nAll required libraries are successfully installed!")

if __name__ == "__main__":
    verify()
