from flask import Flask
app = Flask(__name__)
@app.route('/product/<product_name>/<int:price>/<category>')
def product(product_name,price,category):
    discount = price * 0.10
    subtotal = price - discount
    gst = subtotal * 0.18
    final_price = subtotal + gst
    return f"""
    <h1>Product Information</h1>
    <hr>
    <b>Product Name :</b> {product_name}<br><br>
    <b>Category :</b> {category}<br><br>
    <b>Price :</b> ₹{price}<br><br>
    <b>Discount (10%) :</b> ₹{discount}<br><br>
    <b>GST (18%) :</b> ₹{gst}<br><br>
    <h2>Final Price : ₹{final_price:.2f}</h2>
    """
if __name__ == "__main__":
    app.run(debug=True)
