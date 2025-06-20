from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # ✅ Get the port from Render
    app.run(host='0.0.0.0', port=port, debug=True)  # ✅ Bind to 0.0.0.0 for public access
