import markovify

# Get raw text as string.
with open("catfacts/catfacts.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

print(text_model.make_sentence())