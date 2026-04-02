from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('Data_Prprocessing_Lead_Roadmap.pdf')

docs=loader.load()

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=50,
    chunk_overlap=0,
   
)

text=''' code = """
def greet(name):
    return f"Hello, {name}!"

def square(n):
    return n * n

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

class MathOperations:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

def main():
    print(greet("Nobita"))
    print(square(5))
    print(factorial(4))

    math = MathOperations()
    print(math.add(10, 5))
    print(math.subtract(10, 5))

if __name__ == "__main__":
    main()
"""'''

chunks=splitter.split_text(text)

print(chunks[1])