from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatOpenAI(model='gpt-4')

template=PromptTemplate(
    template='what is the capital of {country}',
    input_variables=['country']
)

chain=template | model 

result=chain.invoke({'country':'India'})
print(result.content)

chain.get_graph().print_ascii()