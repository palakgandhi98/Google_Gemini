#  Multilanguage Invoice Extractor

![Multilanguage Invoice Extractor](https://github.com/user-attachments/assets/cbb96763-492b-45ea-a812-d9b6d8547ac1)

## Overview 📜

The Multilanguage Invoice Extractor is a Streamlit application that utilizes Google's Gemini Pro Vision model to extract and understand information from invoice images. This tool is designed to help users quickly get insights from invoices in various languages by simply uploading an image of the invoice and asking questions about it.

## Features 🌟

- Upload invoice images in formats like JPG, JPEG, and PNG.
- Enter custom prompts to ask specific questions about the invoice.
- Receive detailed responses based on the invoice image.
- Supports multiple languages.

## Prerequisites 🛠️

- Python 3.6 or later
- Streamlit
- Google Gemini Vision API Key
- Pillow (Python Imaging Library)
- python-dotenv
- 

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/Invoice Extractor.git
   cd Invoice Extractor
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Google API key:

   ```sh
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

1. Run the Streamlit application:

   ```sh
   streamlit run app.py
   ```

2. Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload an image of the invoice using the file uploader.

4. Enter your question or prompt in the text input field.

5. Click the "Tell me about the invoice" button to get the response.

## Example

1. Upload an invoice image.
2. Enter a prompt like "What is the total amount due?"
3. Click the "Tell me about the invoice" button.
4. View the detailed response based on the invoice image.

## File Structure 📁

```sh
Gemini Text to SQL/
│
├── .env
├── app.py
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
