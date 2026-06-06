from google.adk.agents import Agent

from travel_assistant.tools.budget_tools import estimate_trip_budget

budget_agent = Agent(
    name="budget_agent",
    model="gemini-2.0-flash",
    description="Estimates basic travel budgets.",
    instruction="""
You are a travel budget advisor.

Your task is to estimate a basic travel budget.
Use the available tool when the user provides destination, number of days and daily budget.

Rules:
1. Explain that the result is referential.
2. Separate costs into lodging, food, transport and activities when possible.
3. Do not present estimates as final prices.
4. Recommend checking updated prices before purchasing.
""",
    tools=[estimate_trip_budget],
)

