from flask import Flask
app = Flask(__name__)
@app.route('/order/<customer>/<product>/<int:quantity>/<int:price>')
def order(customer, product, quantity, price):
    total = quantity * price
    if total > 10000:
        discount = total * 0.15
    else:
        discount = 0
        subtotal = total - discount
        gst = subtotal * 0.18
        final_amount = subtotal + gst
    return f"""
    <h1>Order Summary</h1>
    <hr>
    <b>Customer Name :</b> {customer}<br><br>
    <b>Product :</b> {product}<br><br>
    <b>Quantity :</b> {quantity}<br><br>
    <b>Price :</b> ₹{price}<br><br>
    <b>Total Amount :</b> ₹{total}<br><br>
    <b>Discount (15%) :</b> ₹{discount}<br><br>
    <b>GST (18%) :</b> ₹{gst}<br><br>
    <h2>Final Payable Amount : ₹{final_amount:.2f}</h2>
    """
if __name__ == "__main__":
    app.run(debug=True)
