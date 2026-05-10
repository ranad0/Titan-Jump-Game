# Titan Jump

Titan Jump is a simple 2D arcade jumping game built with Python and Pygame.  
The game was developed as an educational project based on an endless vertical platformer tutorial, then customized with an *Attack on Titan*-inspired theme where the player controls Levi, jumps between platforms, avoids titans, and tries to achieve the highest score.

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
git clone https://github.com/ranad0/Titan-Jump-Game.git
cd Titan-Jump-Game
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

- Ranad Oweis
- Shatha Arar

This project was inspired by the anime *Attack on Titan* and was created for educational purposes only.

The base gameplay structure was learned and developed with guidance from the PyGame Endless Vertical Platformer tutorial by Coding With Russ:

- Tutorial: https://www.youtube.com/watch?v=5FMPAt0n3Nc&list=PLjcN1EyupaQlBSrfP4_9SdpJIcfnSJgzL
- Original project by Coding With Russ: https://github.com/russs123/Jumpy

We customized and expanded the project by adding our own theme, characters, enemy concept, assets, sounds, scoring logic, and Attack on Titan-inspired visual direction.

This is a fan-made educational project and is not affiliated with or endorsed by *Attack on Titan*, Coding With Russ, or any original asset creators.

## Contributors

- [Ranad Oweis](https://github.com/ranad0)
- [Shatha Arar](https://github.com/shathaarar)
