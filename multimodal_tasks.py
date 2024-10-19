import google.generativeai as genai
from config import API_KEY
from PIL import Image

# Configure the API
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def multimodal_task(image_path, prompt):
    image = Image.open(image_path)
    response = model.generate_content([prompt, image])
    return response.text

def main():
    print("Multimodal Tasks with Gemini API")
    print("--------------------------------")

    # Make sure to replace 'path/to/your/image.jpg' with an actual image path on your system
    image_path = 'thinking.png'

    # Example 1: Image captioning with a specific theme
    prompt1 = "Create a funny caption for this image related to technology."
    print(f"Prompt: {prompt1}")
    print(f"Response:\n{multimodal_task(image_path, prompt1)}\n")

    # Example 2: Visual question answering
    prompt2 = "What time of day does this image appear to be taken? Explain your reasoning."
    print(f"Prompt: {prompt2}")
    print(f"Response:\n{multimodal_task(image_path, prompt2)}\n")

    # Example 3: Image-based storytelling
    prompt3 = "Create a short story inspired by this image. The story should be about an unexpected adventure."
    print(f"Prompt: {prompt3}")
    print(f"Response:\n{multimodal_task(image_path, prompt3)}\n")

if __name__ == "__main__":
    main()
