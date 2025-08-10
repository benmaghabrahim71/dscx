#!/usr/bin/env python3

import os
import sys
import subprocess

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import flask
        import psutil
        print("✅ All dependencies are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements_dashboard.txt"])
        return True

def main():
    print("🚀 Starting MHDDoS Dashboard...")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Check if start.py exists
    if not os.path.exists("start.py"):
        print("❌ Error: start.py not found in current directory!")
        print("Make sure you're running this from the MHDDoS directory.")
        return
    
    # Start the Flask app
    print("🌐 Starting web server on http://localhost:5000")
    print("📱 Open your browser and navigate to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        from app import app
        app.run(debug=False, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n🛑 Dashboard stopped by user")
    except Exception as e:
        print(f"❌ Error starting dashboard: {e}")

if __name__ == "__main__":
    main()
