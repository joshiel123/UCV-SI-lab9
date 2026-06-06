from travel_assistant.tools.budget_tools import estimate_trip_budget


def test_estimate_trip_budget_success():
    result = estimate_trip_budget("Cusco", 5, 80)

    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert result["days"] == 5
    assert result["daily_budget_usd"] == 80
    assert result["estimated_total_usd"] == 400


def test_estimate_trip_budget_invalid_days():
    result = estimate_trip_budget("Cusco", 0, 80)

    assert result["status"] == "error"
    assert "days" in result["message"].lower()


def test_estimate_trip_budget_invalid_daily_budget():
    result = estimate_trip_budget("Cusco", 5, 0)

    assert result["status"] == "error"
    assert "daily budget" in result["message"].lower()