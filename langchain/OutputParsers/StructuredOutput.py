# deprecated version




# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain.output_parsers import StructuredOutputParser, ResponseSchema
 
# load_dotenv()

# model=ChatOpenAI(model="gpt-4o-mini",temperature=1)

# schema = [
#     ResponseSchema(name='fact1',description='fact 1 about the topic'),
#     ResponseSchema(name='fact2',description='fact 2 about the topic'),
#     ResponseSchema(name='fact3',description='fact 3 about the topic')
# ]
# parser=StructuredOutputParser.from_response_schemas(schema)
# #template1
# template1=PromptTemplate(
#     template='give me three facts about the topic {topic}\n {format_instructions}',
#     input_variables=['topic'],
#     partial_variables={'format_instructions':parser.get_format_instructions()}
# )

# prompt=template1.invoke({'topic':'sun'})

# chain=template1 | model | parser

# print(chain.invoke({}))


# # print("------PROMPT------")
# # print(prompt)
# # print("------------------")




