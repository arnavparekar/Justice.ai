import os
import pytesseract
import openpyxl
from pdf2image import convert_from_path
from PIL import Image
import google.generativeai as genai

# Configure tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Excel setup
output_file = "C:/Users/Nikhil/Downloads/case_summaries.xlsx"
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['File Name', 'Summary', 'Genre', 'Outcome'])

# Configure Gemini API key
genai.configure(api_key="AIzaSyCw88j4W0qh78KSWiVdYz8fgoX3wK2H8vw")


model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    print(f"Extracting text from: {pdf_path}")
    images = convert_from_path(pdf_path, poppler_path="C:/Users/Nikhil/Downloads/Release-24.07.0-0/poppler-24.07.0/Library/bin")
    extracted_text = ""

    for i, image in enumerate(images):
        print(f"Processing page {i + 1} of PDF: {pdf_path}")
        text = pytesseract.image_to_string(image)
        extracted_text += text

    if extracted_text.strip() == "":
        print(f"Warning: No text extracted from {pdf_path}")
    else:
        print(f"Text successfully extracted from {pdf_path}")

    return extracted_text

def analyze_text(text):
    try:
        print("Sending text to Generative AI for analysis...")
        
        # Create the prompts for summarization, genre, and outcome
        prompt_summary = text + " Summarize the above text in a few sentences."
        prompt_genre = text + " What is the genre of this case? for eg (Labour Matters,Rent Matters,Direct Taxes Matters,Indirect Taxes Matters,Land Acquisition and Requisition Matters,Service Matters,Academic Matters,Election Matters,Company Law, MRTP, TRAI, SEBI, IDRAI & RBI,Arbitration Matters,Compensation Matters,Habeas Corpus,Criminal Matters,Appeal Against Orders Of Statutory Bodies,Divorce and Child Custody Matters,Inter caste Marriage Matters,Religious & Charitable Endowments,Mercantile Laws, Commercial Transactions Including Banking)"
        prompt_outcome = text + " What is the outcome of this legal case ? (in a couple of sentences)"

        # Get responses from the model
        summary_response = model.generate_content([prompt_summary])
        genre_response = model.generate_content([prompt_genre])
        outcome_response = model.generate_content([prompt_outcome])
        
        # Extract text from responses
        print(summary_response.text)
        print(genre_response.text)
        print(outcome_response.text)

        print("Analysis completed successfully!")

        return summary_response.text, genre_response.text, outcome_response.text

    except Exception as e:
        print(f"Error during text analysis: {e}")
        return "Error", "Error", "Error"



# Process all PDFs in a folder
def process_pdfs(pdf_folder):
    for pdf_file in os.listdir(pdf_folder) :
        if pdf_file.endswith(".PDF") or pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            print(f"Processing PDF: {pdf_path}")

            # Extract text from the PDF
            extracted_text = extract_text_from_pdf(pdf_path)

            # Check if extracted text is not empty
            if extracted_text.strip() == "":
                print(f"Skipping {pdf_path} as no text was extracted.")
                continue

            # Analyze the text using Generative AI
            summary, genre, outcome = analyze_text(extracted_text)

            # Append results to Excel
            ws.append([pdf_file, summary, genre, outcome])
            print(f"Results added to Excel for: {pdf_file}")

    print("All PDFs processed.")

# Main function
if __name__ == "__main__":
    pdf_folder = "C:/Users/Nikhil/Nikhil Data/Coding/Projects/IBM' 24/Justice.ai/cases"  # Set the folder containing your PDFs
    print(f"Starting PDF processing in folder: {pdf_folder}")

    if not os.path.exists(pdf_folder):
        print(f"Error: The folder {pdf_folder} does not exist.")
    else:
        process_pdfs(pdf_folder)
    
    # Save the Excel file
    print(f"Saving results to {output_file}")
    wb.save(output_file)
    print(f"Results saved in {output_file}")
