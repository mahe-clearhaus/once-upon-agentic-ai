from strands import Agent
from strands_tools import current_time

agent = Agent(
    tools=[current_time]
)
response = agent("What is the time in Berlin?")
print(response)
