from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template='write a joke about topic {topic}',
    input_variables=['topic']
)

model=ChatOpenAI()

parser=StrOutputParser()

prompt2=PromptTemplate(
    template='explain this joke {topic}',
    input_variables=['topic']
)

joke_gen=RunnableSequence(prompt1,model,parser)


chain=RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'explaination':RunnableSequence(prompt1,model,parser,prompt2,model,parser)
    }
)

final_chain=RunnableSequence(joke_gen,chain)

print(final_chain.invoke({'topic':'student'}))

# print(result1)
# print('********************EXPLAINATION**********************')
# print(result2)

