import os
import datetime
import subprocess
from django.http import HttpResponse

def htop_view(request):
    name = "Divyanshu"  # Replace with your name
    username = os.getenv("USER", "Unknown")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True)
    except subprocess.CalledProcessError:
        top_output = "Error fetching top output"

    response_text = f"""
    <html>
    <body>
        <h2>Name: {name}</h2>
        <h3>User: {username}</h3>
        <h3>Server Time (IST): {server_time}</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response_text)