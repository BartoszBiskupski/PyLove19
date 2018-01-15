from flask import Flask, request_finished, render_template, redirect, request


app = Flask(__name__)

balance = 1000
history= []
@app.route("/")
def redir():
    return render_template("zadanie_1a.html")

@app.route("/account", methods=["GET", "POST"])
def account():
    global balance
    if request.method == "POST":
        account = request.form.get("account")
        amount = int(request.form.get("amount"))
        balance -= amount
        history.append("Withdraw of {} balance: {}".format(amount, balance))
        return redirect("/account")


    return render_template("zadanie_1a.html", history = history, balance = balance)

app.run(debug=True)