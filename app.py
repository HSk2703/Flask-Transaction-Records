# Import libraries
from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation: List all transactions
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation: Add a new transaction
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == 'POST':
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }
        transactions.append(transaction)
        return redirect(url_for("get_transactions"))
    
    return render_template("form.html")

# Update operation: Edit an existing transaction
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        date = request.form['date']
        amount = float(request.form['amount'])

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break

        return redirect(url_for("get_transactions"))
    
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction)

    return {"message": "Transaction not found"}, 404

# Delete operation: Delete a transaction
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break

    return redirect(url_for("get_transactions"))

# Search Transactions
@app.route("/search", methods=["GET", "POST"])
def search_transactions():
    if request.method == 'POST':
        # Retrieve the minimum and maximum amount from the form
        min_amount = float(request.form['min_amount'])
        max_amount = float(request.form['max_amount'])

        # Filter transactions within the specified range
        filtered_transactions = [t for t in transactions if min_amount <= t['amount'] <= max_amount]

        # Render the transactions template with filtered transactions
        return render_template("transactions.html", transactions=filtered_transactions)

    # If the request method is GET, render the search form
    return render_template("search.html")

# Total Balance
@app.route("/balance")
def total_balance():
    # Calculate total balance by summing all transaction amounts
    balance = sum(t['amount'] for t in transactions)
    
    # Return the total balance as a formatted string
    return f"Total Balance: {balance:.2f}"

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
