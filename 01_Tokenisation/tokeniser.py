import sys
def tokenize(text):
    text = text.replace(' ', '\n')

    punct = [')', ':', '\'', ',', '"','(']

    for char in punct:
        text = text.replace(char, f'{char} ')
    text = text.replace(' ', '\n')
    print(text)

if __name__ == "__main__":
    input = sys.stdin.read()
    tokenized = tokenize(input)
    print(tokenized)