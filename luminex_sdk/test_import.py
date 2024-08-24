import sys
import os

# Add the directory containing luminex_sdk to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'luminex_sdk')))

# Test import
try:
    import luminex_sdk
    print("Luminex SDK imported successfully!")
except ImportError as e:
    print(f"ImportError: {e}")

# Wait for user input to exit
input("Press Enter to exit...")
