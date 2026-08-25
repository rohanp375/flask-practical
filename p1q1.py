from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return """
    <h1>Welcome to Flask Application</h1>
    <p>This is the Home Page.</p>
    """
@app.route('/about')
def about():
    return """
    <h1>About Us</h1>
    <p>This application is developed using Flask Framework.</p>
    """
@app.route('/contact')
def contact():
    return """
    <h1>Contact Us</h1>
    <p>Email: info@example.com</p>
    <p>Phone: 9876543210</p>
    """
if __name__ == "__main__":
    app.run(debug=True)
