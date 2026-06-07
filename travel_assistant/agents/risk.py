from google.adk.agents import Agent

from travel_assistant.tools.risk_tools import assess_basic_travel_risks

risk_reviewer_agent = Agent(
    name="risk_reviewer_agent",
    model="gemini-2.5-flash",
    description="Reviews travel risks and practical recommendations.",
    instruction="""
You are a travel risk reviewer.

Your task is to identify practical travel risks.
Consider:
- weather
- altitude
- transport delays
- high season
- safety
- documentation
- health precautions

Rules:
1. Be practical and concise.
2. Avoid causing unnecessary fear.
3. Provide preventive recommendations.
4. Use the available tool for basic risk checks when destination and season are available.
""",
    tools=[assess_basic_travel_risks],
)

