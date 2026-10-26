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

for label, questions in (("IN THE ACT", in_act), ("NOT IN THE ACT", not_in_act)):
    print("\n" + label)
    for q in questions:
        top = search(q, k=1)[0]
        print(f"  {top['similarity']:.2f}  page {top['page']:>3}  {q}")