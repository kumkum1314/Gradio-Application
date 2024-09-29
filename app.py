import gradio as gr
from PIL import Image
import pytesseract

# OCR function using Pytesseract
def ocr_process(image):
    text = pytesseract.image_to_string(image, lang='eng+hin')  # Supports English and Hindi
    return text

# Function to search keywords
def search_text(extracted_text, keyword):
    if keyword in extracted_text:
        start_index = extracted_text.index(keyword)
        return f"Keyword found at position {start_index}."
    return "Keyword not found."

# Build the interface
with gr.Blocks() as demo:
    image = gr.Image(type="pil", label="Upload Image", elem_id="image_input")  # Upload image with id
    keyword = gr.Textbox(label="Enter keyword to search", elem_id="keyword_input")  # Keyword input with id
    output_text = gr.Textbox(label="Extracted text", interactive=False, elem_id="output_text")  # Show extracted text with id
    search_result = gr.Label(label="Search result", elem_id="search_result")  # Search result with id

    def process(image, keyword):
        if image is None:
            return "Please upload a valid image.", "No search performed."
        
        text = ocr_process(image)  # Extract text
        found_message = search_text(text, keyword)  # Search for the keyword
        return text, found_message

    btn = gr.Button("Submit")
    btn.click(process, inputs=[image, keyword], outputs=[output_text, search_result])

# Fallback to 7860 if not set
demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
