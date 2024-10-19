import google.generativeai as genai
from config import API_KEY
from PIL import Image
import os

# Configure the API
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def process_input(user_input, chat):
    if user_input.lower().startswith('image:'):
        image_path = user_input[6:].strip()
        if os.path.exists(image_path):
            image = Image.open(image_path)
            chat_response = chat.send_message(image)
            return chat_response.text
        else:
            return "Image file not found. Please provide a valid path."
    else:
        chat_response = chat.send_message(user_input)
        return chat_response.text

def multimodal_chat():
    print("Welcome to the Multimodal Chat with Gemini API")
    print("You can type text or enter 'image: [path_to_image]' to send an image.")
    print("Type 'quit' to end the conversation.")
    print("-------------------------------")

    chat = model.start_chat(history=[])

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        try:
            response = process_input(user_input, chat)
            print("Gemini:", response)
            print("-------------------------------")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    print("Chat ended. Thank you for using the Multimodal Chat!")

if __name__ == "__main__":
    multimodal_chat()
