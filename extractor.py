import os
import easyocr
from PIL import Image
from openai import OpenAI
from dotenv import load_dotenv

# load env variables
load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1", # may change to https://api.openai.com/v1
    api_key=os.getenv("API_KEY"), # GROQ API key , replace with OpenAI API key
)

def extract_text_with_easyocr(image_path, lang_list=None):
    """
    Extracts text from an image using EasyOCR.
    Args:
        image_path (str): Path to the image file.
        lang_list (list, optional): List of languages for OCR (default is English).
    Returns:
        str: Extracted text from the image.
    """
    reader = easyocr.Reader(lang_list if lang_list else ['en', 'ja'], gpu=False)
    
    # Perform OCR on the image
    results = reader.readtext(image_path, detail=0)
    
    # Combine results into a single string
    extracted_text = "\n".join(results)
    return extracted_text

def analyze_table_with_gpt(ocr_text):
    """
    Analyzes the OCR-extracted text using OpenAI's GPT model.
    Args:
        ocr_text (str): Text extracted from the image.
    Returns:
        str: GPT-processed interpretation of the data.
    """

    # Call OpenAI GPT API
    response = client.chat.completions.create(
        model="llama3-8b-8192", # may change to use OpenAI's GPT-3.5 model
        messages=[
            {"role": "system", "content": "The following text has been extracted from an image of a table. The table may contain data in japanese or english."},
            {"role": "user", "content": "Analyze the table columns and rows and provide highlight any trends, patterns, or key observations."},
            {"role": "user", "content": ocr_text}
        ],
        max_tokens=1024,
        temperature=0.7,
    )
        
    return response.choices[0].message.content

if __name__ == "__main__":
    image_path = "image.png"  # Replace with the actual path to your image

    # Extract text from the image using EasyOCR
    print("Extracting text from image using EasyOCR...")
    extracted_text = extract_text_with_easyocr(image_path, ['en', 'ja'])
    print("\nExtracted Text:")
    print(extracted_text)

    # Analyze the extracted data using ChatGPT
    print("\nAnalyzing extracted data with GPT...")
    analysis_result = analyze_table_with_gpt(extracted_text)
    print("\nGPT Analysis:")
    print(analysis_result)
