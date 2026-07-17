# Reachy Eyes — Assembly

> [!NOTE]
> This assembly guide is incomplete. 

This is a WIP which will be built out as a detailed guide, but I am waiting to put on the polish until a few people can confirm parts availability and general workflow. I need collaborators! Feel free to [open a GitHub issue](https://github.com/brainwavecollective/reachy-eyes/issues) to get in touch with any questions or support along the way.

## Before You Begin

This guide assumes you are comfortable with basic soldering and related efforts. If you haven't soldered before this project is probably not for you. Anything is possible, but not recommended as it will be quite ambitious for a first project.

### Tools Required

- Soldering iron with a fine tip
- Solder (63/37 or 60/40, rosin core recommended)
- Flux paste, self-cleaning / no-clean recommended
- Wire strippers
- Flush cutters
- Needle Nose Pliers (or similar)

### If You Are Doing the recommended but optional SMD Level Shifter

The SOT-23-5 IC can be hand soldered with the right tip and enough patience,  but, if you already have an SMD setup (hotplate, reflow oven, or similar) then this will be easy. This guide represents the hard end of what's possible without specialized equipment. A steady hand, a fine tip, and good magnification are absolute requirements.

- Extremely fine soldering tip (0.2mm or similar)
- Hands-free magnification (e.g., magnifying lamp, or digital microscope)
- Flux (no-clean solder paste or extremely fine low melt solder is recommended)

If you have a hotplate or reflow setup, the process is faster and more reliable, but those workflows are outside the scope of this guide. If you do not already own that equipment DO NOT source that equipemnt just for this project... it's only worth it if you are already planning on doing a ton of SMD work in the future (which is not true for most people).

### Nice to Have

- Multimeter (various continuity and voltage checks)
- Magnifying lamp or other hands-free maginfication and lighting
- Helping hands / PCB vise

### Before You Start

- Electronics sourced and on hand → [Electronics.md](./Electronics.md)
- 3D parts printed → [3D.md](./3D.md)

---

> [!NOTE]
> This guide is actively being validated. If you're an early builder, reach out because I'll be available to walk through the process with you. [Open a GitHub issue](https://github.com/brainwavecollective/reachy-eyes/issues) to get in touch with any questions or related needs.

---

## Prepare your parts 

### Cut the wires

This project requires the following wires. Lengths don't have to be precise. This is meant as a reference to help you get started easily. I recommend pre-cutting all of these first as they're much easier to have on hand as needed. 

| Wire | Cut Length (mm) | End 1 Strip | End 2 Strip |
|------|----------------|-------------|-------------|
| A | 34 | 8mm | 12mm |
| B | 50 | 8mm | 8mm |
| C | 38 | 5mm | 8mm |
| D | 46 | 5mm | 8mm |
| E | 47 | 3mm | 8mm |
| F | 46 | 3mm | 12mm |
| G | 49 | 3mm | 5mm |
| H | 47 | 3mm | 5mm |
| I | 47 | 3mm | 12mm |
| J | 38 | 3mm | 8mm |

### Bend the LED Leads 

A pair of needle nose pliers are ideal for this (the only time they are necessary).

## Build the daughter board 

You'll need to cut your PCB which is easy using a few different methods. There are lots of tutorials out there, and it doesn't matter how you get there, but assuming standard 2.54mm spacing **your goal is a small perf board that is: 22 x 4 holes**

You will install the LEDs and wires first, and then the resistors/capacitors and logic level shifters.

Wires will be bent out of the way so that they are roughly where they will need to be placed.

> [!WARNING]
> Solid wire can only withstand a few bends before it becomes *work hardened* and brittle. They will break, and you will be sad. The recommendation is to roughly place them per this guide and then keep them wherever they end up during the build process. Move them once more only when you are ready to place them for the Pico.

TBD: Pics/etc. for the process.

## Mount into Enclosure

Simply snap the parts together and you'll be good to go.

## Install

For software setup and running the application, see the [main project documentation](../INSTALLATION.md).


