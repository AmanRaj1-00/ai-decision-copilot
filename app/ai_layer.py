def generate_ai_explanation(decision, model_mode="local"):
    prompt = f"""
You are a business analyst.

Action: {decision['action']}
Reason: {decision['reason']}

Explain:
1. Why this happened
2. One strategic suggestion
3. One risk
"""

    try:
        import ollama

        # Choose model
        if model_mode == "cloud":
            model = "kimi-k2.5:cloud"
        else:
            model = "qwen2.5-coder:7b"

        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"AI unavailable: {str(e)}"
