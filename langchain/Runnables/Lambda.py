from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableLambda
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

prompt1=PromptTemplate(
    template='write a joke about topic {topic}',
    input_variables=['topic']
)

model=ChatOpenAI()

parser=StrOutputParser()

prompt2=PromptTemplate(
    template='give the word count of this topic {topic}',
    input_variables=['topic']
)

joke_gen=RunnableSequence(prompt1,model,parser)



chain=RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'count':RunnableLambda(word_count)
    }
)

final_chain=RunnableSequence(joke_gen,chain)

print(final_chain.invoke({'topic':'student'}))



