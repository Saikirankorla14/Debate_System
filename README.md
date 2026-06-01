# Multi-Agent Debate System

A Python-based AI debate system where two agents argue opposite sides of any topic using the **Groq API**, with turn-based rounds, a neutral judge scoring system, and automatic transcript export by using groq api.

---

## Features

- Two AI agents argue opposite sides of any topic they choose
- Turn-based debate with configurable rounds (2–5)
- Neutral judge scores each round on logic, evidence, and persuasion
- Final verdict declaring a winner
- Auto-saves full transcript as a timestamped JSON file
- Rich terminal UI with colored panels and score tables

---

## Project Structure

```
debate-system/
├── debate.py          # Entry point — runs the debate loop
├── agents.py          # agent_argue() — calls Groq, returns argument
├── judge.py           # judge_round() and final_verdict() scoring
├── exporter.py        # export_transcript() — saves debate as JSON
├── display.py         # Rich console printing helpers
├── config.py          # Model, API key, and constants
├── requirements.txt   # Python dependencies
├── .env               # Your Groq API key (never commit this)
├── .env.example       # Template for .env
├── .gitignore         # Ignores .env and transcripts/
└── transcripts/       # Auto-saved debate JSON files
```

---

## Prerequisites

- Python 3.8 or higher
- A Groq API key — get one free at [console.groq.com](https://console.groq.com)

---

## Installation

**1. Clone or download the project**

```bash
git clone https://github.com/your-username/debate-system.git
cd debate-system
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Set up your API key**

Copy the example env file and add your key:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder:

```
GROQ_API_KEY=gsk_your_actual_key_here
```

---

## Usage

Run the debate:

```bash
python debate.py
```

You will be prompted to enter:

```
Debate topic: AI will replace programmers
Agent A stance: Yes, AI will fully replace programmers within 10 years
Agent B stance: No, programmers will always be essential
Rounds (default 3): 3
```

The debate runs turn-by-turn in the terminal with live scoring after each round.

---

## Example Output

```
╭─────────────── Debate Start ───────────────╮
│ Topic: AI will replace programmers         │
╰────────────────────────────────────────────╯

────────────────── Round 1 ──────────────────

╭──── Agent A ────╮
│ AI systems are already writing production  │
│ code, passing coding interviews, and ...   │
╰─────────────────╯

╭──── Agent B ────╮
│ While AI assists developers, it cannot     │
│ replace human creativity and judgment ...  │
╰─────────────────╯

Judge: Agent A made a strong empirical case.
  Round scores → A: 7  B: 6

╭────────── Final Verdict ──────────────╮
│ Agent A wins with a score of 21 vs 18. │
╰───────────────────────────────────────╯

Transcript saved → transcripts/debate_20260502_143012.json
```

---

## Transcript Format

Each debate is saved automatically to the `transcripts/` folder as JSON:

```json
{
  "topic": "AI will replace programmers",
  "transcript": [
    { "round": 1, "agent": "Agent A", "argument": "..." },
    { "round": 1, "agent": "Agent B", "argument": "..." }
  ],
  "final_scores": { "A": 21, "B": 18 },
  "verdict": "Agent A wins by making stronger empirical arguments..."
}
```

---

## Configuration

Edit `config.py` to change defaults:

| Setting | Default | Description |
|---|---|---|
| `MODEL` | `llama-3.3-70b-versatile` | Groq model to use |
| `MAX_TOKENS` | `300` | Max tokens per argument |
| `DEFAULT_ROUNDS` | `3` | Default number of rounds |
| `TRANSCRIPTS_DIR` | `transcripts` | Folder for saved debates |

### Available Groq Models

| Model ID | Speed | Best For |
|---|---|---|
| `llama-3.3-70b-versatile` | Fast | Best quality (recommended) |
| `llama-3.1-8b-instant` | Very fast | Quick/cheap debates |
| `llama-4-scout` | Fast | Long context debates |

---

## Troubleshooting

**`model_decommissioned` error**
The model in `config.py` has been retired by Groq. Update `MODEL` to `llama-3.3-70b-versatile`.

**`AuthenticationError`**
Your API key is missing or incorrect. Check your `.env` file.

**`JSONDecodeError` during judging**
The judge occasionally returns malformed JSON. Re-run the debate — this is rare.

**No module named `groq`**
Run `pip install -r requirements.txt` again.

---

## License

MIT License — free to use, modify, and distribute.
