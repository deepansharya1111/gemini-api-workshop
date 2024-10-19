import google.generativeai as genai
from config import API_KEY

# Configure the API
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text

def confirm_or_edit_prompt(prompt):
    while True:
        print(f"\nCurrent prompt: {prompt}")
        action = input("Press Enter to confirm, or type 'edit' to modify the prompt: ").lower()
        if action == '':
            return prompt
        elif action == 'edit':
            new_prompt = input("Enter the new prompt: ")
            if new_prompt:
                return new_prompt
            print("Prompt cannot be empty. Using the original prompt.")
            return prompt
        else:
            print("Invalid input. Please try again.")

def main():
    print("Text Generation with Gemini API")
    print("-------------------------------")

    # Predefined prompts
    prompts = [
        "Write a short story about a robot learning to paint.",
        "Summarize the key points of climate change in 3 bullet points.",
        "What are the main differences between Python and JavaScript?"
    ]

    for prompt in prompts:
        final_prompt = confirm_or_edit_prompt(prompt)
        print("\nGenerating response...\n")
        response = generate_text(final_prompt)
        print(f"Response:\n{response}\n")
        print("-------------------------------")

    print("All prompts have been processed.")

if __name__ == "__main__":
    main()
