# Zania-AI-Challenge

This repository contains the solution to the Zania AI Challenge. The goal of this project is to create an AI agent that leverages OpenAI's GPT-4o-mini model to answer questions based on the content of a large PDF document.

## Problem Statement

You are required to create an AI agent that can:

- Take a PDF document as input.
- Extract relevant information from the document to answer user queries.
- Return answers in a structured JSON format, pairing each question with its corresponding answer.
- Handle scenarios where answers are low confidence and return "Data Not Available" in such cases.

The solution uses OpenAI’s GPT-4o-mini model to process the PDF document and answer questions in natural language.

## Features

- **PDF Text Extraction**: Efficient extraction of text from PDF files.
- **AI-based Question Answering**: Leveraging GPT-4o-mini to answer questions.
- **Confidence Handling**: The program detects low-confidence answers and returns "Data Not Available".
- **Modular Code**: Clean and modular code structure, focusing on maintainability and scalability.


### Prerequisites
- Python 3.8 or above.


### Running the Application
Prepare your PDF document and the list of questions.
Run the script:
- python main.py
