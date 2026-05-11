# Titan Jump

Titan Jump is a 2D endless vertical platformer game built with Python and Pygame.  
Its gameplay is similar to classic vertical jumping games like *Doodle Jump*, where the player jumps between platforms and tries to reach the highest score possible. The project was developed as an educational game based on a PyGame tutorial, then customized with an *Attack on Titan*-inspired theme where the player controls Levi, avoids titans, and continues climbing as the difficulty increases.

> This is a fan-made educational project and is not affiliated with or endorsed by *Attack on Titan*, Coding With Russ, or any original asset creators.

## Features

- Pygame-based 2D gameplay
- Jumping platform mechanics
- Moving platforms after reaching a higher score
- Enemy spawning after score progression
- Background music and sound effects
- High score saved locally in `score.txt`

## Demo Video

Watch a short gameplay recording here:

[Gameplay Demo](https://drive.google.com/file/d/1e5Q1aVsBVhjd46ZduImDbFSscbgzaCMq/view?usp=sharing)

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

Created as a Python/Pygame educational game project by:

- Ranad Oweis
- Shatha Arar

This project was developed with guidance from the PyGame Endless Vertical Platformer tutorial by Coding With Russ.

- Tutorial: https://www.youtube.com/watch?v=5FMPAt0n3Nc&list=PLjcN1EyupaQlBSrfP4_9SdpJIcfnSJgzL
- Original Jumpy project by Coding With Russ: https://github.com/russs123/Jumpy

The original Jumpy project is licensed under the MIT License.  
This project adapts the base vertical platformer concept and customizes it with an *Attack on Titan*-inspired theme, characters, enemies, sounds, scoring behavior, and visual direction.

This is a fan-made educational project and is not affiliated with or endorsed by *Attack on Titan*, Coding With Russ, or any original asset creators.

## Contributors

- [Ranad Oweis](https://github.com/ranad0)
- [Shatha Arar](https://github.com/shathaarar)

## License

This project is based on and adapted from the original Jumpy project by Coding With Russ, which is licensed under the MIT License.

Original project: https://github.com/russs123/Jumpy
