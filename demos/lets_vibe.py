import time
from _runner import run

def demo(eyes, duration=None):
    end = None if duration is None else time.time() + duration
    print("VIBE: Emotional state expressions via ML model\n")
    
    # Model inputs: (valence, arousal, dominance, complexity, coherence)
    vibes = [
        ("joyful",        0.95, 0.85, 0.75, 0.30, 0.90, "😄", "happy, excited, playful"),
        ("deep_peace",    0.65, 0.10, 0.50, 0.55, 0.53, "🕉️", "meditation, zen gardens"),
        ("frustrated",    0.20, 0.85, 0.80, 0.80, 0.85, "😤", "annoyed, warning lights"),
        ("curious",       0.60, 0.55, 0.45, 0.70, 0.75, "🤔", "inquisitive, exploring"),
        ("social",        0.90, 0.93, 0.95, 0.80, 0.93, "🎉", "celebration"),
        ("passionate",    0.95, 0.75, 0.95, 0.70, 0.70, "❤️", "romantic love, warm"),
        ("task_focused",  0.50, 0.65, 0.55, 0.75, 0.75, "💼", "attentive, engaged, working"),
        ("sunset",        0.80, 0.60, 0.97, 0.70, 0.65, "🌅", "golden hour"),
        ("content",       0.80, 0.30, 0.60, 0.20, 0.90, "😊", "satisfied, at ease"),
        ("overwhelmed",   0.35, 0.82, 0.30, 0.93, 0.30, "🤯", "overloaded, chaotic"),
        ("playful",       0.90, 0.90, 0.80, 0.80, 0.90, "🎮", "fun, energetic, bouncy"),
        ("ember",         0.20, 0.95, 1.00, 0.95, 0.95, "🔥", "primal fire"),
        ("melancholy",    0.30, 0.25, 0.40, 0.60, 0.65, "😔", "sad, reflective, subdued"),
        ("sunshine",      0.85, 0.90, 0.75, 0.85, 0.90, "☀️", "pleasant surprise, sparklers"),
        ("golden_glow",   0.95, 0.80, 1.00, 0.70, 0.80, "✨", "divine warmth"),
    ]
    
    while end is None or time.time() < end:
        for name, val, aro, dom, cplx, coh, emoji, desc in vibes:
            eyes._device.send_command(f"VIBE {val} {aro} {dom} {cplx} {coh}")
            print(f"{emoji} {name:14} | V:{val:.2f} A:{aro:.2f} D:{dom:.2f} Cx:{cplx:.2f} Ch:{coh:.2f} | {desc}")
            time.sleep(1.5)

if __name__ == "__main__":
    run(demo)
