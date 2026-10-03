import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function
import json
import sys


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise ValueError("API key not found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

for _ in range(20):

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=available_functions
    )
    

    if response.usage is None:
        raise RuntimeError("No response")
    elif args.verbose is True:
        print(f"User prompt: {args.user_prompt}") 
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    message = response.choices[0].message
    
    messages.append(message)

    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, args.verbose)
            messages.append(result_message)
            if not result_message["content"]:
                raise RuntimeError("Content is empty")
            if args.verbose:
                print(f"-> {result_message['content']}")
    else:
        print(response.choices[0].message.content)
        break
else:
    print("Exceeded attempt limit...")
    sys.exit(1)
    
    
def main():
    print("Hello from llm-project!")


if __name__ == "__main__":
    main()
