from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__, template_folder="template")

@app.route("/", methods=["POST", "GET"])
def inp_rng():
    l = ""
    if request.method == "POST":
        # Get the number from the form
        i = int(request.form["number_range"])
        x = int(request.form["length_password"])
        
        # Ensure length is greater than 0
        if x > 0:
            for _ in range(x):
                # Randomly choose between a letter or number for password
                #random_char = random.choice(string.ascii_letters+string.punctuation) + string.digits
                random_char = random.choice(string.ascii_letters + string.digits)
                l += random_char
            # Redirect to the display_num route with the generated password
            return redirect(url_for("display_num", l=l))
        else:
            return render_template("input_range.html")

    # Render the input form when accessed via GET
    return render_template("input_range.html")

@app.route("/display_num")
def display_num():
    # Get the value of l (the generated password) from the query parameter
    password = request.args.get("l")
    
    # Display the generated password in the template
    return render_template("input_range.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)