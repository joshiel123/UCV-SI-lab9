from travel_assistant.tools.risk_tools import assess_basic_travel_risks


def test_assess_basic_travel_risks_for_cusco():
    result = assess_basic_travel_risks("Cusco", "temporada alta")

    assert result["status"] == "success"
    assert len(result["risks"]) >= 1
    assert any("altitude" in risk.lower() or "altura" in risk.lower() for risk in result["risks"])


def test_assess_basic_travel_risks_default_case():
    result = assess_basic_travel_risks("Lima", "normal")

    assert result["status"] == "success"
    assert len(result["risks"]) == 1

def test_assess_basic_travel_risks_rainy_season():
    result = assess_basic_travel_risks("Cusco", "rain")

    assert result["status"] == "success"
    assert len(result["risks"]) >= 1