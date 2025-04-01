import os
from flask import Flask

# Create a Flask instance
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    return "Hello, Render!"

# Ensure the app listens on the port provided by the Render environment variable
if __name__ == "__main__":
    # Get the dynamic port Render assigns (or fallback to 10000)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)  # Bind to all IP addresses and use the dynamic port
