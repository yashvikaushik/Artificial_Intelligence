from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableBranch,RunnableLambda,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

prompt1=PromptTemplate(
    template='generate a report on this topic {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='count the number of words in this text {topic}',
    input_variables=['topic']
)


parser=StrOutputParser()

text_summarise=RunnableSequence(prompt1,model,parser)



chain=RunnableBranch(
    (lambda x:len(x.split())>500, RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(text_summarise,chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))