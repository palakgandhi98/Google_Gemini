# Health Management App
![healthy](https://github.com/user-attachments/assets/7f897ea1-fbf6-4b0b-91d2-e70ce9561796)

## Overview 📜

The Health Management App is a web application built using Streamlit and the Google Gemini Vision API. This app allows users to upload an image of their food, and it will provide a detailed breakdown of the calorie count for each food item, along with nutritional insights.

## Features 🌟
- Upload an image of your meal.
- Get a detailed breakdown of the calorie count for each food item.
- Receive insights on the nutritional value and whether the meal is healthy.
- Visualize the uploaded image within the app.

## Prerequisites 🛠️
- Python 3.6 or later
- Streamlit
- Google Gemini Vision API Key
- Pillow (Python Imaging Library)

## Setup 🛠️

### 1. Clone the Repository 📦
```bash
git clone https://github.com/palakgandhi98/HealthApp.git
cd HealthApp
```

### 2. Install Dependencies 📦
Make sure you have Python 3.7+ installed. Then, install the required packages:
```sh
pip install -r requirements.txt
```

### 3. Set Up Environment Variables 🔧
- Create a `.env` file in the root directory.
- Add your Google Gemini Vision API key to the `.env` file:
```sh
GOOGLE_API_KEY=your_api_key_here
```

### Running the Application 🚀

1. **Activate the virtual environment:**

    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Run the Streamlit application:**

    ```bash
    streamlit run healty.py
    ```

3. Open your web browser and navigate to the provided local URL (usually http://localhost:8501).

4. Upload an image of your meal using the file uploader.

5. Click the "Tell me the total calories" button to get the nutritional analysis.

### Example 📋

- **Upload an Image:**
- **Click the "Tell me the total calories" Button:** Submit Button
- **View the Response:**

## File Structure 📁
```
HealthApp/
│
├── .env
├── healty.py
└── README.md
```

## Dependencies 📦

The following Python packages are required to run the application:

- `streamlit` For building the web application.
- `Pillow` For image processing.
- `google-generativeai` For interacting with the Google Gemini Vision API.
- `python-dotenv` For loading environment variables.

## Contributing 🤝

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3.Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.

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
