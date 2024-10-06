from flask import Flask, render_template, request, redirect, url_for
import base64  # Import base64 for encoding and decoding

app = Flask(__name__, template_folder="templates")

class WebPage:
    @app.route("/home", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            name = request.form["uname"]
            email = request.form["uemail"]
            password = request.form["upassword"]

            # Encode the password 
            encoded_password = base64.b64encode(password.encode("utf-8")) 
            print("Encoded Password:", encoded_password.decode("utf-8")) 

            # Decode the password
            decoded_password = base64.b64decode(encoded_password).decode("utf-8")
            print("Decoded Password:", decoded_password)

            # Check the username and redirect
            if name == "Sai":
                return redirect(url_for("login", uname=name))
            else:
                return render_template("index.html")

        return render_template("index.html")

    @app.route("/", methods=["GET", "POST"])
    def index():
        return redirect(url_for("home"))
    
    @app.route("/login")
    def login():
        # Access the 'uname' query parameter from the URL
        name = request.args.get("uname", "")
        return render_template("Success.html", name=name)

# Ensure that the app runs only if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
