from query import search

in_act = [
    "What are the obligations of providers of high-risk AI systems?",
    "Which AI practices are prohibited?",
    "What are the penalties for violations?",
    "What is a general-purpose AI model?",
    "Who enforces the regulation?",
]
not_in_act = [
    "What is the recipe for apple pie?",
    "Who won the football World Cup in 2022?",
    "How do I install Python on Windows?",
    "What is the capital of France?",
    "How do I train a neural network?",
]

in_act += [
    "Do I have to tell users they are talking to a chatbot?",
    "Can the police use facial recognition in public places?",
    "What is a regulatory sandbox?",
]
not_in_act += [
    "What is GDPR?",
    "How does ChatGPT work?",
    "What is machine learning?",
]

scores = {}
for label, questions in (("IN THE ACT", in_act), ("NOT IN THE ACT", not_in_act)):
    print("\n" + label)
    scores[label] = []
    for q in questions:
        top = search(q, k=1)[0]
        scores[label].append(top["similarity"])
        print(f"  {top['similarity']:.2f}  page {top['page']:>3}  {q}")

lowest_in = min(scores["IN THE ACT"])
highest_out = max(scores["NOT IN THE ACT"])
print(f"\nLowest in-Act score:      {lowest_in:.2f}")
print(f"Highest not-in-Act score: {highest_out:.2f}")
if lowest_in > highest_out:
    print(f"Gap from {highest_out:.2f} to {lowest_in:.2f}: any cutoff in between separates them.")
else:
    print("Overlap: no single cutoff separates all questions.")