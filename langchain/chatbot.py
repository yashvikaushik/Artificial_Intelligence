from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

model=ChatOpenAI()
memory=[
    SystemMessage(content='You are a helpful AI assistant')
]
while True:
    user_input=input('you: ')
    memory.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break

    result=model.invoke(memory)
    memory.append(AIMessage(content=result.content))

    print('AI: ',result.content)

print(memory)


