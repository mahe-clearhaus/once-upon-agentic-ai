# TODO: Add debug logging to see what your agent is thinking

# TODO: Create the agent with the following system prompt: "You are a game master for a Dungeon & Dragon game"

# TODO: Summon your agent with a basic incantation such as "Hi, I am an advanturer ready for adventure!"
from strands import Agent
import logging

# Configure the root strands logger
logging.getLogger("strands").setLevel(logging.INFO)

# Add a handler to see the logs
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s", 
    handlers=[logging.StreamHandler()]
)


agent = Agent(
    system_prompt=(
        "You are a game master for a Dungeon & Dragon game"
    )
)


agent = Agent()

print(agent.model.config)

response = agent("Hi, I am an advanturer ready for adventure!")
