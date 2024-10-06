from flask import Flask, render_template, request, redirect, url_for
import base64  # Import base64 for encoding and decoding

app = Flask(__name__, template_folder="templates")
registered_data = {}

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

            # Store encoded password in the registered_data
            registered_data[email] = {'Name': name, 'Decode Password': decoded_password, 'Encoded password':encoded_password}
            print(registered_data)

            # Redirect to the login page with the username
            return redirect(url_for("login", uname=name))

        return render_template("index.html")

    @app.route("/", methods=["GET", "POST"])
    def index():
        return redirect(url_for("home"))
    
    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form["uemail"]
            password = request.form["upassword"]

            # Check if email is registered
            user_data = registered_data.get(email)
            if user_data and user_data['Password'] == password:
                # Redirect to the success page with the user's name
                return redirect(url_for("Success", uname=user_data['Name']))
            else:
                return "Invalid email or password", 401

        return render_template("login.html")
    
    # Allow both GET and POST methods for the Success route
    @app.route("/Success", methods=["GET", "POST"])
    def Success():
        # Access the 'uname' query parameter from the URL
        name = request.args.get("uname", "")
        return render_template("Success.html", name=name)

# Ensure that the app runs only if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
