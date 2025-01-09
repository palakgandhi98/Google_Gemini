# YouTube Video Transcript Summarizer 🎬📝

## Overview 📚

This project is a Streamlit application that allows users to input a YouTube video URL and get a summarized version of the video transcript. The summarization is powered by Google's Gemini Pro model, which ensures the summaries are concise and informative.

## Features ✨

- Extract transcripts from YouTube videos.
- Summarize the transcript using Google's Gemini Pro model.
- Display the summarized notes in a user-friendly interface.

## Requirements 🛠️

- Python 3.x
- Streamlit
- Google Generative AI
- youtube-transcript-api
- python-dotenv

## Installation 💻

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/YouTube Transcribe Summerizer.git
    cd YouTube Transcribe Summerizer
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Set up your environment variables:

    Create a `.env` file in the root directory and add your Google API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage 🔍

1. Run the Streamlit application:

    ```sh
    streamlit run app.py
    ```

2. Open your browser and go to the provided local URL (usually `http://localhost:8501`).

3. Enter a YouTube video URL in the input field and click "Get Detailed Notes" to see the summarized transcript.

## File Structure 📁

```sh
YouTube Transcribe Summerizer/
│
├── .env
├── app.py
└── README.md
```

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
