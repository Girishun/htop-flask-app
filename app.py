from flask import Flask, redirect, url_for
import subprocess
import getpass
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('htop'))

@app.route('/htop')
def htop():
    # Full Name
    full_name = "Girishun Kumar R"

    # System Username
    system_user = getpass.getuser()

    # Server Time in IST
    tz = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Top Output
    top_output = subprocess.getoutput('top -b -n 1')

    return f"""
    Name: {full_name}<br>
    user: {system_user}<br>
    Server Time(IST): {server_time}<br>
    TOP Output:  
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
