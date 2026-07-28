# Leucine Backend Assignment

## Project Overview

This project is a Backend API developed using **FastAPI**, **MongoDB**, and **Google Gemini AI**. It allows users to register, log in securely using JWT authentication, upload documents, and ask questions based on the uploaded documents using Retrieval-Augmented Generation (RAG).

---

## Features

- User Registration and Login
- JWT Authentication
- Secure Password Hashing
- Document Upload
- Text Chunking
- Embedding Generation using Sentence Transformers
- Semantic Search using Cosine Similarity
- AI-powered Question Answering using Google Gemini
- MongoDB Database Integration

---

## Tech Stack

- Python
- FastAPI
- MongoDB
- JWT Authentication
- Sentence Transformers
- Scikit-learn
- Google Gemini AI
- Uvicorn

---

## Prerequisites

Make sure the following are installed:

- Python 3.10 or above
- MongoDB
- Git

---

## Installation

Clone the repository:

```bash
git clone https://github.com/MITALI-CP/Leucine-Assignment.git
```

Move into the project directory:

```bash
cd Leucine_Assignment
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file and add the following:

```env
MONGO_URI=your_mongodb_connection_string
DATABASE_NAME=your_database_name
JWT_SECRET=your_secret_key
ALGORITHM=HS256
GEMINI_API_KEY=your_gemini_api_key
```

---

## Run the Project

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Authentication

- POST `/signup`
- POST `/login`

### Document

- POST `/upload-document`

### Chat

- POST `/chat`

---

## Project Structure

```
Leucine_Assignment/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── models/
│   ├── config.py
│   ├── database.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Author

**Mitali Rangani**