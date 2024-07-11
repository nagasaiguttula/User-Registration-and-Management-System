# User Registration and Management System

This is a simple Flask application that allows users to register by providing their name, email, age, and date of birth. The user data is stored in an SQLite database, and there is an endpoint to view all registered users in a tabular format.
## Project Structure
```
task/
├── main.py
├── templates/
│   ├── index.html
│   └── users.html
```
## Prerequisites
Before running the application, make sure you have Python and the required packages installed.
### Python
You can download and install Python from the [official website](https://www.python.org/downloads/).

### Required Packages
Install the required packages using pip:
pip install flask sqlite3
## Getting Started

### Step 1: Clone the repository
Clone the repository to your local machine:
git clone <repository_url>
cd task
### Step 2: Database Setup
The database is set up automatically when you run the application for the first time. The `init_db()` function in `main.py` creates the necessary table if it doesn't already exist.
### Step 3: Run the Application
Run the Flask application:
python main.py
The application will start, and you can access it in your web browser at `http://127.0.0.1:5000`.
## Application Features
### User Registration
1. Navigate to the root URL (`http://127.0.0.1:5000`).
2. Fill in the form with your name, email, age, and date of birth.
3. Click the "Save User" button to submit the form.
4. The data will be stored in the SQLite database.
5. If the email or age is invalid, an error message will be displayed.

### View Registered Users
1. Navigate to the `/users` URL (`http://127.0.0.1:5000/users`).
2. The page will display a table with all registered users, including their name, email, age, and date of birth.
## Files Description
### `main.py`
This is the main application file that contains the following:
- `init_db()`: Initializes the SQLite database and creates the `users` table.
- Route for the root URL (`/`): Displays the user registration form and handles form submissions.
- Route for `/users`: Displays a list of all registered users.

### `templates/index.html`
This is the HTML template for the user registration form. It contains:
- A form to input user details (name, email, age, and date of birth).
- A button to submit the form.
- Error message display if the input is invalid.
### `templates/users.html`
This is the HTML template for displaying the list of registered users. It contains:
- A table displaying user details (name, email, age, and date of birth).

## Example Usage
1. Start the application by running `python main.py`.
2. Open your web browser and navigate to `http://127.0.0.1:5000`.
3. Register a new user by filling out the form and submitting it.
4. View the list of registered users by navigating to `http://127.0.0.1:5000/users`.
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
## Acknowledgments

- This project uses [Flask](https://flask.palletsprojects.com/), a lightweight WSGI web application framework in Python.
- SQLite is used as the database for simplicity and ease of use.
