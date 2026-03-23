import ollama


def generate_ai_explanation(decision):
    """
    Generate AI-based business explanation using Llama3
    """

    prompt = f"""
You are a business analyst.

Given:
Action: {decision['action']}
Reason: {decision['reason']}

Provide:
1. Why this might be happening
2. One strategic suggestion
3. One potential risk

Keep it concise.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

