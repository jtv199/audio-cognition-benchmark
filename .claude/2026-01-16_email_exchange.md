# Email Exchange: Framework Selection & Reference Request

**Date:** January 16, 2026
**Participants:** Jack Peng, Ting Dang
**Subject:** Framework Selection (Direction clarification) & Reference Request

---

### Reply from Ting Dang

**From:** Ting Dang <ting.dang@unimelb.edu.au>
**Sent:** Friday, January 16, 2026
**To:** Jack Peng <k.peng5@student.unimelb.edu.au>

Thanks for the clarification. It’s good to know that chapter 4 is useful.

Regarding the directions, both are reasonable but still do not address the research questions we ask. The good part is the dual-task experiments and we can incorporate them as one of the tasks for our ones, but purely based on that is very limited, and only measures one aspect. Please list the possible tasks that you think of in the dual-task setting and we can include them probably under one category!

Please don’t worry about the taxonomy and we will figure it out. Appreciate your sharing of all the valuable resources and theories!

Re your internship: sure happy to help. Feel free to put me in.

Just let me know when you are back from your leave and we will keep our discussion then. During this time, will keep you updated via emails to keep you in the loop!

Have a great break!

Best regards
Ting

---

### Original Message from Jack Peng

**From:** Jack Peng <k.peng5@student.unimelb.edu.au>
**Sent:** Friday, January 16, 2026 12:48:20 PM
**To:** Ting Dang <ting.dang@unimelb.edu.au>
**Subject:** Framework Selection (Direction clarification) & Reference Request

Dear Professor Dang,

I hope you are having a good week.

Since we missed our last meeting, I wanted to send a brief update on the framework selection.

**Travel Update**
I will be traveling during our next three scheduled meetings. However, I will remain available via email and can schedule ad-hoc quick calls if you need to discuss anything urgently.

**Framework Selection**
I have been reviewing Auditory Cognition and Human Performance (specifically Chapters 4 and 6) to find a definitive taxonomy between cognitive models and specific tasks. So far in my research, I have found that different cognitive models try to capture/answer a useful question instead of fitting into a single hierarchy. (IE: Baddeley's model asks "What cognitive areas are constrained by other tasks?" and Rönnberg's ELU model asks "How do we know if this auditory task is difficult or simple?"). I am not sure which models should we focus on since a lot of existing auditory tasks from MMAU-pro and other benchmarks would cover multiple components of multiple models. Which means it would be difficult to prove that these human cognitive components are useful in describing MM-LLM behavior.

Since no existing MM-LLM paper explicitly maps these cognitive model, I believe our contribution lies in applying these established human methodologies to AI for the first time.

I see three potential directions for our test design, and I believe Direction 1 is the strongest.

**The Experimental Approach:** We can use standard cognitive psychology experiments outlined in Chapters 4 and 6 to isolate specific processing components. We can mirror the methodology of "Dual-Task Interference experiment" Baddeley & Hitch (1974) used to originally prove that "Working Memory" is distinct from the "Central Executive."

*The Logic:* If two tasks use the same cognitive resource, doing them simultaneously will cause performance to collapse. If they use different resources, performance remains stable.

*Example: Executive vs. Phonological Loop (The "Reasoning" Experiment):*
*   **Task:** Ask the AI to solve a complex verbal reasoning puzzle (Executive task).
*   **Interference:** Ask it to solve the puzzle while repeating a nonsense sequence like "the-the-the" (Articulatory Suppression) or holding a 6-digit number string (Loop Load).
*   **Result:** If the AI fails under load, it has a "single-channel" bottleneck. If it succeeds, it demonstrates a human-like separation between Executive processing and Short-Term storage.

It provides structural proof of how the model thinks, moving beyond simple accuracy metrics to model architecture validation.

**The Clinical Approach (CAPD Testing)**
This uses test batteries designed for Central Auditory Processing Disorder (e.g., SCAN-3) to identify functional deficits. There are standard batteries of tests, which makes tasks selection easier.
*   *Example: Competing Sentences:* Listen to different sentences in each ear; repeat only one. (Tests Inhibition/Tolerance-Fading Memory).
*   *Example: Filtered Words:* Recognize muffled speech. (Tests Auditory Closure/Episodic Buffer).

*Pros/Cons:* While these established tests cover a wide range of deficits, they are diagnostic rather than structural. They would allow us to benchmark AI against human developmental norms (e.g., "The model performs like a 6-year-old"), but they are less effective at proving distinct cognitive components than Direction 1.

**My Plan**
I propose focusing on Direction 1, citing Chapters 4 and 6 of the text as our framework for "Comprehensive Auditory Cognition." I have not found any other source as systematic as this text.

I will select ~10 tasks from the book to form a representative sample, and then select 1 or 2 (likely the Dual-Task experiment) to implement immediately as a pilot.

**Reference Request**
Finally, I am currently applying to the Australia AI Safety Institute as an AI safety engineer role. Would you be willing to be listed as a reference on my application? They may contact you simply to verify that I am a Master's student currently conducting research under your supervision.

Please let me know if you are comfortable with this, and if so, the best contact number/email to provide.

Best regards,
Jack