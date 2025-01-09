# Gemini Text to SQL
![Gemini Text to SQL](https://github.com/user-attachments/assets/bd2b2532-a240-4fff-98b7-016ee0c4c793)

## Overview 📜

Gemini Text to SQL is a Streamlit application that uses Google Gemini Pro to convert natural language questions into SQL queries and retrieve data from a SQLite database. This application serves as a convenient way to interact with a database using plain English.

## Features 🌟
- **Natural Language to SQL Conversion**: Convert English questions into SQL queries.
- **Database Interaction**: Execute SQL queries on a SQLite database.
- **User-Friendly Interface**: Display query results in an intuitive and accessible manner.

## Prerequisites 🛠️
- Python 3.6 or later
- SQLite database named `student.db`
- Google API Key for Google Gemini Pro

## Setup 🛠️

### 1. Clone the Repository 📦
```bash
git clone https://github.com/palakgandhi98/Gemini Text to SQL.git
cd Gemini Text to SQL
```

### 2. Install Dependencies 📦
Make sure you have Python 3.7+ installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```
### 3. Set Up Environment Variables 🔧
Create a `.env` file in the root directo

### Database 🗄️

Ensure you have a SQLite database named `student.db` with a table named `STUDENT` containing the following columns:

- `NAME`
- `CLASS`
- `SECTION`
- `MARKS`

### Running the Application 🚀

1. **Activate the virtual environment:**

    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

3. Open the provided URL in your web browser to access the application.

## Usage 💻

1. Enter a question in the input field.
2. Click the "Ask Me Question" button.
3. The application will convert the question to an SQL query, execute it on the SQLite database, and display the results.

### Example 📋

- **Question:** `How many entries of records are present?`
- **SQL Query:** `SELECT COUNT(*) FROM STUDENT;`

## File Structure 📁
```
Gemini Text to SQL/
│
├── .env
├── app.py
└── README.md
```
## Dependencies 📦

The following Python packages are required to run the application:

- `streamlit`
- `SQLite`
- `google-generativeai`
- `python-dotenv`

## Contributing 🤝

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your branch to your fork.
5. Create a pull request.

## License 📜
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
Distributed under the MIT License. See `LICENSE` for more informati

## Acknowledgments 🙏
- Streamlit for the web-based interface.
- Google Gemini Pro for the generative AI model.

## Contact 📧
For any questions or suggestions, feel free to open an issue or contact the maintainer directly.

 * [![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff)](https://www.github.com/palakgandhi98)
 * [![LinkedIn](https://img.shields.io/badge/Linkedin-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/palakgandhi98)

Let's build something amazing together! 🌟🚀
