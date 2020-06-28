# EXITPYTH

Python clone of exit path.

This project tries to copy the gameplay of the platformer exit path in another language than flash.

Of course it's very ugly: my first glance at pygame, plus trying to copy a game full of glitches

# Run:

To run the game, you need python3 and pygame installed.

On linux: 
```pip install pygame```

Just run main.py from the game directory to launch the game:

```python main.py```

# Log:

- 28/06:
  - Levels with blocks only and loader
  - Basic GUI
  - Added simple moving camera
  - Respawn when outside of level borders
  - Copy/pasted physics engine, but wrong hitboxes (thus wrong legit distances and unusual glitches)