def assess_basic_travel_risks(destination: str, season: str) -> dict:
    """Return basic travel risks based on destination and season.

    This is intentionally simple for an introductory laboratory.
    """
    destination_normalized = destination.lower().strip()
    season_normalized = season.lower().strip()

    risks = []

    if "cusco" in destination_normalized or "machu picchu" in destination_normalized:
        risks.append("Consider altitude sickness prevention and gradual acclimatization.")

    if "rain" in season_normalized or "lluvia" in season_normalized:
        risks.append("Carry waterproof clothing and check road or trail conditions.")

    if "high" in season_normalized or "alta" in season_normalized:
        risks.append("Book hotels, trains and entrance tickets in advance.")

    if not risks:
        risks.append(
    "Check weather, local transport, "
    "health requirements and travel documentation."
    )

    return {
        "status": "success",
        "destination": destination,
        "season": season,
        "risks": risks,
    }