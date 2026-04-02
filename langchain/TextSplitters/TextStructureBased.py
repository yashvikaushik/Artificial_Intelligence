from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('Data_Prprocessing_Lead_Roadmap.pdf')

docs=loader.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0,
   
)

text='''Artificial Intelligence (AI) is transforming the world at an unprecedented pace. From healthcare to finance, AI systems are being used to automate tasks, improve decision-making, and enhance user experiences.

Machine Learning, a subset of AI, allows systems to learn from data without being explicitly programmed. It is widely used in applications such as recommendation systems, fraud detection, and self-driving cars.

Deep Learning is a further subset of Machine Learning that uses neural networks with many layers. These models are particularly powerful for tasks like image recognition, natural language processing, and speech recognition.

Natural Language Processing (NLP) enables machines to understand and generate human language. It powers chatbots, translation systems, and voice assistants like Siri and Alexa.

AI also raises ethical concerns. Issues such as bias, privacy, and job displacement need to be carefully addressed as AI continues to evolve.

The future of AI is both exciting and uncertain. While it has the potential to solve complex global challenges, it also requires responsible development and regulation.'''

chunks=splitter.split_text(text)

print(chunks)