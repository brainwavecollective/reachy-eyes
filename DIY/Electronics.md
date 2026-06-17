# Reachy Eyes — Electronics Sourcing Guide

> **Scope:** This guide covers electronic components only. 3D printing, assembly, and firmware are covered in separate companion guides.

---

## Is This Project For You?

This is not a beginner guide, but it is intended to be well within reach for the average hobbyist if you're willing to push yourself a little. There are a few points of real complexity along the way (One optional SMD solder being the main one), but nothing that can't be learned. If this is your first time touching some of these skills, that's kind of the point. Building something complete and functional from scratch is rewarding in a way that buying the finished kit isn't.

If you'd rather skip the DIY and just get the finished accessory, [the fully built kit is available here](https://reachyeyes.brainwavecollective.ai/#buy). No judgment, that's what it's there for. It's my recommendation for most people. If you value your time, it is far less expensive to buy the kit. That said, the purpose of this guide is to walk you through the process and give you the ability to do and learn everything from scratch. 

---

## Parts Sourcing

All components in this guide are available from **DigiKey**. Single-supplier sourcing was a deliberate choice to simplify ordering, reduce shipping complexity, and make it easier for you to get started by giving you everything in one go.

That said, this is a simple circuit and most parts have direct equivalents. Where substitutions are reasonable, they're noted in the component details below. 

**[COMPLETE DIGIKEY CART](https://www.digikey.com/short/b4bpth0q)**
This cart includes all related electronic components (and maybe even a few that you already have on hand). The goal here is to demonstrate the most comlete kit to make sure you have everything necessary on hand. More details below if you want to get into it further. Note that you will still need to source 3D printed parts separately (files are included [3D parts printing guide is available here](3D.md)

You may want to [check out this section on level shifting](#logic-level-shifting) before you decide if you want to place the order for the SchmalzTech level shifter boards.

---

## BOM

| Item | Qty | Notes |
|------|-----|-------|
| [Perfboard / Project Board](https://www.digikey.com/en/products/detail/dfrobot/FIT0203/6588423) | 1 | Cut-to-size, PTH, 0.1" pitch |
| [WS2812 Addressable RGB LED (5mm)](https://www.digikey.com/en/products/detail/sparkfun-electronics/12986/5673799) | 2* | Through-hole, WS2812-compatible |
| [330Ω Resistor](https://www.digikey.com/en/products/detail/koa-speer-electronics-inc/MF1-4LCT52R331J/21679525) | 2 | 1/4W, axial through-hole |
| [0.1µF Ceramic Capacitor](https://www.digikey.com/en/products/detail/kemet/C320C104K5R5TA/818040) | 2 | 50V, X7R, radial |
| [470µF Electrolytic Capacitor](https://www.digikey.com/en/products/detail/rubycon/10YXJ470M6.3X11/717560) | 1 | 10V, radial, observe polarity |
| [SOT-23-5 Adapter](https://www.digikey.com/en/products/detail/schmalztech-llc/ST-SOT23-5/15283225) | 2* | Breakout for SMD IC onto perfboard |
| [Logic Buffer (SN74AHCT1G125)](https://www.digikey.com/en/products/detail/texas-instruments/SN74AHCT1G125DBVR/376028) | 2 | SOT-23-5, 3.3V→5V level shifting |
| [Raspberry Pi Pico 2 (RP2350)](https://www.digikey.com/en/products/detail/raspberry-pi/SC1631/24627136) | 1 | RP2350, 3.3V logic, USB programmable |
| [22 AWG Hook-Up Wire](https://www.digikey.com/en/products/detail/cnc-tech/1015-22-1-2000-001-1-td/3441643) | 2 ft | Solid core, PVC |
| [USB Cable (Micro-B to USB-C)](https://www.digikey.com/en/products/detail/adafruit-industries-llc/3879/9607602) | 1 | For connecting Pico 2 to host, 6in to 1ft |

\* DigiKey may require you to purchase more units than this project needs for this item.

See below for more details, as well as sourcing alternative parts and other potential modifications.

---

## Components

---

### Perfboard / Project Board (×1)
[DFRobot FIT0203 – Perfboard](https://www.digikey.com/en/products/detail/dfrobot/FIT0203/6588423) — $2.90

<details>
<summary>What it does</summary>

Provides a physical base for assembling the circuit. The board can be cut down to size, keeping the final assembly compact and tidy.

</details>

<details>
<summary>Alternatives & notes</summary>

Any general-purpose PTH (plated through-hole) perfboard with 0.1" pitch will work. Cut to fit.

</details>

---

### WS2812 Addressable RGB LED, 5mm (×2)
[SparkFun 12986](https://www.digikey.com/en/products/detail/sparkfun-electronics/12986/5673799) — $4.75 (5 pcs)

<details>
<summary>What it does</summary>

These are the eyes. Each LED contains red, green, and blue elements in a single package and can display any color. They are addressable, meaning a single data line from the microcontroller can control multiple LEDs in sequence (chained via DIN → DOUT), or each LED can be driven from its own GPIO pin. Note that in rare cases you may end up with LEDs that do not have DOUT available, meaning you will be required to address each individually.

</details>

<details>
<summary>Alternatives & notes</summary>

Stick with WS2812-compatible LEDs. The protocol matters more than the brand; this guide assumes WS2812 or WS2812B in 5mm through-hole form factor. Avoid substituting other addressable LED families without verifying protocol compatibility. There are many SMD variants available as well, but this guide assumes you are using the standard T-1¾ round LEDs.

</details>

---

### 330Ω Resistor (×2)
[KOA Speer MF1/4LCT52R331J](https://www.digikey.com/en/products/detail/koa-speer-electronics-inc/MF1-4LCT52R331J/21679525)

<details>
<summary>What it does</summary>

Placed in series on the data line between the microcontroller (or level shifter) and each LED. Helps suppress signal reflections and protects against transient voltage spikes that can corrupt data or damage the LED's internal controller.

</details>

<details>
<summary>Alternatives & notes</summary>

Any standard 5% 1/4W axial through-hole resistor in the 330Ω–470Ωish range will work. This is one of the most flexible parts in the BOM.

</details>

---

### 0.1µF Ceramic Capacitor (×2)
[KEMET C320C104K5R5TA](https://www.digikey.com/en/products/detail/kemet/C320C104K5R5TA/818040)

<details>
<summary>What it does</summary>

Decoupling capacitor placed close to each LED. Filters out high-frequency noise on the power supply line and helps maintain stable voltage at the LED during rapid color changes.

</details>

<details>
<summary>Alternatives & notes</summary>

0.1µF, 50V, X7R, radial ceramic. The X7R dielectric is slightly preferred for stability across temperatures, but it doesn't matter that much. So long as the minimum voltage requiremnets are met between 0.1µF and 0.47µF are acceptable substitutes.

</details>

---

### 470µF Electrolytic Capacitor (×1)
[Rubycon 10YXJ470M6.3X11](https://www.digikey.com/en/products/detail/rubycon/10YXJ470M6.3X11/717560) — $0.30

<details>
<summary>What it does</summary>

Bulk capacitor on the power rail. LEDs can draw brief but sharp current spikes when changing color. Without this capacitor, those spikes can cause voltage sag that leads to flickering, dimming, or erratic behavior. This isn't critical for this project, but for the price it's a nice to have and easy to justify adding in.

</details>

<details>
<summary>Alternatives & notes</summary>

Aim for 100µF–1000µF, 6.3V minimum, radial electrolytic fits this guide. Going higher on capacitance is fine. Going lower increases risk. Polarity matters so be sure to observe the markings on the component.

</details>

---

### Raspberry Pi Pico 2 / RP2350 (×1)
[Raspberry Pi SC1631](https://www.digikey.com/en/products/detail/raspberry-pi/SC1631/24627136) — ~$5.00

<details>
<summary>What it does</summary>

The microcontroller at the heart of the build. Runs the firmware that controls LED color, timing, and behavior. The Pico 2 is powered and programmed over USB. It operates at 3.3V logic, which is relevant to the level shifter discussion below.

</details>

<details>
<summary>Alternatives & notes</summary>

The original Pico (RP2040) will also work. Other microcontrollers are possible but you're on your own for firmware compatibility. The Pico 2 is inexpensive, well-supported, easy to find, and hard to beat at this price. You can also use it for other projects. For the Reachy Mini LITE (USB wired version) you do not need the Wireless Pico (Wireless Reachy Mini configuration is TBD).

</details>

---

### 22 AWG Solid Hook-Up Wire (×1 short length)
One option: CNC Tech 1015-22-1-2000-001-1-TD

<details>
<summary>What it does</summary>

Used for all point-to-point connections on the perfboard. Solid core wire holds its shape well for short runs on perfboard, making assembly cleaner.

</details>

<details>
<summary>Alternatives & notes</summary>

It's just wire, and you'll only need a foot or so. We're sandwiching this into our build so good insulation is important. I'm recommending 22 AWG solid core, PVC insulated. You might also consider spending a few dollars more and getting a multi-color kit, or a larger spool, or you may already have what you need lying around. I'm suggesting black as a universal convention to save a few dollars, but other colors can help with tracing connections. A few colors is ideal to cover power, ground, and signals.

</details>

---

### USB Cable — 5 pin Micro-B to USB-C (×1)
[Adafruit 3879](https://www.digikey.com/en/products/detail/adafruit-industries-llc/3879/9607602) — $2.95

<details>
<summary>What it does</summary>

Connects the Raspberry Pi Pico 2 (Micro-B port) to the USB-C port in the head of Reachy.

</details>

<details>
<summary>Alternatives & notes</summary>

This is a difficult item to find at DigiKey, so you may want to source elswhere. Any 6" 5 pin Micro-B to USB-C cable will probably work BUT this was designed for relatively low clearance plugs so you'll want to look for minimal material around the port of the plug. E.g., avoid a big bulky section where you grip the plug. 6 inches is ideal but up to 1 foot or so will work.

</details>

---

## Logic Level Shifting

The Pico 2 outputs 3.3V logic. WS2812 LEDs expect ~5V logic on the data line. In practice, **3.3V often works, but not always.** Some builds run perfectly without a level shifter. Others may exhibit flickering, wrong colors, or dropped updates. Whether your build works without one depends on your specific components, wire length, and build quality. This project probably doesn't need a level shifter, but you won't know until you try.

Here's how to think about your options:

---

### Do you want to learn SMD soldering?

This is the recommended path, and at the moment is what is documented in this guide.

The level shifter used here is a **SN74AHCT1G125** in a SOT-23-5 package, mounted on a breakout adapter for use on perfboard. It's a small component that requires fine soldering, but it's also a single IC with five pins. For someone wanting to get into SMD work, this is a reasonable first attempt: low pin count, forgiving layout, and low stakes if you need to retry. Consider buying one or two extra if you're brand new to this. An extremely fine tipped soldering iron is a practical requirement, and reflow setup or hotplate will help (but these are beyond most hobbyist setups).

These parts are included in the recommended shopping cart, repeated here for ease of reference:
- [SOT-23-5 Adapter – SchmalzTech ST-SOT23-5](https://www.digikey.com/en/products/detail/schmalztech-llc/ST-SOT23-5/15283225)
- [SN74AHCT1G125 – Logic Buffer](https://www.digikey.com/en/products/detail/texas-instruments/SN74AHCT1G125DBVR/376028)

<details>
<summary>What it does</summary>

Converts the Pico's 3.3V data signal to a 5V signal that WS2812 LEDs reliably recognize. The AHCT family is specifically well-suited to this: it accepts 3.3V input while running on a 5V supply, making it a clean single-chip solution for this exact problem. 

</details>

<details>
<summary>Adapter & assembly notes</summary>

The SOT-23-5 adapter converts the surface mount IC to a through-hole-friendly 0.1" pitch footprint that sits on perfboard like any other DIP component. Solder the IC to the adapter first, then treat it as a through-hole part for the rest of assembly.

Use 1–2 adapters and ICs depending on your wiring approach (one per LED if driving independently, one shared if chaining).

</details>

---

### Not ready for SMD?

A through-hole version of this circuit using the **SN74AHCT125 (DIP package)** is in progress. If you'd prefer that path, [open a GitHub issue](https://github.com/brainwavecollective/reachy-eyes/issues) to let me know so I can prioritize getting that documented. It's probably a better way to go overall for this project, but I need to confirming layout & wire routing, and assembly instructions. If you are ambitious and figured this out on your own please feel free to share details. 

---

### Prefer to skip the level shifter entirely?

Some builds work fine without it so skipping the level shifter is a valid call. If you see flickering, unexpected colors, or LEDs that stop responding, the level shifter is the first thing to add. You can always retrofit it later but it's easiest to just include it from the start. That said, it's a toss up as to whether or not you need it so is only really necessary if you are having issues.