import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple Inc. is planning to open a new store in New York City."

# Process the text with SpaCy
doc = nlp(text)

# Extract and print named entities
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
