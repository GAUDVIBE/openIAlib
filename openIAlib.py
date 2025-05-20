from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="sk-6730797685e8475392411913b3a9bb04")  # Replace with your actual API key

def call_deepseek_reasoner(prompt):
    try:
        response = client.chat.completions.create(
            model="deepseek-reasoner",  # Verify the correct model name
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  # Adjust for creativity (0-1)
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling API: {e}"

# Usage
if __name__ == "__main__":
    print("Welcome to DeepSeek Reasoner! Type your prompt below (or 'exit' to quit).")
    while True:
        user_prompt = input("\nYour prompt: ")
        if user_prompt.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        answer = call_deepseek_reasoner(user_prompt)
        print("\nDeepSeek Reasoner's Response:")
        print(answer)