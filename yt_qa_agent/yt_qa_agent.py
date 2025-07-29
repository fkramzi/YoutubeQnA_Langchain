### Youtube Q&A Agent 

import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Load your OpenAI API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def get_video_id(url):
    """Extract the video ID from a YouTube URL"""
    if "watch?v=" in url:
        return url.split("watch?v=")[-1]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1]
    else:
        raise ValueError("Invalid YouTube URL")

def get_transcript_text(video_id):
    """Fetch transcript from YouTube"""
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([entry["text"] for entry in transcript])

# Step 1: Get YouTube Transcript
video_url = input("Enter a YouTube video URL: ")
video_id = get_video_id(video_url)
transcript = get_transcript_text(video_id)

# Step 2: Split the transcript
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = splitter.create_documents([transcript])

# Step 3: Create vector DB
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(docs, embeddings)

# Step 4: Setup LLM and QA Chain
retriever = db.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    retriever=retriever,
    return_source_documents=True
)

# Step 5: Ask questions
while True:
    question = input("\nAsk a question about the video (or type 'exit'): ")
    if question.lower() == "exit":
        break
    answer = qa_chain({"query": question})
    print("\nAnswer:", answer["result"])
