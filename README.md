# Asteroids

A classic Asteroids clone built with [pygame](https://www.pygame.org/). Fly a ship, dodge asteroids, and blast them apart — each large asteroid splits into smaller ones when shot.

## Requirements

- **Python 3.13+**
- [**uv**](https://docs.astral.sh/uv/) (recommended) — handles the virtualenv and dependencies for you

The only runtime dependency is `pygame==2.6.1`.

## Setup & Run

### With uv (recommended)

```bash
# Install dependencies into a managed virtualenv
uv sync

# Start the game
uv run main.py
```

### With plain pip

```bash
# Create and activate a virtualenv
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
pip install pygame==2.6.1

# Start the game
python main.py
```

A `1280x720` window will open and the game starts immediately.

## Controls

| Key     | Action          |
| ------- | --------------- |
| `W`     | Thrust forward  |
| `S`     | Thrust backward |
| `A`     | Rotate left     |
| `D`     | Rotate right    |
| `Space` | Shoot           |

Touching an asteroid ends the game (`Game over!` prints to the terminal). Close the window to quit.

## Tuning

Gameplay values (screen size, speeds, asteroid spawn rate, shot cooldown, etc.) live in `constants.py` — tweak them to change how the game feels.

## Logging

While running, the game writes telemetry to `game_state.jsonl` (per-frame state) and `game_events.jsonl` (hits and shots). Both are gitignored.
