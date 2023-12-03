import sys

def replacestops(input_text):
    modified_content = input_text.replace('. ', '.\n')
    return modified_content

if __name__ == "__main__":
    input_text = sys.stdin.read()
    modified_text = replacestops(input_text)
    print(modified_text)


