from unittest.mock import MagicMock

from google.adk.tools import ToolContext

from travel_assistant.agents.coordinator import transfer_to_local_culture
from travel_assistant.agents.local_culture import local_culture_agent
from travel_assistant.tools.culture_tools import get_local_culture_info


def test_local_culture_agent_exists():
    assert local_culture_agent.name == "local_culture_agent"
    assert local_culture_agent.model == "gemini-2.5-flash"


def test_get_local_culture_info_cusco():
    result = get_local_culture_info("Cusco")
    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert any("Cuy" in dish for dish in result["typical_dishes"])
    assert any("Pachamama" in custom for custom in result["local_customs"])
    assert any("Allianllachu" in phrase for phrase in result["useful_phrases"])


def test_get_local_culture_info_buenos_aires():
    result = get_local_culture_info("Buenos Aires")
    assert result["status"] == "success"
    assert result["destination"] == "Buenos Aires"
    assert any("Asado" in dish for dish in result["typical_dishes"])
    assert any("mate" in custom for custom in result["local_customs"])
    assert any("Che" in phrase for phrase in result["useful_phrases"])


def test_get_local_culture_info_arequipa():
    result = get_local_culture_info("Arequipa")
    assert result["status"] == "success"
    assert result["destination"] == "Arequipa"
    assert any("Rocoto" in dish for dish in result["typical_dishes"])
    assert any("Misti" in custom for custom in result["local_customs"])
    assert any("diantres" in phrase for phrase in result["useful_phrases"])


def test_get_local_culture_info_paris():
    result = get_local_culture_info("París")
    assert result["status"] == "success"
    assert result["destination"] == "París"
    assert any("Coq au vin" in dish for dish in result["typical_dishes"])
    assert any("Bonjour" in custom for custom in result["local_customs"])
    assert any("Merci" in phrase for phrase in result["useful_phrases"])


def test_get_local_culture_info_default():
    result = get_local_culture_info("New York")
    assert result["status"] == "success"
    assert result["destination"] == "New York"
    assert len(result["typical_dishes"]) == 1
    assert len(result["local_customs"]) == 2
    assert len(result["useful_phrases"]) == 3


def test_transfer_to_local_culture():
    mock_context = MagicMock(spec=ToolContext)
    mock_actions = MagicMock()
    mock_context.actions = mock_actions

    res = transfer_to_local_culture("Arequipa", mock_context)
    assert mock_actions.transfer_to_agent == "local_culture_agent"
    assert "local_culture_agent" in res
