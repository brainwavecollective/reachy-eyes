# Reachy Eyes — Assembly

> [!NOTE]
> This assembly guide is incomplete. 

This is a WIP which will be built out as a detailed guide, but I am still uploading pics/etc. and waiting to put on the polish until a few people can confirm parts availability and general workflow. I need collaborators for this to work for everyone! Feel free to [open a GitHub issue](https://github.com/brainwavecollective/reachy-eyes/issues) to get in touch with any questions or support along the way.

## Before You Begin

This guide assumes you are comfortable with basic soldering and related efforts. If you haven't soldered before this project is not recommended.

### Tools Required

- Soldering iron with a fine tip
- Solder (63/37 or 60/40, rosin core recommended)
- Flux paste, self-cleaning / no-clean recommended
- Wire strippers
- Flush cutters
- Needle Nose Pliers (or similar)

### If You Are Doing the recommended but optional SMD Level Shifter

The SOT-23-5 IC can be hand soldered with the right tip and enough patience,  but, if you already have an SMD setup (hotplate, reflow oven, or similar) then this will be easy. This guide represents the hard end of what's possible without highly specialized equipment. A steady hand, a fine tip, and good magnification are non-negotiable.

- Extremely fine soldering tip (0.2mm or similar)
- Hands-free magnification (e.g., magnifying lamp, or digital microscope)
- Flux (no-clean solder paste or extremely fine low melt solder is recommended)

If you have a hotplate or reflow setup, the process is faster and more reliable, but those workflows are outside the scope of this guide. DO NOT source that equipemnt just for this project... it's only worth it if you intend on doing other SMD work in the future.

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

This project requires specific wires as follows. Lenghts don't have to be precise but are meant as a reference to help you get started easily. I recommend pre-cutting all of these first as they're much easier to have on hand/re-cut on the fly as needed. 

| Wire | Cut Length (mm) | End 1 Strip | End 2 Strip |
|------|----------------|-------------|-------------|
| A | 34 | 8mm (L) | 12mm (XL) |
| B | 50 | 8mm (L) | 8mm (L) |
| C | 38 | 5mm (M) | 8mm (L) |
| D | 46 | 5mm (M) | 8mm (L) |
| E | 47 | 3mm (S) | 8mm (L) |
| F | 46 | 3mm (S) | 12mm (XL) |
| G | 49 | 3mm (S) | 5mm (M) |
| H | 47 | 3mm (S) | 5mm (M) |
| I | 47 | 3mm (S) | 12mm (XL) |
| J | 38 | 3mm (S) | 8mm (L) |

### Bend the LED Leads 

A pair of needle nose pliers are ideal for this (the only time they are necessary).

## Build the daughter board 

You'll need to cut your PCB which is easy using a few different methods. I prefer to score it with a knife and then snap across a hard surface (like a vise). A pair of pliers or two also works, and you can also cut with a hand saw or trim with flush-cut pliers. In short, there are lots of tutorials out there, and it doesn't matter how you get there, but **your goal is a small perf board that is: 22 x 4 holes (assuming standard 2.54mm spacing)**

You will install the LEDs and wires first, and then the resistors/capacitors and logic level shifters.

Wires will be bent out of the way so that they are roughly where they will need to be placed.

> [!WARNING]
> Solid wire can only withstand a few bends before it becomes *work hardened* and brittle. They will break, and you will be sad. The recommendation is to roughly place them per this guide and then keep them wherever they end up during the build process. Move them once more only when you are ready to place them for the Pico.

TBD: Pics/etc. for the process.

## Mount into Enclosure

By now your 3D print should be complete. Simply snap the parts together and you'll be good to go. 

## Install

For software setup and running the application, see the [main project documentation](../INSTALLATION.md).


