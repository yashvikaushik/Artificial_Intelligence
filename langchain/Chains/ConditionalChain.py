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


model=ChatOpenAI(model='gpt-4')

prompt1=PromptTemplate(
    template='classify the user feedback as positive or negative {text},{format_instructions}',
    input_variables=['text'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain=prompt1 | model | parser 

print(chain.invoke({'text':'this is a terrible phone'}).feedback)

print(chain)


