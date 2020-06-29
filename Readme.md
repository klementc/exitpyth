# EXITPYTH

Python clone of exit path.

This project tries to copy the gameplay of the platformer exit path in another language than flash.

Of course it's very ugly: my first glance at pygame, plus trying to copy a game full of glitches

# Run:

To run the game, you need python3, pyperclip and pygame installed.

On linux: 
```bash
pip install pygame
pip install pyperclip
```


Just run main.py from the game directory to launch the game:

```
python main.py
```

# How to play? (as of june 28th)

Move: arrows

Flow: shift (inf flow for now)

Change level: `a` and `z`

Enter commands: `t` then command (none for now, but soon :)) 

# Important TODO

- player hitbox is wrong
- spikes hitbox is wrong

# Log:

- v0.1
  - Sprite color different when jump available and when not
  - Added checkpoints
  - Added spikes
  - Added half blocks
  - Example of level codes
  - Type a level code (not epyck format for now) in the command input and enter to load it
  - Press `a` and `z` to load the 2 available levels
  - Enter text by pressing t and return when command typed
  - Levels with blocks only and loader
  - Basic GUI
  - Added simple moving camera
  - Respawn when outside of level borders
  - Copy/pasted physics engine, but wrong hitboxes (thus wrong legit distances and unusual glitches)
  - Simple sprites