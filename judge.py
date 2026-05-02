import json
from groq import Groq
from config import GROQ_API_KEY, MODEL

client = Groq(api_key=GROQ_API_KEY)

def judge_round(topic, arg_a, arg_b):
    prompt = (
        f"Topic: {topic}\nAgent A: {arg_a}\nAgent B: {arg_b}\n\n"
        "Score each 1-10 on logic, evidence, persuasion. "
        'Reply ONLY with JSON: {"score_a": int, "score_b": int, "reasoning": "str"}'
    )
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200, temperature=0.3
    )
    return json.loads(resp.choices[0].message.content.strip())

def final_verdict(topic, transcript, score_a, score_b):
    summary = "\n".join([f"{t['agent']}: {t['argument']}" for t in transcript])
    prompt = (
        f"Topic: {topic}\nDebate:\n{summary}\n\n"
        f"Scores — A: {score_a}, B: {score_b}. "
        "Write a 2-sentence verdict declaring the winner and why."
    )
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return resp.choices[0].message.content.strip()