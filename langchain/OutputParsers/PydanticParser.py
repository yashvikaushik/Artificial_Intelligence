from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
 
load_dotenv()

class person(BaseModel):
    name:str =Field(description='name of the person')
    age:int=Field(description='age of person',gt=18)
    city:str=Field(description='city of the person')

model=ChatOpenAI(model="gpt-4o-mini",temperature=1)

parser=PydanticOutputParser(pydantic_object=person)

template=PromptTemplate(
    template='give the name,age,city of the bollywood celebrity{name} \n {format_instructions}',
    input_variables=['name'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

#prompt=template.invoke({'name':'salman khan'})

chain=template | model | parser

print(chain.invoke({'name':'salman khan'}))