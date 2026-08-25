from flask import Flask
app = Flask(__name__)
@app.route('/employee/<id>/<name>/<department>/<salary>')
def employee(id,name,department,salary):
    return f"""
    <h1>Employee Profile</h1>
    <hr>
    <b>Employee ID :</b> {id}<br><br>
    <b>Name :</b> {name}<br><br>
    <b>Department :</b> {department}<br><br>
    <b>Salary :</b> {salary}<br><br>
    """
if __name__ == "__main__":
    app.run(debug=True)
