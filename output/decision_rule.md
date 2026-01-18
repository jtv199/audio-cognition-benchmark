# Auditory Cognition: Components and Decision Rules

This document outlines the functional components of human auditory cognition, primarily based on Baddeley's Multi-Component Working Memory Model (2012 update). For each component, we define its scope, typical activities, and the specific "Decision Rules" (mechanisms) that govern its operation.

---

## 1. The Central Executive ("The Boss")

### Scope
The Central Executive (CE) is the most complex component, responsible for attentional control rather than storage. It acts as a supervisory system that directs focus, switches between tasks, and inhibits irrelevant information.

### Typical Activities
*   **Selective Attention:** Focusing on one speaker in a noisy room (Cocktail Party Effect).
*   **Task Switching:** Alternating between adding and subtracting numbers.
*   **Inhibition:** Ignoring a "Stop" signal or a distractor voice.
*   **Dual-Task Coordination:** Driving while listening to complex instructions.

### Decision Rules & Mechanisms

*   **The "CEO" Rule:** The CE does not do the work itself; it decides *what* gets done.
    > "The central executive... [is] likened to a company's CEO, making decisions about which issues deserve attention and which should be ignored." (*Baddeley, 1996*)
    *   *Example:* The CEO doesn't build the car; they decide *to* build a car. Similarly, the CE doesn't "hear" the sound; it tells the Phonological Loop to "listen to that voice."

*   **The Inhibition Rule:** Capacity is often defined by what you can *ignore*, not just what you can hold.
    > "Engle and colleagues... emphasize the importance of inhibitory processes, which they argue are crucial to shielding the memory content from potential disruption." (*Baddeley, 2012, p. 20*)
    *   *Example:* Trying to do math in your head while someone shouts random numbers at you. Your success depends on *blocking* the shouting, not just *doing* the math.

*   **The "Task Set" Rule:** The CE creates a temporary procedural program (a "mini-program") to guide action.
    > "It is as if some mini-program is set up and then runs... I think the investigation of this aspect of procedural working memory, sometimes referred to as 'task set,' will become increasingly influential." (*Baddeley, 2012, p. 22*)
    *   *Example:* "If you hear a bell, press Red. If you hear a whistle, press Green." You load this rule into your mind once, and then it runs automatically until the rules change.

---

## 2. The Phonological Loop ("The Recorder")

### Scope
A modular system for the temporary storage of verbal and acoustic information. It consists of a passive **Phonological Store** (which holds traces) and an active **Articulatory Rehearsal** process (which refreshes them).

### Typical Activities
*   **Digit Span:** Repeating a phone number.
*   **Vocabulary Acquisition:** Learning new words (e.g., "flower-svieti").
*   **Instruction Following:** Holding a verbal command in mind while executing it.

### Decision Rules & Mechanisms

*   **The 2-Second Decay Rule:** Capacity is time-limited, not item-limited. You can hold what you can say in 2 seconds.
    > "People are able to remember as many words as they can articulate in two seconds." (*Baddeley, 2012, p. 8*)
    *   *Example:* You can remember "Cat, Pen, Bus, Day, Hot" easily. You will struggle to remember "University, Opportunity, Constitutional, Refrigerator, Hippopotamus" because they take too long to say, so the start fades before you finish the end.

*   **The Automatic Access Rule:** Spoken language enters the store directly; written language must be converted.
    > "We interpret this as suggesting that spoken material gains obligatory access to the phonological store, whereas written material needs to be subvocalized if it is to register." (*Baddeley, 2012, p. 8*)
    *   *Example:* You can't "close your ears." If someone speaks near you, it enters your working memory automatically. You *can* close your eyes to avoid reading text.

*   **The No-Chaining Rule (Competitive Queuing):** We do not remember order by linking A→B→C (Chaining). If we did, forgetting 'B' would break the chain. Instead, items are activated simultaneously with different strengths (Primacy Gradient).
    > "The most obvious hypothesis is through... chaining... However, this has some major potential problems; if one item is lost, then the chain is broken... yet it is often the case that despite errors in the middle of a sequence, the latter part is reproduced correctly." (*Baddeley, 2012, p. 9*)
    *   *Example:* Remembering "7-9-2".
        *   *Chaining:* 7 is tied to 9, 9 is tied to 2. If you forget 9, you lose 2.
        *   *Gradient:* 7 is Yelling, 9 is Talking, 2 is Whispering. You pick the loudest one first. If you forget 9, you can still hear 2 whispering.

---

## 3. The Episodic Buffer ("The Stage")

### Scope
A passive storage system that integrates (binds) information from different sources (Phonological Loop, Visuo-Spatial Sketchpad, LTM) into coherent "chunks" or episodes. It is the gateway to conscious awareness.

### Typical Activities
*   **Binding:** Connecting a face to a voice, or a color to a shape.
*   **Chunking:** Grouping "C A T D O G" into "Animals" to remember more.
*   **Story Comprehension:** Integrating a sequence of sentences into a narrative.

### Decision Rules & Mechanisms

*   **The 4-Chunk Capacity Rule:** The capacity of the focus of attention is strictly limited to about 4 chunks.
    > "On this point we agree with Cowan (2005) in assuming a capacity in the region of four chunks." (*Baddeley, 2012, p. 15*)
    *   *Example:* You can hold "Cat, Dog, Fish, Bird" (4 items). If you add "Cow," one of the others will fall out, unless you group them into "Pets" and "Farm" (2 chunks).

*   **The Binding Maintenance Rule:** Creating a binding (e.g., "Red Square") is automatic and low-cost. *Holding* that binding against distraction requires Executive attention.
    > "We interpreted this as suggesting that binding did not demand extra attention but that maintaining it against distraction did." (*Baddeley, 2012, p. 17*)
    *   *Example:* It's easy to see a blue circle and say "Blue Circle." It's hard to remember "Blue Circle" if you have to count backwards by 3s. The distraction breaks the glue holding "Blue" and "Circle" together.

---

## 4. The Visuo-Spatial Sketchpad ("The Eye")

### Scope
Handles visual (color, shape) and spatial (location, movement) information. It is separate from the verbal system.

### Typical Activities
*   **Corsi Block Tapping:** Remembering a sequence of spatial locations.
*   **Mental Rotation:** Imagining how an object looks from another angle.
*   **Navigation:** Maintaining a mental map of a route.

### Decision Rules & Mechanisms

*   **The Visual vs. Spatial Rule:** These are distinct sub-systems. You can disrupt one without disrupting the other.
    > "Visual pattern span is dissociable from spatial Corsi span... pattern span can be disrupted by concurrent visual processing, whereas Corsi span is more susceptible to spatial disruption." (*Baddeley, 2012, p. 12*)

---

## Summary of AI Benchmarking Implications

| Component | Test Type | "Decision Rule" to Stress |
| :--- | :--- | :--- |
| **Central Executive** | Dual-Task / N-Back | Can the AI inhibit irrelevant info? (Inhibition Rule) |
| **Phonological Loop** | Serial Recall (Non-words) | Does the AI fail via chaining (total collapse) or gradient (transposition)? (No-Chaining Rule) |
| **Episodic Buffer** | Binding under Load | Can the AI maintain "Face+Voice" binding while counting backwards? (Maintenance Rule) |
| **Sketchpad** | Spatial Instruction | Can the AI map "Left/Right" audio cues to a grid? (Spatial Rule) |

---

## 5. Auditory Scene Analysis (ASA)

### Scope
Defined by Bregman (1990), this model describes how the brain segregates complex auditory mixtures into distinct "streams" or objects.

### Decision Rules
*   **Primitive Segregation (Bottom-Up):**
    *   *Rule:* Group by physics (pitch proximity, onset synchrony, harmonicity).
    *   *Test:* Can the AI separate two simultaneous beeps?
*   **Schema-Based Segregation (Top-Down):**
    *   *Rule:* Group by learned knowledge (language, melody, familiarity).
    *   *Test:* Can the AI hear its name in a noisy room?

## 6. The Katz (Buffalo) Model

### Scope
A clinical model for Central Auditory Processing Disorder (CAPD), focusing on diagnostic categories.

### Components
*   **Phonemic Decoding:** Quick, accurate processing of speech sounds (e.g., distinguishing /ba/ from /da/).
*   **Tolerance-Fading Memory (TFM):** Understanding speech in noise + Short-Term Memory.
*   **Integration:** Combining auditory info with visual/other inputs (e.g., "Put the ball (audio) in the red box (visual)") or binaural cues.
*   **Organization:** Sequencing, planning, and keeping order.

## 7. Ease of Language Understanding (ELU) Model

### Scope
Rönnberg's model (2013) focusing on the interaction between implicit processing and explicit working memory during listening.

### Decision Rules
*   **Implicit Processing (RAMBPHO):**
    *   *Mechanism:* Rapid, Automatic, Multimodal Binding of PHOnology.
    *   *Rule:* If the signal is clear and matches LTM, processing is fast and effortless.
*   **Explicit Processing (Mismatch):**
    *   *Mechanism:* Slow, resource-heavy Working Memory loop.
    *   *Rule:* Triggered only when there is a **Mismatch** (noise, accent, distortion). The brain must "pause and repair."