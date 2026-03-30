from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

class feedback(BaseModel):
    sentiments:Literal['positive','negative'] =Field(description='give the sentiments of the given feedback')

parser=PydanticOutputParser(pydantic_object=feedback)

parser1=StrOutputParser()


model=ChatOpenAI(model='gpt-4')

prompt1=PromptTemplate(
    template='classify the user feedback as positive or negative ' \
    '{text}' \
    '{format_instructions}',
    input_variables=['text'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

prompt2=PromptTemplate(
    template='write an appropriate response to this positive feedback: {text}',
    input_variables=['text']
)

prompt3=PromptTemplate(
    template='write an appropriate response to this negative feedback: {text}',
    input_variables=['text']
)


classifier_chain=prompt1 | model | parser 

branch_chain=RunnableBranch(
     (lambda x:x.sentiments=='positive',prompt2 | model | parser1),
     (lambda x:x.sentiments=='negative',prompt3 | model | parser1),
     RunnableLambda(lambda x: 'could not find sentiments')
)

text='''
Supervised learning is a type of machine learning where models are trained on labeled datasets, meaning each input is paired with a correct output. The model learns the relationship between inputs and outputs and is commonly used for tasks like classification (e.g., spam detection) and regression (e.g., predicting prices). In contrast, unsupervised learning deals with unlabeled data, where the model explores the data to identify hidden patterns, structures, or groupings without any predefined answers—this is often used for clustering and dimensionality reduction. Reinforcement learning takes a different approach, where an agent interacts with an environment and learns by receiving rewards or penalties for its actions. Over time, the agent improves its decision-making to maximize cumulative rewards, making it useful for applications like game playing, robotics, and autonomous systems.

'''

chain=classifier_chain | branch_chain

result=chain.invoke({'text':text})
print(result)


