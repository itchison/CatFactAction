import markovify

# Get raw text as string.
with open("catfacts/catfacts.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)
fact=text_model.make_sentence()
pre="::set-output name=fact::"
print(fact)
output=pre + fact
print(output)
print("done")