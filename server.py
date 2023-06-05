"""
Repository: python-server
Description: A customizable Python server implementation using the Flask framework. Provides a foundation for serving web applications, APIs, or static files.

Instructions:
1. Clone or fork this repository.
2. Install required packages: pip install flask.
3. Customize server options.
4. Run server: python server.py.
5. Access server via appropriate URL.
6. Customize and extend for your needs.

Note: Keep sensitive info secure. Use responsibly and follow security best practices.

"""

from flask import Flask

app = Flask(__name__)

# Custom Configuration Options
GITHUB_USERNAME = "<YOUR_GITHUB_USERNAME>"  # Replace with your GitHub username
REPO_NAME = "python-server"  # Replace with your desired repository name
PORT_NUMBER = 5000  # Replace with desired port number for your server

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=PORT_NUMBER)
