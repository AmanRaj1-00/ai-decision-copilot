def generate_ai_explanation(decision):
    """
    Simulated AI explanation (no API needed)
    """

    region = decision["action"].split()[-1]

    explanation = f"""
Revenue decline in {region} suggests potential drop in customer demand or market competition.

Strategic suggestion:
Focus on targeted promotions and customer engagement campaigns in {region}.

Risk:
Increased marketing spend may not immediately convert to revenue if underlying demand is weak.
"""

    return explanation.strip()
