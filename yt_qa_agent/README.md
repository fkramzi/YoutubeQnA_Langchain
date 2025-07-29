# YouTube Q&A Agent

This project is a command-line tool that allows you to ask questions about the content of any YouTube video using OpenAI's language models and LangChain. It automatically fetches the transcript of a YouTube video, processes it, and answers your questions based on the video content.

## Features
- Extracts transcript from YouTube videos
- Splits transcript into manageable chunks
- Embeds transcript using OpenAI embeddings
- Stores embeddings in a vector database (Chroma)
- Uses a RetrievalQA chain with OpenAI's GPT-3.5-turbo to answer questions

## Requirements
- Python 3.8+
- OpenAI API key
- Required packages (see below)

## Installation
1. Clone this repository or copy the files to your local machine.
2. Install dependencies:
   ```bash
   pip install langchain openai chromadb youtube-transcript-api python-dotenv
   ```
3. Create a `.env` file in the project directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage
1. Run the script:
   ```bash
   python yt_qa_agent.py
   ```
2. Enter a YouTube video URL when prompted.
3. Ask questions about the video transcript. Type `exit` to quit.

## Example
```
Enter a YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Ask a question about the video (or type 'exit'): What is the main topic?
Answer: ...
```

## How it works
- The script extracts the video ID from the provided URL.
- It fetches the transcript using `youtube-transcript-api`.
- The transcript is split and embedded using LangChain and OpenAI.
- A vector database is created for efficient retrieval.
- Questions are answered using a RetrievalQA chain powered by GPT-3.5-turbo.

## License
This project is for educational purposes.
