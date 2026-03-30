from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model=ChatOpenAI(model='gpt-4')

prompt1=PromptTemplate(
    template='generate detailed notes form the following text {text}',
    input_variables=['text']
)

prompt2=PromptTemplate(
    template='generate 5 mcq type quiz questions from the following text {text}',
    input_variables=['text']
)

prompt3=PromptTemplate(
    template='merge the provided notes and quiz into a single document notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes','quiz']
)

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
    'notes':prompt1 | model | parser,
    'quiz':prompt2 | model |parser
    }
)

merge_chain=prompt3 | model | parser

chain=parallel_chain | merge_chain

text='''
Supervised learning is a type of machine learning where models are trained on labeled datasets, meaning each input is paired with a correct output. The model learns the relationship between inputs and outputs and is commonly used for tasks like classification (e.g., spam detection) and regression (e.g., predicting prices). In contrast, unsupervised learning deals with unlabeled data, where the model explores the data to identify hidden patterns, structures, or groupings without any predefined answers—this is often used for clustering and dimensionality reduction. Reinforcement learning takes a different approach, where an agent interacts with an environment and learns by receiving rewards or penalties for its actions. Over time, the agent improves its decision-making to maximize cumulative rewards, making it useful for applications like game playing, robotics, and autonomous systems.
'''

result=chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()

