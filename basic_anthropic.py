import os
import sys
from anthropic import Anthropic

def main():
    """
    Entry point of the program.
    Retrieves a question from the command-line arguments and queries the Anthropic API with the provided question.
    """
    # Check if a question is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide a question as a command-line argument.")
        return

    question = " ".join(sys.argv[1:])

    # Set up the Anthropic API client
    client = Anthropic(
        # This is the default and can be omitted
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
    )

    # Query the Claude API with the provided question
    message = client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Hello, Claude",
            }
        ],
        model="claude-3-opus-20240229",
    )

    # Print the generated response
    print(message.content)

if __name__ == "__main__":
    main()
