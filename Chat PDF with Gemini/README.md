# Chat PDF with Google Gemini 🚀

![Screenshot 2025-01-09 192516](https://github.com/user-attachments/assets/0f220604-f9cc-4380-af8b-ef4a75a76d2d)


This project is a Streamlit application designed to allow users to chat with multiple PDF documents using Google's Gemini AI 🤖. The application leverages LangChain for handling document processing, embeddings, and conversational chains.

## Features 🌟

- 📥 Upload multiple PDF files.
- 🔍 Process the PDFs to extract text and create embeddings.
- ❓ Ask questions based on the content of the PDFs.
- 💬 Get detailed responses from the Gemini AI model.

## Prerequisites 📜

- Python 3.7+
- Google API Key for Google Generative AI services.

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/palakgandhi98/Google_Gemini/Chat PDF with Google Gemini
   cd Chat PDF with Google Gemini
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API Key:
   Create a `.env` file in the root directory of the project and add your Google API Key:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage 💻

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the provided URL in your web browser.

3. Upload your PDF files using the sidebar menu.

4. Click the "Submit & Process" button to process the PDFs.

5. Ask questions in the text input field to get responses based on the content of the uploaded PDFs.

## File Structure 📁

- `app.py`: The main application file.
- `.env`: Environment variables file (containing the Google API Key).
- `requirements.txt`: List of Python dependencies.
- `faiss_index`: Directory to store the vector store index (generated during processing).

## Dependencies 📦

The following Python packages are required to run the application:

- `streamlit`
- `PyPDF2`
- `langchain`
- `langchain_google_genai`
- `google-generativeai`
- `faiss`
- `python-dotenv`

## Contributing 🤝

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📜
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
Distributed under the MIT License. See `LICENSE` for more information.

## Contact 📧
 * [![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff)](https://www.github.com/palakgandhi98)
 * [![LinkedIn](https://img.shields.io/badge/Linkedin-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/palakgandhi98)

Let's build something amazing together! 🌟🚀
