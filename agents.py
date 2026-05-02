from groq import Groq
from config import GROQ_API_KEY, MODEL, MAX_TOKENS

client = Groq(api_key=GROQ_API_KEY)

def agent_argue(role, stance, topic, history):
    system = (
        f"You are {role} in a structured debate. "
        f"Your position is: {stance}. Topic: {topic}. "
        "Make a concise, persuasive argument in 3-4 sentences. "
        "Directly counter the previous point if one exists."
    )
    messages = [{"role": "system", "content": system}] + history + \
               [{"role": "user", "content": "Make your argument now."}]
    resp = client.chat.completions.create(
        model=MODEL, messages=messages,
        max_tokens=MAX_TOKENS, temperature=0.8
    )
    return resp.choices[0].message.content.strip()