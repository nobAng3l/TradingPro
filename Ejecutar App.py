import webbrowser
import subprocess
import threading
import time

def run():
    subprocess.Popen(['streamlit', 'run', 'app.py'])
    time.sleep(2)
    webbrowser.open_new("http://localhost:8501")

if __name__ == '__main__':
    threading.Thread(target=run).start()
