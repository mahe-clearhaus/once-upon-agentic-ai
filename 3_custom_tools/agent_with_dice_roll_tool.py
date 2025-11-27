from strands import Agent
# from strands_tools import tool
from strands import tool
# TODO: Import 'tool' from strands to use the @tool decorator


# example
# @tool
# def get_user_location() -> str:
#     """Get the user's location."""

#     # Implement user location lookup logic here
#     return "Seattle, USA"


# TODO: Add the decorator to transform your function into a tool
@tool
def roll_dice(faces: int = 6) -> int:

    # TODO: Modify the docstring with the args and return informations
    """
    🎲 Roll a dice with a specified number of faces.

    Args:
        int faces: the number of faces on the die
    """

    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)



dice_master = Agent(
    # TODO: Add the tool to the agent
    tools=[roll_dice],
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in D&D adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about D&D mechanics, ability scores, and can help players with character creation.
    When rolling ability scores, remember the traditional method: roll 4d6, drop the lowest die."""
)

# Test your dice master's abilities
dice_master("Help me create a new D&D character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")
