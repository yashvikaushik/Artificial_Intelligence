from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

prompt=PromptTemplate(
    template='give all the most important points from the following text {text}',
    input_variables=['text']
)

loader=TextLoader(file_path='sam_altman.txt',encoding='utf=8')
docs=loader.load()

print(docs[0].page_content)

print(docs[0].metadata)

chain=prompt | model |parser

result=chain.invoke({'text':docs[0].page_content})

print('---------------------------------------------------------------------')

print(result)