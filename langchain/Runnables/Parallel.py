from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template='generate a linkldn post content on the following topic {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='generate an instagram post content on the following topic {topic}',
    input_variables=['topic']
)

model=ChatOpenAI()

parser=StrOutputParser()

chain=RunnableParallel(
    {
        'instagram':prompt2 | model | parser,
        'linkdln':prompt1 | model | parser,
    }
)

result=chain.invoke({'topic':'AI'})

print(result)