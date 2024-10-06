# Flask Random Password Generator

This is a simple Flask application that generates a random password based on user input for the number of characters and the type of characters (letters and digits). 

## Overview

The application consists of a single web page where users can specify the following:
1. A range for random characters (letters and digits).
2. The length of the password they want to generate.

The application then generates a random password based on the specified length and displays it back to the user.

## File Structure

```
your_project/
├── flask_range.py                   # The main Flask application code
└── template/
    └── input_range.html     # The HTML template for user input
```

### flask_range.py

The main Flask application is contained in `flask_range.py`. Below is a breakdown of its functionality:

```python
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
```

### Key Components

- **Flask Initialization**: The application is initialized using `Flask(__name__)`.

- **Route Handling**:
  - The main route `/` handles both `GET` and `POST` requests.
    - On `POST`, it retrieves the user input from the form, checks if the length is greater than 0, and generates a password of the specified length using letters and digits.
    - If the length is 0 or invalid, it re-renders the input form without any generated password.

- **Password Generation**: The password is generated using a combination of letters and digits. The generation process occurs inside a loop, where random characters are appended to a string until the desired length is reached.

- **Displaying the Password**: After generating the password, the application redirects to the `/display_num` route, where the generated password is displayed on the same input form.

### HTML Template (input_range.html)

The corresponding HTML file should be placed in the `template` folder and structured as follows:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Input Range</title>
</head>
<body>
    <h1>Random Password Generator</h1>
    <form method="POST" action="/"> 
        <!-- Range for password length -->
        <label>Length of the Password:</label>
        <input type="range" id="length_password" name="length_password" 
               value="2" min="1" max="20" required>
        <output>2</output>
        <br><br>

        <input type="submit" value="Generate Password">

        <!-- Conditionally display the generated password -->
        {% if password %}
        <p>Random Password Generated: {{ password }}</p>
        {% endif %}
    </form>
</body> 
</html>
```

### How to Run

1. Ensure you have Flask installed:
   ```bash
   pip install Flask
   ```

2. Create the necessary folder structure as shown above.

3. Run the application with:
   ```bash
   python app.py
   ```

4. Open a web browser and navigate to `http://127.0.0.1:5000/` to use the application.
