from llama_main import main
from llama_index.llms.anthropic import Anthropic
from llama_index.core import Settings

# To customize your API key, do this
# otherwise it will lookup ANTHROPIC_API_KEY from your env variable
# Settings.llm = Anthropic(api_key="<api_key>")
Settings.llm = Anthropic(model="claude-3-opus-20240229")

if __name__ == "__main__":
    main()
