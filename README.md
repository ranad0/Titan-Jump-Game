# Titan Jump

Titan Jump is a simple 2D arcade jumping game built with Python and Pygame.  
The game is inspired by the anime *Attack on Titan*, where the player controls Levi, jumps between platforms, avoids titans, and tries to achieve the highest score.

> This is a fan-made educational project and is not affiliated with or endorsed by Attack on Titan.

## Features

- Pygame-based 2D gameplay
- Jumping platform mechanics
- Moving platforms after reaching a higher score
- Enemy spawning after score progression
- Background music and sound effects
- High score saved locally in `score.txt`

## Project Structure

```text
titan-jump/
├── assets/
│   ├── Levi_tell_Erwin_to_leave_his_dream_and_die.mp3
│   ├── gameover_img.jpg
│   ├── levi2.png
│   ├── season 4 opening.mp3
│   ├── stone.png
│   ├── sword.mp3
│   ├── swordjump.wav
│   ├── titan.png
│   └── wallbg.png
├── main.py
├── requirements.txt
├── score.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer
- Pygame

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/titan-jump.git
cd titan-jump
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the game:

```bash
python main.py
```

## Controls

- Left Arrow: Move left
- Right Arrow: Move right
- Space: Restart after game over

## Credits

Created as a Python/Pygame game project by:

- Ranad Jamal Oweis
- Shatha Bassam Arar
