from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatOpenAI(model='gpt-4')

template1=PromptTemplate(
    template='enter a topic of your choice {topic}',
    input_variables=['topic']
)

template2=PromptTemplate(
    template='give a detailed report on this topic{text}',
    input_variables=['text']
)

template3=PromptTemplate(
    template='give a short summary of 5 lines on this topic {t}',
    input_variables=['t']
)

parser=StrOutputParser()

chain=template1  | model | parser | template2 | model | parser |template3 | model | parser

result=chain.invoke({'topic':'bajrangi bhaijan movie'})

print(result)

chain.get_graph().print_ascii()


