from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="template")

# Route for the login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get the username from the form submission
        username = request.form["uname"]
        # Redirect to the welcome page, passing the username as a query parameter
        return redirect(url_for("welcome", username=username))
    return render_template("flask_website.html")

# Route for the welcome page
@app.route("/welcome")
def welcome():
    # Get the username from the query string (passed during redirect)
    username = request.args.get("username")
    return render_template("Welcome.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)
