import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="Enter question")
args = parser.parse_args()

if api_key == None:
    raise RuntimeError("API Key not found or loaded")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=args.user_prompt,
)
# print(
#     f"Prompt tokens: {response.prompt_token_count}\nResponse tokens: {response.candidates_token_count}"
# )
print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)
print(response.text)
# testing change


def main():
    print("Hello from bdev-ai-agent!")


if __name__ == "__main__":
    main()
