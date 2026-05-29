from datetime import datetime, timezone

# English / Communication aptitude questions
# 4 topics × 3 difficulties × 6 questions = 72 total
# Selected at runtime: 1 easy + 1 medium + 1 hard per topic = 12 per subject
# question_format: multiple_choice
# correct_answer: the label (A/B/C/D)
#
# Topics:
#   1. Reading Comprehension  — inferring meaning, identifying main idea, tone
#   2. Grammar & Sentence Structure — correctness, clarity, syntax
#   3. Vocabulary & Word Usage — meaning in context, connotation, word choice
#   4. Writing & Communication Analysis — effective writing, coherence, purpose

APTITUDE_ENGLISH_QUESTIONS = [

    # ════════════════════════════════════════
    # TOPIC: READING COMPREHENSION
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "easy",
     "text": "Read the passage: 'The library opens at 8 AM and closes at 9 PM on weekdays. On weekends, it opens two hours later and closes one hour earlier.'\n\nWhat time does the library close on Saturdays?",
     "options": [{"label": "A", "value": "9 PM"}, {"label": "B", "value": "8 PM"}, {"label": "C", "value": "10 PM"}, {"label": "D", "value": "7 PM"}],
     "correct_answer": "B", "explanation": "The library closes at 9 PM on weekdays. On weekends it closes one hour earlier: 9 PM - 1 hour = 8 PM.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "easy",
     "text": "Read: 'Maria studied hard every night for two weeks before her final examination.'\n\nWhat is the main idea of this sentence?",
     "options": [{"label": "A", "value": "Maria passed her examination."}, {"label": "B", "value": "Maria studied consistently in preparation for her exam."}, {"label": "C", "value": "Maria was nervous about her exam."}, {"label": "D", "value": "The exam was very difficult."}],
     "correct_answer": "B", "explanation": "The sentence states that Maria studied hard for two weeks before her exam. The main idea is her consistent preparation.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "easy",
     "text": "Read: 'Unlike his cheerful siblings, Ben rarely smiled and preferred to spend his evenings alone reading.'\n\nWhat does this sentence tell us about Ben?",
     "options": [{"label": "A", "value": "He is very intelligent."}, {"label": "B", "value": "He has no siblings."}, {"label": "C", "value": "He is more introverted than his siblings."}, {"label": "D", "value": "He does not know how to read."}],
     "correct_answer": "C", "explanation": "The contrast with his 'cheerful siblings' and his preference for being alone suggest Ben is more introverted.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "easy",
     "text": "Read: 'The new policy requires all employees to submit their timesheets every Friday before 5 PM.'\n\nAccording to the passage, when must timesheets be submitted?",
     "options": [{"label": "A", "value": "Every Monday morning"}, {"label": "B", "value": "Any day before 5 PM"}, {"label": "C", "value": "Every Friday before 5 PM"}, {"label": "D", "value": "At the end of every month"}],
     "correct_answer": "C", "explanation": "The passage explicitly states: 'every Friday before 5 PM.'", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "easy",
     "text": "Read: 'Despite the heavy rain, the outdoor concert proceeded as planned and the audience stayed until the very end.'\n\nWhat does 'despite' signal in this sentence?",
     "options": [{"label": "A", "value": "A reason for the concert being cancelled"}, {"label": "B", "value": "A contrast — the event happened even though rain was expected to stop it"}, {"label": "C", "value": "Agreement between two ideas"}, {"label": "D", "value": "A time sequence"}],
     "correct_answer": "B", "explanation": "'Despite' signals contrast — the concert continued even though heavy rain would typically prevent it.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "easy",
     "text": "Read: 'Recycling aluminium uses 95% less energy than producing it from raw materials.'\n\nWhat is the author's likely purpose in stating this fact?",
     "options": [{"label": "A", "value": "To criticize the aluminium industry"}, {"label": "B", "value": "To emphasize the energy benefit of recycling"}, {"label": "C", "value": "To argue that aluminium should be banned"}, {"label": "D", "value": "To explain how aluminium is made"}],
     "correct_answer": "B", "explanation": "The statistic highlights a major advantage of recycling — its purpose is to show recycling saves substantial energy.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "medium",
     "text": "Read the passage: 'Automation is reshaping industries across the globe. While it increases efficiency and reduces costs, it also displaces workers in repetitive roles. Economists disagree about whether new jobs created by technology will adequately replace those lost.'\n\nWhat is the central tension presented in this passage?",
     "options": [{"label": "A", "value": "Automation makes products cheaper but lower quality."}, {"label": "B", "value": "Technology creates jobs faster than it destroys them."}, {"label": "C", "value": "Automation offers economic benefits but raises concerns about job displacement."}, {"label": "D", "value": "Economists support automation because it creates growth."}],
     "correct_answer": "C", "explanation": "The passage presents both sides: automation's efficiency gains versus the risk of job displacement — a tension economists have not resolved.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "medium",
     "text": "Read: 'The director's latest film was a critical darling but a commercial disappointment — praised by reviewers for its artistry yet ignored at the box office.'\n\nWhat does 'critical darling' most likely mean?",
     "options": [{"label": "A", "value": "A film that earned high profits"}, {"label": "B", "value": "A film greatly admired by critics"}, {"label": "C", "value": "A film that was heavily criticized"}, {"label": "D", "value": "A film aimed at children"}],
     "correct_answer": "B", "explanation": "The phrase is reinforced by 'praised by reviewers for its artistry.' A 'critical darling' is a work beloved by critics.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "medium",
     "text": "Read: 'Studies suggest that students who sleep fewer than seven hours perform measurably worse on memory and attention tasks the following day. Yet many students sacrifice sleep to gain more study time, believing this tradeoff is worthwhile.'\n\nWhat logical flaw does the passage imply these students are making?",
     "options": [{"label": "A", "value": "They study subjects that do not require memory."}, {"label": "B", "value": "They are trading better cognitive performance for more study time, reducing the effectiveness of that study."}, {"label": "C", "value": "They sleep too much on weekends."}, {"label": "D", "value": "They do not read efficiently."}],
     "correct_answer": "B", "explanation": "The irony is that sacrificing sleep to study more actually impairs the memory and attention needed to learn — making the extra study time less effective.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "medium",
     "text": "Read: 'The tone of the letter was formal and measured, betraying none of the frustration she had felt when writing the first draft.'\n\nWhat can be inferred about the letter writer?",
     "options": [{"label": "A", "value": "She was incapable of feeling frustrated."}, {"label": "B", "value": "She revised her communication to hide her emotional state and appear professional."}, {"label": "C", "value": "She sent the first draft by mistake."}, {"label": "D", "value": "She preferred formal communication in all situations."}],
     "correct_answer": "B", "explanation": "'Betraying none of the frustration' implies the final version was deliberately edited to conceal her true feelings — a conscious communication choice.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "medium",
     "text": "Read: 'Some researchers argue that social media amplifies political polarization by creating echo chambers, while others contend the evidence for this effect is weaker than commonly assumed.'\n\nWhat is the author doing in this sentence?",
     "options": [{"label": "A", "value": "Proving that social media causes polarization"}, {"label": "B", "value": "Dismissing the idea of echo chambers entirely"}, {"label": "C", "value": "Presenting two opposing positions without taking a side"}, {"label": "D", "value": "Arguing that social media should be banned"}],
     "correct_answer": "C", "explanation": "The author uses 'while others contend' to present a counter-view, presenting the debate without endorsing either side.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "medium",
     "text": "Read: 'The report found that urban areas with more green spaces recorded lower rates of anxiety and depression among residents, even after controlling for income and population density.'\n\nWhat does 'even after controlling for' imply about the finding?",
     "options": [{"label": "A", "value": "Income and density are the only factors that matter."}, {"label": "B", "value": "The relationship between green spaces and mental health holds regardless of income or density differences."}, {"label": "C", "value": "The study was conducted in low-income neighbourhoods only."}, {"label": "D", "value": "Green spaces are more effective for wealthier populations."}],
     "correct_answer": "B", "explanation": "'Controlling for' means the researchers accounted for income and density so those variables could not explain the finding — the green space effect remains independently.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "hard",
     "text": "Read: 'The author does not explicitly state her thesis; instead she allows the accumulation of specific cases to do the argumentative work, trusting the reader to draw the obvious conclusion.'\n\nThis technique is best described as:",
     "options": [{"label": "A", "value": "Deductive reasoning — from general principle to specific case"}, {"label": "B", "value": "Inductive reasoning — building a general conclusion from specific evidence"}, {"label": "C", "value": "Circular reasoning — restating the conclusion as evidence"}, {"label": "D", "value": "Ad hominem — attacking the opposing argument's source"}],
     "correct_answer": "B", "explanation": "The author accumulates specific cases to lead the reader to a general conclusion — this is inductive reasoning presented through implication.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "hard",
     "text": "Read: 'Progress is not a straight line. For every technological advance that appeared to liberate humanity, history offers a corresponding account of new dependencies, new inequities, and unforeseen consequences.'\n\nWhich of the following best captures the author's underlying claim?",
     "options": [{"label": "A", "value": "Technology always causes more harm than good."}, {"label": "B", "value": "Progress should be halted until its consequences are fully understood."}, {"label": "C", "value": "Technological advancement is accompanied by complex and often negative side effects."}, {"label": "D", "value": "Progress is impossible without sacrifice."}],
     "correct_answer": "C", "explanation": "The author does not say technology is net negative — rather that every advance brings new problems. This is a nuanced claim about complexity, not a blanket condemnation.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "hard",
     "text": "Read: 'To call this policy a 'reform' is to abuse the language. A reform improves; this measure merely redistributes the burden from one group to another while leaving the underlying dysfunction untouched.'\n\nThe author's primary rhetorical strategy is:",
     "options": [{"label": "A", "value": "Emotional appeal through vivid personal stories"}, {"label": "B", "value": "Statistical evidence proving the policy failed"}, {"label": "C", "value": "Definitional argument — redefining the term 'reform' to expose a mismatch"}, {"label": "D", "value": "Ad hominem attack on the policy's authors"}],
     "correct_answer": "C", "explanation": "The author's argument hinges on definition: a true reform must improve; this policy does not improve. It is a definitional or semantic argument.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "hard",
     "text": "Read the two statements:\nStatement 1: 'All students who passed the exam studied for more than 20 hours.'\nStatement 2: 'Jana studied for 25 hours.'\n\nWhat can logically be concluded?",
     "options": [{"label": "A", "value": "Jana passed the exam."}, {"label": "B", "value": "Jana did not pass the exam."}, {"label": "C", "value": "Jana met the study-time requirement but we cannot conclude she passed."}, {"label": "D", "value": "All students who studied 25 hours passed."}],
     "correct_answer": "C", "explanation": "Statement 1 says passing → studied >20h. It does NOT say studying >20h → passing. Jana meets the condition but that does not guarantee she passed (affirming the consequent fallacy).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "hard",
     "text": "Read: 'The committee's silence on the matter was not neutral — it was, in its own way, a statement. Institutions communicate as much through what they choose not to say as through their formal declarations.'\n\nWhich of the following best paraphrases the author's argument?",
     "options": [{"label": "A", "value": "Silence is always evidence of wrongdoing."}, {"label": "B", "value": "Institutions should communicate more frequently."}, {"label": "C", "value": "Omission is itself a form of communication that carries meaning."}, {"label": "D", "value": "Formal declarations are less important than internal decisions."}],
     "correct_answer": "C", "explanation": "The author argues that not speaking is itself a communicative act — silence conveys a position just as words do.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "hard",
     "text": "Read: 'It would be naive to assume that simply providing accurate information is sufficient to change behaviour. People do not update their beliefs like machines updating software; beliefs are tied to identity, community, and emotion.'\n\nThe author implies that effective communication requires:",
     "options": [{"label": "A", "value": "More data and statistics"}, {"label": "B", "value": "Attention to the psychological and social dimensions of how people form beliefs"}, {"label": "C", "value": "Simpler language so everyone can understand"}, {"label": "D", "value": "Faster delivery of accurate information"}],
     "correct_answer": "B", "explanation": "The author argues facts alone are insufficient — beliefs are rooted in identity and emotion. Effective communication must therefore engage those psychological dimensions.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: GRAMMAR & SENTENCE STRUCTURE
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "easy",
     "text": "Which sentence is grammatically correct?",
     "options": [{"label": "A", "value": "She don't like coffee."}, {"label": "B", "value": "She doesn't likes coffee."}, {"label": "C", "value": "She doesn't like coffee."}, {"label": "D", "value": "She not like coffee."}],
     "correct_answer": "C", "explanation": "With a third-person singular subject ('she'), the auxiliary is 'doesn't' (does + not), and the main verb stays in its base form: 'like'.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "easy",
     "text": "Choose the correct sentence:",
     "options": [{"label": "A", "value": "Their going to the park."}, {"label": "B", "value": "There going to the park."}, {"label": "C", "value": "They're going to the park."}, {"label": "D", "value": "Theyre going to the park."}],
     "correct_answer": "C", "explanation": "'They're' is the contraction of 'they are.' 'Their' is possessive; 'there' refers to a place.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "easy",
     "text": "Identify the subject in this sentence: 'The tall girl with the red bag runs every morning.'",
     "options": [{"label": "A", "value": "red bag"}, {"label": "B", "value": "runs"}, {"label": "C", "value": "The tall girl"}, {"label": "D", "value": "every morning"}],
     "correct_answer": "C", "explanation": "The subject is who or what performs the action. 'The tall girl' is performing the action (runs). The prepositional phrase 'with the red bag' is a modifier.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "easy",
     "text": "Which of the following is a complete sentence?",
     "options": [{"label": "A", "value": "Running through the park."}, {"label": "B", "value": "Because she was tired."}, {"label": "C", "value": "The dog barked loudly."}, {"label": "D", "value": "After the long meeting."}],
     "correct_answer": "C", "explanation": "A complete sentence needs a subject and a predicate. 'The dog barked loudly' has both. The others are sentence fragments.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "easy",
     "text": "Choose the correct past tense: 'Yesterday, she ___ to the market.'",
     "options": [{"label": "A", "value": "go"}, {"label": "B", "value": "goes"}, {"label": "C", "value": "going"}, {"label": "D", "value": "went"}],
     "correct_answer": "D", "explanation": "'Went' is the irregular simple past tense of 'go.' 'Yesterday' confirms we need past tense.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "easy",
     "text": "Which sentence uses the apostrophe correctly?",
     "options": [{"label": "A", "value": "The student's books were left behind."}, {"label": "B", "value": "The students book's were left behind."}, {"label": "C", "value": "The student's book's were left behind."}, {"label": "D", "value": "The students books were left behind."}],
     "correct_answer": "A", "explanation": "'Student's' correctly shows singular possession. Option D has no apostrophe; options B and C misplace them.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "medium",
     "text": "Identify the error in this sentence: 'The team have made their decision, and each member are expected to comply.'",
     "options": [{"label": "A", "value": "No error"}, {"label": "B", "value": "'have' should be 'has'"}, {"label": "C", "value": "'are' should be 'is'"}, {"label": "D", "value": "Both 'have' and 'are' are incorrect"}],
     "correct_answer": "C", "explanation": "'Each member' is singular, so the verb must be 'is' ('each member is expected'). 'The team have' is acceptable in British English for collective nouns acting as individuals.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "medium",
     "text": "Which sentence correctly uses a semicolon?",
     "options": [{"label": "A", "value": "She studied hard; but she still failed."}, {"label": "B", "value": "She studied hard; she still failed."}, {"label": "C", "value": "She; studied hard, and still failed."}, {"label": "D", "value": "She studied; hard and still failed."}],
     "correct_answer": "B", "explanation": "A semicolon joins two independent clauses without a conjunction. Option A incorrectly uses a semicolon with 'but' — a comma should precede coordinating conjunctions.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "medium",
     "text": "Which of the following contains a dangling modifier?",
     "options": [{"label": "A", "value": "Running to the bus, she dropped her bag."}, {"label": "B", "value": "Having finished the exam, the students left."}, {"label": "C", "value": "Walking down the street, the flowers looked beautiful."}, {"label": "D", "value": "Tired after the race, he sat down to rest."}],
     "correct_answer": "C", "explanation": "In option C, the modifier 'Walking down the street' logically applies to the subject of the main clause — which is 'the flowers.' Flowers cannot walk. This is a dangling modifier.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "medium",
     "text": "Choose the sentence with correct subject-verb agreement:",
     "options": [{"label": "A", "value": "Neither the manager nor the employees was informed."}, {"label": "B", "value": "Neither the manager nor the employees were informed."}, {"label": "C", "value": "Neither the manager nor the employees is informed."}, {"label": "D", "value": "Neither the manager nor the employees are was informed."}],
     "correct_answer": "B", "explanation": "With 'neither…nor,' the verb agrees with the subject closest to it. 'Employees' is plural, so the verb is 'were.'", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "medium",
     "text": "Which sentence is written in the passive voice?",
     "options": [{"label": "A", "value": "The engineer designed the bridge."}, {"label": "B", "value": "The bridge was designed by the engineer."}, {"label": "C", "value": "The engineer is designing the bridge."}, {"label": "D", "value": "The engineer had designed the bridge."}],
     "correct_answer": "B", "explanation": "Passive voice: subject receives the action. 'The bridge was designed by the engineer' — the bridge (subject) had the action done to it.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "medium",
     "text": "Identify the type of clause underlined: 'She left early [because she had an appointment].'",
     "options": [{"label": "A", "value": "Independent clause"}, {"label": "B", "value": "Relative clause"}, {"label": "C", "value": "Adverbial clause of reason"}, {"label": "D", "value": "Noun clause"}],
     "correct_answer": "C", "explanation": "The bracketed clause begins with 'because' and explains why she left — it is an adverbial clause of reason.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "hard",
     "text": "Which sentence uses the subjunctive mood correctly?",
     "options": [{"label": "A", "value": "I wish he was more careful."}, {"label": "B", "value": "I wish he were more careful."}, {"label": "C", "value": "I wish he is more careful."}, {"label": "D", "value": "I wish he would was more careful."}],
     "correct_answer": "B", "explanation": "The subjunctive mood uses 'were' (not 'was') for hypothetical or wished-for states with 'wish' and 'if only': 'I wish he were more careful.'", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "hard",
     "text": "Choose the sentence that avoids a comma splice error:",
     "options": [{"label": "A", "value": "The presentation was excellent, the audience applauded."}, {"label": "B", "value": "The presentation was excellent; the audience applauded."}, {"label": "C", "value": "The presentation was excellent, audience applauded."}, {"label": "D", "value": "The presentation was excellent the audience applauded."}],
     "correct_answer": "B", "explanation": "A comma splice incorrectly joins two independent clauses with only a comma. The semicolon in option B correctly joins two related independent clauses.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "hard",
     "text": "What is the grammatical function of the italicised phrase in: 'The proposal submitted last Tuesday was rejected.'?",
     "options": [{"label": "A", "value": "Adverbial phrase modifying 'rejected'"}, {"label": "B", "value": "Participial phrase modifying 'proposal'"}, {"label": "C", "value": "Infinitive phrase acting as subject"}, {"label": "D", "value": "Prepositional phrase acting as subject complement"}],
     "correct_answer": "B", "explanation": "'Submitted last Tuesday' is a past participial phrase modifying the noun 'proposal' — it tells us which proposal is being referred to.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "hard",
     "text": "Which sentence correctly uses the present perfect tense?",
     "options": [{"label": "A", "value": "I have seen that film yesterday."}, {"label": "B", "value": "I seen that film already."}, {"label": "C", "value": "I have already seen that film."}, {"label": "D", "value": "I had see that film before."}],
     "correct_answer": "C", "explanation": "Present perfect: have/has + past participle. Option A incorrectly pairs present perfect with 'yesterday' (a specific past time point, which requires simple past). Option C is correct.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "hard",
     "text": "Identify the sentence that contains a misplaced modifier:",
     "options": [{"label": "A", "value": "She almost drove her kids to school every day."}, {"label": "B", "value": "He carefully read the instructions before starting."}, {"label": "C", "value": "We only eat organic vegetables."}, {"label": "D", "value": "Both A and C contain misplaced modifiers."}],
     "correct_answer": "D", "explanation": "In A, 'almost' should modify 'every day' (she drove them nearly every day), not 'drove.' In C, 'only' should precede 'organic vegetables.' Both are misplaced modifiers.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_structure", "difficulty": "hard",
     "text": "Which correctly expresses the third conditional (hypothetical past)?",
     "options": [{"label": "A", "value": "If she studied, she will pass."}, {"label": "B", "value": "If she would have studied, she passed."}, {"label": "C", "value": "If she had studied, she would have passed."}, {"label": "D", "value": "If she studies, she would pass."}],
     "correct_answer": "C", "explanation": "Third conditional: If + past perfect → would + have + past participle. Used for hypothetical situations in the past: 'If she had studied, she would have passed.'", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: VOCABULARY & WORD USAGE
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "easy",
     "text": "What does the word 'benevolent' mean?",
     "options": [{"label": "A", "value": "Hostile and aggressive"}, {"label": "B", "value": "Kind and generous"}, {"label": "C", "value": "Sad and lonely"}, {"label": "D", "value": "Clever and resourceful"}],
     "correct_answer": "B", "explanation": "'Benevolent' means well-meaning, kind, and generous. It comes from the Latin 'bene' (well) + 'volo' (wish).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "easy",
     "text": "Choose the word that is closest in meaning to 'diligent':",
     "options": [{"label": "A", "value": "Lazy"}, {"label": "B", "value": "Careless"}, {"label": "C", "value": "Hardworking"}, {"label": "D", "value": "Confused"}],
     "correct_answer": "C", "explanation": "'Diligent' means careful and hardworking. A diligent student puts in steady, careful effort.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "easy",
     "text": "Which word is the antonym (opposite) of 'transparent'?",
     "options": [{"label": "A", "value": "Clear"}, {"label": "B", "value": "Obvious"}, {"label": "C", "value": "Opaque"}, {"label": "D", "value": "Visible"}],
     "correct_answer": "C", "explanation": "'Opaque' means not able to be seen through — the opposite of 'transparent.'", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "easy",
     "text": "Choose the correct word: 'The committee will ___ the proposal at the next meeting.'",
     "options": [{"label": "A", "value": "review"}, {"label": "B", "value": "revue"}, {"label": "C", "value": "revu"}, {"label": "D", "value": "revew"}],
     "correct_answer": "A", "explanation": "'Review' means to examine or assess formally. A 'revue' is a type of theatrical entertainment.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "easy",
     "text": "What does 'ambiguous' mean?",
     "options": [{"label": "A", "value": "Clearly stated with no room for misunderstanding"}, {"label": "B", "value": "Open to more than one interpretation"}, {"label": "C", "value": "Extremely detailed and precise"}, {"label": "D", "value": "Completely unrelated to the topic"}],
     "correct_answer": "B", "explanation": "'Ambiguous' means open to multiple interpretations or unclear in meaning.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "easy",
     "text": "Choose the word that best completes the sentence: 'Her speech was so ___ that the audience quickly lost interest.'",
     "options": [{"label": "A", "value": "captivating"}, {"label": "B", "value": "monotonous"}, {"label": "C", "value": "inspiring"}, {"label": "D", "value": "concise"}],
     "correct_answer": "B", "explanation": "'Monotonous' means dull and lacking variety — which logically explains why the audience lost interest.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "medium",
     "text": "Choose the word with the correct connotation: 'The politician's speech was ___, touching on every point just enough to avoid committing to anything.' ",
     "options": [{"label": "A", "value": "comprehensive"}, {"label": "B", "value": "eloquent"}, {"label": "C", "value": "evasive"}, {"label": "D", "value": "detailed"}],
     "correct_answer": "C", "explanation": "'Evasive' carries the negative connotation of deliberately avoiding clear answers — fitting the context of avoiding commitment.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "medium",
     "text": "What does 'ubiquitous' mean?",
     "options": [{"label": "A", "value": "Rare and difficult to find"}, {"label": "B", "value": "Present, appearing, or found everywhere"}, {"label": "C", "value": "Unique to a specific culture"}, {"label": "D", "value": "Changing rapidly over time"}],
     "correct_answer": "B", "explanation": "'Ubiquitous' means seeming to appear everywhere at once — e.g., 'Smartphones have become ubiquitous in modern life.'", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "medium",
     "text": "Identify the word used incorrectly: 'The scientist's findings had a profound affect on the field of medicine.'",
     "options": [{"label": "A", "value": "profound"}, {"label": "B", "value": "findings"}, {"label": "C", "value": "affect (should be 'effect')"}, {"label": "D", "value": "field"}],
     "correct_answer": "C", "explanation": "'Effect' (noun) is needed here — the result or impact. 'Affect' is typically a verb meaning to influence. 'Had a profound effect on' is correct.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "medium",
     "text": "Which pair of words are homophones?",
     "options": [{"label": "A", "value": "principle / principal"}, {"label": "B", "value": "write / right"}, {"label": "C", "value": "their / there"}, {"label": "D", "value": "All of the above"}],
     "correct_answer": "D", "explanation": "All three pairs are homophones — words that sound the same but differ in spelling and meaning.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "medium",
     "text": "What is the difference between 'imply' and 'infer'?",
     "options": [{"label": "A", "value": "They mean the same thing"}, {"label": "B", "value": "A speaker implies; a listener infers"}, {"label": "C", "value": "A listener implies; a speaker infers"}, {"label": "D", "value": "'Imply' is for written text; 'infer' is for speech"}],
     "correct_answer": "B", "explanation": "To 'imply' is to suggest something indirectly (the speaker/writer does this). To 'infer' is to draw a conclusion from clues (the reader/listener does this).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "medium",
     "text": "Choose the most precise word: 'The lawyer's argument was not just persuasive — it was ___: every flaw in the opposing case was systematically dismantled.'",
     "options": [{"label": "A", "value": "verbose"}, {"label": "B", "value": "incisive"}, {"label": "C", "value": "superficial"}, {"label": "D", "value": "redundant"}],
     "correct_answer": "B", "explanation": "'Incisive' means intelligently analytical and clear — it captures the idea of penetrating to the core of an argument and dismantling it precisely.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "hard",
     "text": "Choose the word that most precisely fits the context: 'His reputation for ___ was well-earned; no matter how much evidence was presented, he refused to update his position.'",
     "options": [{"label": "A", "value": "intransigence"}, {"label": "B", "value": "prudence"}, {"label": "C", "value": "eloquence"}, {"label": "D", "value": "candour"}],
     "correct_answer": "A", "explanation": "'Intransigence' means refusing to change one's position despite pressure or evidence — exactly what the context describes.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "hard",
     "text": "What is the difference between 'sceptical' and 'cynical'?",
     "options": [{"label": "A", "value": "They are synonyms with no meaningful distinction"}, {"label": "B", "value": "'Sceptical' means doubtful and demanding evidence; 'cynical' implies a distrust of people's motives, often from world-weariness"}, {"label": "C", "value": "'Cynical' is more positive than 'sceptical'"}, {"label": "D", "value": "'Sceptical' applies only to scientific claims"}],
     "correct_answer": "B", "explanation": "A sceptic doubts claims and asks for evidence — a neutral epistemic stance. A cynic distrusts human motives and believes people act from self-interest — a more negative view of character.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "hard",
     "text": "Identify the malapropism (wrong word used that sounds similar to the correct one):\n'For all intensive purposes, the project is complete.'",
     "options": [{"label": "A", "value": "The phrase is correct as written."}, {"label": "B", "value": "'intensive' should be 'intents and' (for all intents and purposes)"}, {"label": "C", "value": "'purposes' should be 'purposes'"}, {"label": "D", "value": "'complete' should be 'completed'"}],
     "correct_answer": "B", "explanation": "The correct idiom is 'for all intents and purposes' — meaning in every practical sense. 'For all intensive purposes' is an eggcorn (a mishearing).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "hard",
     "text": "What does 'begging the question' mean in formal logic?",
     "options": [{"label": "A", "value": "Raising a topic that requires further discussion"}, {"label": "B", "value": "Using the conclusion as a premise in the argument — circular reasoning"}, {"label": "C", "value": "Asking a rhetorical question to make a point"}, {"label": "D", "value": "Avoiding the main point of an argument"}],
     "correct_answer": "B", "explanation": "To 'beg the question' (Latin: petitio principii) is a logical fallacy where the argument's conclusion is assumed as a premise — a form of circular reasoning.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "hard",
     "text": "Choose the sentence in which 'enervate' is used correctly:",
     "options": [{"label": "A", "value": "The motivational speech enervated the team before the championship."}, {"label": "B", "value": "The long humid summer enervated the workers, leaving them listless and unmotivated."}, {"label": "C", "value": "Regular exercise enervates the body over time."}, {"label": "D", "value": "The caffeine enervated her enough to finish the report."}],
     "correct_answer": "B", "explanation": "'Enervate' means to weaken or drain of energy — the opposite of energise. Option B correctly uses it to describe the debilitating effect of heat and humidity.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_word_usage", "difficulty": "hard",
     "text": "In context, choose the best word: 'Her argument was ___ — it appeared rigorous but contained a subtle flaw that only an expert would notice.'",
     "options": [{"label": "A", "value": "specious"}, {"label": "B", "value": "cogent"}, {"label": "C", "value": "trite"}, {"label": "D", "value": "verbose"}],
     "correct_answer": "A", "explanation": "'Specious' means superficially plausible but actually flawed — precisely fitting an argument that looks rigorous but contains a hidden error.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: WRITING & COMMUNICATION ANALYSIS
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "easy",
     "text": "Which is the most appropriate opening sentence for a formal email to a professor you have not met?",
     "options": [{"label": "A", "value": "Hey! I need help with assignment 3."}, {"label": "B", "value": "Dear Professor Santos, I am writing to request guidance on Assignment 3."}, {"label": "C", "value": "Yo Prof, got questions bout my assignment lol."}, {"label": "D", "value": "Hi there, assignment question below:"}],
     "correct_answer": "B", "explanation": "Formal written communication uses a proper salutation, full name, and a clear, polite statement of purpose.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "easy",
     "text": "What is the main purpose of a topic sentence in a paragraph?",
     "options": [{"label": "A", "value": "To conclude the paragraph with a summary"}, {"label": "B", "value": "To introduce the main idea of the paragraph"}, {"label": "C", "value": "To provide supporting details"}, {"label": "D", "value": "To link the paragraph to the next one"}],
     "correct_answer": "B", "explanation": "A topic sentence states the main point of the paragraph. All subsequent sentences in the paragraph should support or develop this central idea.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "easy",
     "text": "Which of the following best describes the tone of: 'I regret to inform you that your application was unsuccessful at this time.'?",
     "options": [{"label": "A", "value": "Casual and friendly"}, {"label": "B", "value": "Aggressive and dismissive"}, {"label": "C", "value": "Formal and politely regretful"}, {"label": "D", "value": "Excited and encouraging"}],
     "correct_answer": "C", "explanation": "The phrase 'I regret to inform you' signals formality and expressed regret — a standard tone for professional rejection communications.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "easy",
     "text": "In writing, what is the purpose of a concluding paragraph?",
     "options": [{"label": "A", "value": "To introduce new arguments not mentioned before"}, {"label": "B", "value": "To summarise the main points and reinforce the central idea"}, {"label": "C", "value": "To list all the sources used"}, {"label": "D", "value": "To define key terms used in the essay"}],
     "correct_answer": "B", "explanation": "A conclusion wraps up the piece by summarising the key arguments and restating the main idea — it does not introduce new points.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "easy",
     "text": "Which sentence is the most concise and clear?",
     "options": [{"label": "A", "value": "Due to the fact that it was raining, she decided to take the bus instead of walking."}, {"label": "B", "value": "Because it was raining, she took the bus."}, {"label": "C", "value": "She took the bus as a result of the rain that was occurring at the time."}, {"label": "D", "value": "Given the conditions of rain present, bus was taken by her."}],
     "correct_answer": "B", "explanation": "Option B is concise: it removes redundant phrases ('due to the fact that,' 'instead of walking') without losing meaning.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "easy",
     "text": "What does it mean for writing to be 'coherent'?",
     "options": [{"label": "A", "value": "It contains many technical terms."}, {"label": "B", "value": "Ideas flow logically and are clearly connected."}, {"label": "C", "value": "It is very long and detailed."}, {"label": "D", "value": "It uses formal vocabulary throughout."}],
     "correct_answer": "B", "explanation": "Coherence in writing means ideas are logically organized and connected — the reader can follow the argument without confusion.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "medium",
     "text": "Which of the following demonstrates the most effective use of transition words to show contrast?",
     "options": [{"label": "A", "value": "The report was detailed. Furthermore, it lacked a clear recommendation."}, {"label": "B", "value": "The report was detailed. Similarly, it lacked a clear recommendation."}, {"label": "C", "value": "The report was detailed; however, it lacked a clear recommendation."}, {"label": "D", "value": "The report was detailed. Therefore, it lacked a clear recommendation."}],
     "correct_answer": "C", "explanation": "'However' signals contrast between the positive detail and the negative absence of a recommendation. 'Furthermore' and 'similarly' signal continuation; 'therefore' signals result.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "medium",
     "text": "Which paragraph is better structured?",
     "options": [{"label": "A", "value": "Exercise benefits health. People run. It is also good for the mind. Gyms exist. Sleep is important too."}, {"label": "B", "value": "Regular exercise offers significant mental and physical health benefits. Studies show it reduces anxiety, improves cardiovascular health, and boosts cognitive performance. Even 30 minutes of moderate activity daily can produce measurable results."}, {"label": "C", "value": "Exercise, health, mind, body, and more. Important always. People should try."}, {"label": "D", "value": "Exercise is beneficial. Benefits are many. Many people exercise. Exercise is good."}],
     "correct_answer": "B", "explanation": "Option B has a clear topic sentence, supporting evidence, and specific details — all characteristics of a well-structured paragraph.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "medium",
     "text": "What is the difference between 'audience' and 'purpose' in writing?",
     "options": [{"label": "A", "value": "They are the same concept described differently"}, {"label": "B", "value": "'Audience' is who you are writing for; 'purpose' is why you are writing"}, {"label": "C", "value": "'Purpose' defines the length; 'audience' defines the format"}, {"label": "D", "value": "'Audience' refers to readers of fiction only"}],
     "correct_answer": "B", "explanation": "Audience = the intended reader. Purpose = the goal (to inform, persuade, entertain, instruct). Both shape vocabulary, tone, and structure choices.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "medium",
     "text": "Identify the logical fallacy: 'You should follow this diet — my favourite celebrity swears by it.'",
     "options": [{"label": "A", "value": "Straw man"}, {"label": "B", "value": "Appeal to authority (false authority)"}, {"label": "C", "value": "Slippery slope"}, {"label": "D", "value": "False dichotomy"}],
     "correct_answer": "B", "explanation": "Using a celebrity's endorsement as evidence for a diet is an appeal to false authority — fame does not make someone a qualified nutritional expert.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "medium",
     "text": "Which revision best improves the following sentence?\nOriginal: 'The reason why the project failed was because of a lack of communication.'",
     "options": [{"label": "A", "value": "The project failed because of a lack of communication."}, {"label": "B", "value": "The reason that the project failed was due to communication issues being absent."}, {"label": "C", "value": "The project, it failed because communication was lacking in it."}, {"label": "D", "value": "Lack of communication: this was the reason for the failure of the project."}],
     "correct_answer": "A", "explanation": "'The reason why…was because' is redundant. Option A removes the redundancy while preserving the full meaning.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "medium",
     "text": "What does it mean to 'tailor' your communication to an audience?",
     "options": [{"label": "A", "value": "Using sewing metaphors in your writing"}, {"label": "B", "value": "Adjusting your vocabulary, tone, and level of detail to suit the knowledge and expectations of your reader"}, {"label": "C", "value": "Shortening your writing to save time"}, {"label": "D", "value": "Using the same template for all communications"}],
     "correct_answer": "B", "explanation": "Tailoring communication means adapting your style to match the audience — e.g., technical detail for experts, plain language for general readers.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "hard",
     "text": "A student writes: 'This essay will argue that climate policy is important because climate change is bad.'\nWhat is the primary weakness of this thesis?",
     "options": [{"label": "A", "value": "It is too long."}, {"label": "B", "value": "It is circular — the premise ('climate change is bad') is too vague to support a meaningful argument."}, {"label": "C", "value": "It mentions policy, which is off-topic."}, {"label": "D", "value": "It uses first-person, which is never acceptable in academic writing."}],
     "correct_answer": "B", "explanation": "A strong thesis makes a specific, arguable claim. 'Climate change is bad' is vague and self-evident — it does not give the essay anything substantive to argue.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "hard",
     "text": "Identify the rhetorical device used: 'Ask not what your country can do for you — ask what you can do for your country.'",
     "options": [{"label": "A", "value": "Alliteration"}, {"label": "B", "value": "Antithesis"}, {"label": "C", "value": "Hyperbole"}, {"label": "D", "value": "Anaphora"}],
     "correct_answer": "B", "explanation": "This is antithesis — the juxtaposition of contrasting ideas in parallel structure ('what your country can do for you' vs 'what you can do for your country').", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "hard",
     "text": "A writer wants to argue that remote work improves productivity. Which type of evidence would be most persuasive in a formal report?",
     "options": [{"label": "A", "value": "A personal anecdote about working from home comfortably"}, {"label": "B", "value": "A famous person's quote about loving remote work"}, {"label": "C", "value": "A peer-reviewed study measuring output metrics before and after remote work adoption in 500 companies"}, {"label": "D", "value": "A social media poll of 200 workers"}],
     "correct_answer": "C", "explanation": "Empirical data from a controlled, large-scale, peer-reviewed study is the most credible and persuasive evidence in formal academic or professional writing.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "hard",
     "text": "Which of the following best describes the difference between denotation and connotation?",
     "options": [{"label": "A", "value": "Denotation is for verbs; connotation is for nouns"}, {"label": "B", "value": "Denotation is the literal dictionary meaning; connotation is the emotional or cultural associations the word carries"}, {"label": "C", "value": "Denotation refers to figurative language; connotation refers to literal meaning"}, {"label": "D", "value": "They are two terms for the same concept"}],
     "correct_answer": "B", "explanation": "Denotation: the precise, literal definition. Connotation: the implied associations. E.g., 'slender' and 'skinny' denote the same thing but carry different connotations (positive vs. negative).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "hard",
     "text": "A report concludes: 'Since 90% of surveyed students prefer morning classes, the university should schedule all courses before noon.'\nWhat logical flaw does this conclusion contain?",
     "options": [{"label": "A", "value": "The sample size is too large."}, {"label": "B", "value": "The conclusion overgeneralizes — preference for morning classes does not mean all courses should be scheduled before noon."}, {"label": "C", "value": "The data is fabricated."}, {"label": "D", "value": "The conclusion does not mention professors' preferences."}],
     "correct_answer": "B", "explanation": "The argument commits a hasty generalization / overreach — from 'prefer morning classes' it jumps to 'schedule ALL courses before noon,' ignoring practical constraints and the interests of other stakeholders.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "writing_and_communication", "difficulty": "hard",
     "text": "What is the 'Pyramid Principle' in professional communication?",
     "options": [{"label": "A", "value": "Starting with supporting details and building to a conclusion"}, {"label": "B", "value": "Structuring communication by leading with the key message, then supporting it with evidence and detail"}, {"label": "C", "value": "Using three arguments to support every claim"}, {"label": "D", "value": "Writing in bullet points only for corporate audiences"}],
     "correct_answer": "B", "explanation": "The Minto Pyramid Principle (Barbara Minto) recommends leading with the governing thought (answer/recommendation first), then supporting it — the inverse of traditional essay structure, optimized for busy professional readers.", "active": True, "createdAt": datetime.now(timezone.utc)},
]