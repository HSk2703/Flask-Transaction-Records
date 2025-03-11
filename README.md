# Flask Transaction Records

**Flask Transaction Records** is a web-based application that allows users to record, manage, and track financial transactions securely. Built using Flask, the app provides a simple and intuitive interface for handling income and expense records.

## Features

- **User Authentication** – Secure login and registration system.
- **Transaction Management** – Add, edit, delete, and categorize transactions.
- **Analytics Dashboard** – Visualize transaction data through charts.
- **REST API Support** – Integrate with external services.
- **Database Storage** – Securely store transaction records.
- **Export & Import** – Export transactions in CSV format.

## Technologies Used

- **Backend:** Flask, Python
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite / PostgreSQL
- **Authentication:** Flask-Login, JWT
- **Deployment:** Docker, Heroku/AWS/GCP

## Project Structure

```
Flask-Transaction-Records/
├── models/             # Database models
├── routes/             # API and view routes
├── templates/          # HTML templates
├── static/             # CSS, JavaScript, images
├── app.py              # Main application file
├── config/             # Configuration settings
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

## Getting Started

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/HSk2703/Flask-Transaction-Records.git
cd Flask-Transaction-Records
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and configure the necessary environment variables:

```
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=your_database_connection_string
SECRET_KEY=your_secret_key
```

### 5. Run the Application

```bash
flask run
```

### 6. Access the Application

Open your browser and navigate to:

👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## API Endpoints

| Method | Endpoint         | Description                     |
|--------|-----------------|---------------------------------|
| POST   | `/add`          | Add a new transaction          |
| GET    | `/transactions` | Get all transaction records    |
| PUT    | `/update/<id>`  | Update a specific transaction  |
| DELETE | `/delete/<id>`  | Delete a transaction record    |

## Contributing

Contributions are welcome! To contribute:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix.
3. **Commit your changes** with a clear message.
4. **Push your changes** to your forked repository.
5. **Submit a pull request** with details of your changes.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

