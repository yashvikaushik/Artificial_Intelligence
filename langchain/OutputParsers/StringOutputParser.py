from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
 
load_dotenv()

model=ChatOpenAI(model="gpt-4",temperature=0.4)

#template1
template1=PromptTemplate(
    template='write a detailed summary on {topic}',
    input_variables=['topic']
)

#template2
template2=PromptTemplate(
    template='write a five line summary of {text}',
    input_variables=['text']
)

#without output pareser
# Prompt1=template1.invoke({'topic':'black hole'})
# result1=model.invoke(Prompt1)

# Prompt2=template2.invoke({'text':result1.content})

# result2=model.invoke(Prompt2)

# print(result2.content)

Sparser=StrOutputParser()

chain=template1 | model | Sparser | template2 | model |Sparser 

result=chain.invoke({'topic':'black hole'})

print(result)






