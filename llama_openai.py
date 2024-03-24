from llama_main import main
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings

Settings.llm = OpenAI(temperature=0.2, model="gpt-4")

if __name__ == "__main__":
    main()
