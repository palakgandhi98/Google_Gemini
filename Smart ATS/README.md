# Smart ATS

![Gemini Resume ATS](https://github.com/user-attachments/assets/3a35fe33-f9b1-44dc-9952-8763fb13b844)

## Overview 📜

Smart ATS is a Streamlit application designed to help job seekers improve their resumes by evaluating them against job descriptions. The application utilizes the Google Gemini API to provide insights and suggestions based on the latest trends and requirements in the tech field, including software engineering, data science, data analysis, and big data engineering.


## Features 🌟
- **Resume Evaluation**: Upload your resume in PDF format and get an evaluation based on the job description you provide.
- **Job Description Match**: Receive a percentage match indicating how well your resume aligns with the job description.
- **Missing Keywords**: Identify keywords missing from your resume that are essential for the job description.
- **Profile Summary**: Get a summary of your profile based on the job description.

## Prerequisites 🛠️
- Python 3.7+
- Streamlit
- PyPDF2
- google-generativeai
- python-dotenv

## Setup 🛠️

### 1. Clone the Repository 📦
```sh
git clone https://github.com/palakgandhi98/Gemini Resume ATS.git
cd Gemini Resume ATS
```

### 2. Install Dependencies 📦
Make sure you have Python 3.7+ installed. Then, install the required packages:
```sh
pip install -r requirements.txt
```

### 3. Set Up Environment Variables 🔧
Create a `.env` file in the root directory

### 4. Run the Application 🚀
Run the Streamlit app using the following command:
```sh
streamlit run Vision.py
```

### 5. Access the Application 🌐
Open your web browser and go to `http://localhost:8501` to access the application.

## Usage 💻
1. **Open your browser** and go to the URL provided by Streamlit (usually `http://localhost:8501`).

2. **Paste the Job Description** in the text area provided.

3. **Upload Your Resume** in PDF format.

4. **Click Submit** to get the evaluation and suggestions.

## File Structure 📁
```
Gemini Resume ATS/
│
├── .env
├── app.py
└── README.md
```
## Dependencies 📦

The following Python packages are required to run the application:

- `streamlit`
- `PyPDF2`
- `google-generativeai`
- `python-dotenv`

## Contributing 🤝

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project 🍴
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`) 🌱
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`) 📝
4. Push to the Branch (`git push origin feature/AmazingFeature`) 🚀
5. Open a Pull Request 🔔

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
