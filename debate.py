from agents import agent_argue
from judge import judge_round, final_verdict
from exporter import export_transcript
from display import (print_intro, print_round, print_argument,
                     print_scores, print_verdict)
from config import DEFAULT_ROUNDS

def run_debate(topic, stance_a, stance_b, rounds=DEFAULT_ROUNDS):
    history, transcript = [], []
    score_a, score_b = 0, 0
    print_intro(topic)

    for r in range(1, rounds + 1):
        print_round(r)

        arg_a = agent_argue("Agent A", stance_a, topic, history)
        print_argument("Agent A", arg_a, "green")
        history.append({"role": "assistant", "content": f"Agent A: {arg_a}"})
        transcript.append({"round": r, "agent": "Agent A", "argument": arg_a})

        arg_b = agent_argue("Agent B", stance_b, topic, history)
        print_argument("Agent B", arg_b, "red")
        history.append({"role": "assistant", "content": f"Agent B: {arg_b}"})
        transcript.append({"round": r, "agent": "Agent B", "argument": arg_b})

        scores = judge_round(topic, arg_a, arg_b)
        score_a += scores["score_a"]
        score_b += scores["score_b"]
        print_scores(scores["reasoning"], scores["score_a"], scores["score_b"])

    verdict = final_verdict(topic, transcript, score_a, score_b)
    print_verdict(verdict, score_a, score_b)

    saved = export_transcript(topic, transcript, score_a, score_b, verdict)
    print(f"\nTranscript saved → {saved}")

if __name__ == "__main__":
    topic    = input("Debate topic: ")
    stance_a = input("Agent A stance: ")
    stance_b = input("Agent B stance: ")
    rounds   = int(input(f"Rounds (default {DEFAULT_ROUNDS}): ") or DEFAULT_ROUNDS)
    run_debate(topic, stance_a, stance_b, rounds)