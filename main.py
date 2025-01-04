import openai  # Import the OpenAI library to interact with the GPT model
import json  # Import the JSON library to handle JSON data
from PyPDF2 import PdfReader  # Import the PDF reader to extract text from the PDF

# Enter your actual API key. 
API_KEY = "API KEY"

def extract_pdf_content(file_path): # Function to extract text content from a PDF file
    try:
        reader = PdfReader(file_path) # Using PyPDF2 to read the PDF
        text = []  # List to store text from each page
       
        for page in reader.pages: # Loop through each page and extract text
            text.append(page.extract_text())
        # Join the list into a single string and return the content
        return " ".join(text)
    
    except Exception as e: # If something goes wrong, raise an error with a helpful message
        raise Exception(f"Error extracting content from PDF: {e}")

def answer_questions(pdf_content, questions, api_key): # Function to answer a list of questions using GPT-4o-mini
    openai.api_key = api_key  # Set the OpenAI API key for authentication
    answers = {}  # Dictionary to store the question-answer pairs

    for question in questions: # Loop through each question and ask GPT to generate an answer
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # Use GPT-4o-mini as per the instructions
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Document:\n{pdf_content}\n\nQuestion: {question}"}
                ]
            )
            answer = response["choices"][0]["message"]["content"].strip() # Extract the answer from the response and store it
            answers[question] = answer if answer else "Data Not Available"  # If answer is empty, respond with "Data Not Available"
        
        except Exception as e: # If something goes wrong, capture the error and store it in the answers dictionary
            answers[question] = f"Error: {str(e)}"
   
    return answers  # Return the dictionary containing all answers

def main(): # Main function 
    print("Welcome to the Zania AI Challenge Solution!")
    
    pdf_path = input("Enter the path to the PDF file: ").strip() # The user to input the paths for the PDF file and the questions file
    questions_path = input("Enter the path to the JSON questions file: ").strip()

    # Step 1: Extract content from the PDF
    try:
        print("Extracting content from the PDF...")
        pdf_content = extract_pdf_content(pdf_path)  # Call the extract_pdf_content function
        print("PDF content extracted successfully.")
    
    except Exception as e:  # If there’s an error during PDF extraction, print the error and stop the program
        print(f"Error: {e}")
        return

    # Step 2: Load questions from the JSON file
    try:
        print("Loading questions...")
        with open(questions_path, "r") as q_file:
            questions = json.load(q_file)  # Read the questions from the JSON file
        print("Questions loaded successfully.")
   
    except Exception as e:  # If there’s an error loading the questions, print the error and stop the program 
        print(f"Error: {e}")
        return

    # Step 3: Use GPT to answer the questions based on the PDF content
    print("Answering questions using GPT-4o-mini...")
    answers = answer_questions(pdf_content, questions, API_KEY)  # Call the answer_questions function
    
    # Step 4: Display the answers in a structured JSON format
    print("Answers:")
    print(json.dumps(answers, indent=4))  # Print the answers in a pretty JSON format with indentation

if __name__ == "__main__":
    main()  # Call the main function to start the program

