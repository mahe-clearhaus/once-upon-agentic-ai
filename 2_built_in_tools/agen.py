from strands import Agent
from strands_tools import http_request, handoff_to_user
# TODO: Import the http_request built-in tool


# agent = Agent(tools=[http_request, handoff_to_user])
agent = Agent(tools=[ handoff_to_user, http_request])


# Request user input and continue
response = agent.tool.handoff_to_user(
    message="I need your approval to proceed. Type 'yes' to confirm.",
    breakout_of_loop=False
)

# Complete handoff to user (stops agent execution)
agent.tool.handoff_to_user(
    message="Task completed. Please review the results.",
    breakout_of_loop=True
)


agent("""
   Using the website https://en.wikipedia.org/wiki/Dungeons_%26_Dragons tell me the name of the designers of
   Dungeons and Dragons.
    """
    )
