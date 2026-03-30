from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
 
load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini",temperature=1)

Jparser=JsonOutputParser()

#template1
template1=PromptTemplate(
    template='tell me the name,age,city, famous movie of a fictional person from bollywood and also the name of the actor \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':Jparser.get_format_instructions()}
)

prompt=template1.format()

chain=template1 | model | Jparser

print(chain.invoke({}))


# print("------PROMPT------")
# print(prompt)
# print("------------------")




