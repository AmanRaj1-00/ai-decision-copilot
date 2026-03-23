def generate_decisions(signals):
    """
    Convert signals into business decisions
    """

    decisions = []

    for signal in signals:

        if signal["type"] == "revenue_drop":
            decision = {
                "action": f"Increase marketing efforts in {signal['region']}",
                "reason": f"Revenue dropped by {signal['change_pct']*100:.1f}% in {signal['region']} region",
                "impact": "Expected revenue recovery of 3-8%",
                "confidence": "Medium",
                "priority": "High" if abs(signal["change_pct"]) > 0.15 else "Medium"
            }

            decisions.append(decision)

    return decisions
