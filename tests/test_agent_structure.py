from travel_assistant.agent import root_agent


def test_root_agent_name():
    assert root_agent.name == "travel_coordinator_agent"


def test_root_agent_has_sub_agents():
    assert len(root_agent.sub_agents) == 5


def test_sub_agent_names():
    names = {agent.name for agent in root_agent.sub_agents}

    assert "web_search_agent" in names
    assert "itinerary_agent" in names
    assert "budget_agent" in names
    assert "risk_reviewer_agent" in names
    assert "local_culture_agent" in names


