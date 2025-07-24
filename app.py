from flask import Flask
app = Flask(__name__)

# Required: Root route
@app.route('/')
def home():
    return "Nexora.AI Fraud Detection API is running!"

# Your API endpoint
@app.route('/api/predict', methods=['POST'])
def predict():
    # Your prediction code
    return {"fraud": False}  # Replace with real logic

# Critical for Vercel
if __name__ == '__main__':
    app.run()
