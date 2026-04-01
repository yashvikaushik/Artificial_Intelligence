from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template='write a joke about topic {topic}',
    input_variables=['topic']
)

model=ChatOpenAI()

parser=StrOutputParser()

prompt2=PromptTemplate(
    template='explain this joke {topic}',
    input_variables=['topic']
)


chain1=RunnableSequence(prompt1,model,parser)
chain2=RunnableSequence(chain1,prompt2,model,parser)

result1=chain1.invoke({'topic':'btech'})

result2=chain2.invoke({'topic':'btech'})

print(result1)
print('********************EXPLAINATION**********************')
print(result2)

