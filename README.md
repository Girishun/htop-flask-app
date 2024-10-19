# HTOP Flask App

This project is a Flask-based web application that exposes an `/htop` endpoint. The endpoint displays system information including:

- **Name**: Girishun Kumar R
- **Username**: Girishun
- **Server Time**: 18:30
- **Top Output**: A snapshot of the system's `top` command output

## Features
- `/htop` endpoint that displays real-time system stats in a browser.
- Hosted using Codespaces with public visibility enabled.

## Requirements
- Python 3.x
- Flask

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/htop-flask-app.git
    cd htop-flask-app
    ```

2. **Install dependencies:**

    Install Flask by running:

    ```bash
    pip install flask
    ```

3. **Run the application:**

    Start the Flask app:

    ```bash
    python app.py
    ```

4. **Access the application:**

    Visit `http://localhost:5000/htop` to view the system stats.

## Deploying on GitHub Codespaces

This app can be deployed on GitHub Codespaces. Follow these steps:

1. Create a Codespace for this repository.
2. Follow the setup instructions to start the Flask server inside the Codespace.
3. Make the port public to access the `/htop` endpoint externally.
