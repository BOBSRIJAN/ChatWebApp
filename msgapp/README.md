# Django Chat App

This is a simple chat application built with Django and MongoDB. Users can log in with a username, send messages, and see messages from other active users in real-time.

## Features

- User login with unique usernames
- Real-time chat messaging
- Active user tracking
- Messages stored in MongoDB
- Simple and clean user interface

## Technologies Used

- Django 5.1.4
- MongoDB
- Python
- HTML/CSS for frontend templates

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd chat-app
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Make sure MongoDB is installed and running on your machine. The app connects to MongoDB to store messages and active users.

5. Configure MongoDB connection if needed in `msgapp/app/dbconf.py`.

6. Apply Django migrations (if any):

   ```bash
   python manage.py migrate
   ```

## Running the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/` to access the app.

## Usage

- Navigate to the login page and enter a unique username.
- Once logged in, you can send messages and see messages from other users.
- Use the logout option to end your session.

## License

