import random

def generate_tech_jargon():
    verbs = ["Optimize", "Leverage", "Innovate", "Revolutionize", "Automate"]
    adjectives = ["Scalable", "Agile", "Robust", "Data-Driven", "Machine-Learning"]
    nouns = ["Platform", "API", "Blockchain", "IoT", "Algorithm"]

    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    tech_jargon = f"{verb} {adjective} {noun}"
    return tech_jargon

def test_tech_jargon_format():
    tech_jargon = generate_tech_jargon()
    words = tech_jargon.split()
    assert len(words) == 3, "Tech jargon phrase must have exactly 3 words."

if __name__ == "__main__":
    test_tech_jargon_format()
    for _ in range(5):
        print(generate_tech_jargon())