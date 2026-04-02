from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

prompt=PromptTemplate(
    template='answer these questions {questions} from the following text {text}',
    input_variables=['questions','text']
)


url='https://economictimes.indiatimes.com/news/international/global-trends/who-is-sunita-williams-all-about-veteran-nasa-astronauts-life-and-her-remarkable-journey-to-space-sunita-williams-husband-salary-net-worth-experience/articleshow/118942392.cms?from=mdr'

loader=WebBaseLoader(url)

docs=loader.load()

chain=prompt | model | parser

result=chain.invoke({'questions':"when and where was sunita born?",'text':docs[0].page_content})

print(result)