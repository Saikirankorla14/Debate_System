import json, os, datetime
from config import TRANSCRIPTS_DIR

def export_transcript(topic, transcript, score_a, score_b, verdict):
    os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{TRANSCRIPTS_DIR}/debate_{ts}.json"
    data = {
        "topic": topic,
        "transcript": transcript,
        "final_scores": {"A": score_a, "B": score_b},
        "verdict": verdict
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    return filename