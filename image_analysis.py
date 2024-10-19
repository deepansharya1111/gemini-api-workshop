import google.generativeai as genai
from config import API_KEY
from PIL import Image

# Configure the API
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def analyze_image(image_path, prompt):
    image = Image.open(image_path)
    response = model.generate_content([prompt, image])
    return response.text

def main():
    print("Image Analysis with Gemini API")
    print("-------------------------------")

    # Make sure to replace 'path/to/your/image.jpg' with an actual image path on your system
    image_path = 'thinking.png'

    # Example 1: Image description
    prompt1 = "Describe this image in detail."
    print(f"Prompt: {prompt1}")
    print(f"Response:\n{analyze_image(image_path, prompt1)}\n")

    # Example 2: Object detection
    prompt2 = "List the main objects you can see in this image."
    print(f"Prompt: {prompt2}")
    print(f"Response:\n{analyze_image(image_path, prompt2)}\n")

    # Example 3: Emotion detection
    prompt3 = "Describe the emotions or mood conveyed by this image."
    print(f"Prompt: {prompt3}")
    print(f"Response:\n{analyze_image(image_path, prompt3)}\n")

if __name__ == "__main__":
    main()
