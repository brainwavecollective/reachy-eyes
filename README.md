# Reachy Mini Eyes

Control interface for Reachy Mini Eyes. Automatically discovered hardware that gives your Reachy Mini robot fully controllable LED eyes.  

<img src="media/ReachyMiniEyes.png" style="max-width:50%; height:auto;" alt="A cute robot named Reachy Mini with colorful glowing eyes">

> [!NOTE]
> This is an experimental community project that is not affiliated with or endorsed by Pollen Robotics.

## Quick Demo - START HERE

You can run these straight out of the box, even before installing into the robot. Just plug in the USB and go.

**Get the code:**
```bash
git clone https://github.com/brainwavecollective/reachy-eyes.git
cd reachy-eyes
```

**Run the demos:**  
```bash
# Option 1: Manual installation
pip install pyserial
python demos/demo_all_the_things.py

# Option 2: Automatically pull dependencies with your favorite environment manager
uv run demos/demo_all_the_things.py
```

Any of the example files in `demos/` can be run individually. `demo_all_the_things.py` simply cycles through everything available.

## Repository Structure
```
reachy-eyes/
├── demos/              # Standalone demo scripts
│   ├── _runner.py      # Demo framework (handles imports & cleanup)
│   ├── *.py            # Various demonstrations 
│
├── media/              # Misc. assets 
│
├── reachy_eyes/        # Main component package
│   ├── __init__.py     # Component factory & exports
│   ├── defaults.py     # Default configuration values, set elsewhere
│   ├── device.py       # Low-level serial communication
│   ├── eyes.py         # High-level API (ReachyEyes class) and creative implementations
│   └── protocol.py     # Protocol constants (Color, Effect, Eye, Config)
│
├── pyproject.toml      # Package metadata & dependencies
├── INSTALLATION.md     # Instructions for installing the physical eye module
└── README.md           # This file
```

## Installation

This section covers software. The first step is to [Install the Hardware into your Reachy](INSTALLATION.md)

All of the standard approaches will work, you just need to point to this repo (PyPi coming soon!).

```bash
# HTTPS pip
pip install git+https://github.com/brainwavecollective/reachy-eyes.git

# SSH pip
pip install git+git@github.com:brainwavecollective/reachy-eyes.git

# HTTPS uv
uv run pip install git+https://github.com/brainwavecollective/reachy-eyes.git

# SSH uv
uv run pip install git+git@github.com:brainwavecollective/reachy-eyes.git
```

## Programmatic Access 

Use the API for app integration 

```python
import reachy_eyes
eyes = reachy_eyes.create()
```

### Color Controls
```python
eyes.set_color(Color.RED)
eyes.set_color(Color.BLUE, duration=1.5)
eyes.set_color("GREEN", eye="LEFT")
eyes.set_color(Color.GREEN, eye=Eye.LEFT)
eyes.off()
```

Available: `WHITE`, `RED`, `GREEN`, `BLUE`, `AMBER`, `CYAN`, `MAGENTA`  

COMING SOON: Full indexed RGB will be published in the next firmware update (Contact me if you want this upgrade before you install the eyes... the eyes need to be removed from the robot for firmware updates).

### Built-In Effects
```python
eyes.blink()
eyes.ack()
eyes.startle()
```

### State Modification
```python
eyes.set_intensity(0.4)
eyes.set_energy(0.6)
```

### Autonomous Background Behavior
```python
eyes.enable_blinking()
eyes.disable_blinking()
```

---

## Contributing
This project is in active development. Feel free to open issues for bugs, feature requests, or to propose changes.

---

## Robot Component Integration

It is not difficult to interact with the eyes directly, but I'm optimistic that these eyes can be driven as part of a first-class component runtime for Reachy Mini robots. I've proposed an approach that will take some time to work through with the Pollen team. You can check [PR #755](https://github.com/pollen-robotics/reachy_mini/pull/755) for current status and join the conversation. If you have thoughts related to the solution, please comment!

--- 

## Status
This project is in early development and actively maintained (Q1 2026).

**Licensing:** Decisions will be made as the project matures.  
**Usage:** Feel free to view and reference this code for personal learning.  
**Commercial/Partnership/Distribution:** Please [email Daniel](mailto:daniel@brainwavecollective.ai)