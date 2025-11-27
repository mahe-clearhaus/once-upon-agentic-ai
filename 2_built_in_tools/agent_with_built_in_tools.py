from strands import Agent
from strands_tools import handoff_to_user, http_request
# TODO: Import the http_request built-in tool
agent = Agent(tools=[handoff_to_user])

agent("""
   Using the website https://en.wikipedia.org/wiki/Dungeons_%26_Dragons tell me the name of the designers of
   Dungeons and Dragons.
    """
    )
