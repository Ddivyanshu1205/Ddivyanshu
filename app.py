from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Divyanshu Gupta"
    username = os.getlogin()
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput('top -bn1')

    return f"""
    <pre>
    Name: {name}
    User: {username}
    Server Time (IST): {server_time}
    TOP Output:
    {top_output}
    </pre>
    """

if __name__ == '__main__p':
    app.run(host='0.0.0.0', port=5000)