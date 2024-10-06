
# Flask User Authentication Application

This application demonstrates a simple user registration and authentication system built with Flask. It uses Base64 encoding for password storage and decoding. The application contains three primary pages: the Home (Registration) page, the Login page, and the Success page.

## Features
- **User Registration**: Users can register with a username, email, and password.
- **Password Encoding**: Passwords are encoded using Base64 for storage.
- **User Authentication**: Users can log in, and their credentials are verified against the registered data.
- **Success Page**: Upon successful login, users are redirected to a success page.

## Requirements
To run this application, you'll need:
- **Python** (3.7+ recommended)
- **Flask** (install using `pip install flask`)

## Project Structure
```plaintext
project/
│
├── app.py                # Main application file
├── templates/            # Folder for HTML templates
│   ├── index.html        # Home (Registration) page
│   ├── login.html        # Login page
│   └── Success.html      # Success page
└── README.md             # This README file
```

## Setup and Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install the required packages**:
   Make sure you have Flask installed:
   ```bash
   pip install flask
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```
   The application will be available at `http://127.0.0.1:5000`.

## Application Routes

### 1. Home (Registration) Page - `/home`
- **Method**: GET, POST
- **Description**: Allows users to register with a username, email, and password. Passwords are encoded with Base64 before being stored.
- **Template**: `index.html`
  
### 2. Login Page - `/login`
- **Method**: GET, POST
- **Description**: Authenticates the user by verifying the email and decoded password against registered data. If successful, the user is redirected to the Success page.
- **Template**: `login.html`

### 3. Success Page - `/Success`
- **Method**: GET, POST
- **Description**: Displays a personalized message if login is successful. The user's name is displayed on the page.
- **Template**: `Success.html`

## How It Works
1. **Registering a User**:
   - Go to `/home` and enter your username, email, and password.
   - On submission, the password is encoded with Base64 and stored in `registered_data`.

2. **Logging In**:
   - Go to `/login` and enter your registered email and password.
   - If credentials are correct, you are redirected to the `/Success` page with a welcome message.

3. **Data Storage**:
   - User data, including the username and encoded password, is stored temporarily in the `registered_data` dictionary for demonstration purposes. This data is not persistent and will be cleared when the server restarts.

## Sample Usage
After running the application:
1. Register a new user by going to `http://127.0.0.1:5000/home`.
2. Enter the email and password you registered with on the Login page.
3. Upon successful login, you will be redirected to the Success page, where you will see a welcome message.

## Notes
- **Base64 Encoding**: This example uses Base64 encoding for demonstration. Base64 encoding is **not** secure for real-world password storage. For production, consider using secure hashing algorithms like bcrypt or Argon2.
- **Data Storage**: This app uses a simple dictionary to store data. In a real application, use a database for data persistence.

## License
This project is open-source and available under the MIT License.
