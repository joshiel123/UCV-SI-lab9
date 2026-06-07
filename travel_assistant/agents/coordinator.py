from google.adk.agents import Agent
from google.adk.tools import ToolContext

from travel_assistant.agents.budget import budget_agent
from travel_assistant.agents.itinerary import itinerary_agent
from travel_assistant.agents.local_culture import local_culture_agent
from travel_assistant.agents.risk import risk_reviewer_agent
from travel_assistant.agents.web_search import web_search_agent


def transfer_to_local_culture(destination: str, tool_context: ToolContext) -> str:
    """Transfer travel planning to the Local Culture Agent.

    Use this tool when the traveler asks about typical dishes, traditional ingredients,
    local customs, social etiquette, or useful phrases/slang for a specific destination.

    Args:
        destination: The travel destination city or region.
        tool_context: Context to perform the agent transfer.
    """
    tool_context.actions.transfer_to_agent = "local_culture_agent"
    return f"Transferred to local_culture_agent for destination: {destination}"


travel_coordinator_agent = Agent(
    name="travel_coordinator_agent",
    model="gemini-2.5-flash",
    description="Coordinates a team of travel agents.",
    instruction="""
You are the coordinator of a travel planning multiagent system.

Your job is to receive the user's travel request and coordinate the specialized agents.

Use the agents as follows:
- Use web_search_agent when the answer requires updated or current information.
- Use itinerary_agent to create day-by-day plans.
- Use budget_agent to estimate basic budget when enough information is available.
- Use risk_reviewer_agent to check travel risks and recommendations.
- Use local_culture_agent (via transfer_to_local_culture) to get info on typical foods,
  customs, etiquette, and local phrases.


Final response format:
1. Brief summary of the request.
2. Updated findings if web search was needed.
3. Suggested itinerary.
4. Referential budget.
5. Risks and recommendations.
6. Local culture, typical food, customs, and useful phrases.
7. Final advice.

Rules:
1. Answer in Spanish.
2. Be clear and structured.
3. Do not invent exact prices, schedules or availability.
4. Tell the user to verify official sources before booking.
5. Keep the response useful for an introductory university laboratory.
""",
    tools=[transfer_to_local_culture],
    sub_agents=[
        web_search_agent,
        itinerary_agent,
        budget_agent,
        risk_reviewer_agent,
        local_culture_agent,
    ],
)


