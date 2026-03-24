def generate_ai_explanation(decision):
    try:
        import ollama

        prompt = f"""
        Action: {decision['action']}
        Reason: {decision['reason']}
        """

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    except:
        return "AI insight unavailable (requires Ollama setup)"
