#necessary libraries
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal
import streamlit as st


load_dotenv()

model=ChatOpenAI(model='gpt-4')

class text(BaseModel):
    sentiments:Literal['positive','negative'] =Field(description='give the sentiments of the given feedback')


parser1=PydanticOutputParser(pydantic_object=text)
parser2=StrOutputParser()

prompt1=PromptTemplate(
    template='classify the following feedback as positive or negative only do not use anything like neutral it has to be strict ' \
    
    ' {feedback}. ' \
    
    '{format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser1.get_format_instructions()}
)

prompt2=PromptTemplate(
    template='give a response for this positive feedback {feedback}',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='give a response for this negative feedback {feedback}',
    input_variables=['feedback']
)

base_chain=prompt1 | model | parser1

chain=RunnableBranch(
    (lambda x:x.sentiments=='positive',prompt2 | model | parser2),
    (lambda x:x.sentiments=='negative',prompt3 | model | parser2 ),
    RunnableLambda(lambda x:'not a valuable feedback')
)

final_chain=base_chain | chain

# result=final_chain.invoke({'feedback':'this phone is terrible'})

st.title("💬 AI Feedback Analyzer")
st.info("Enter feedback and get sentiment + AI response")

user_input = st.text_area("Enter your feedback here...")

if st.button("Analyze"):
    if user_input.strip():

        # Step 1: sentiment
        sentiment_obj = base_chain.invoke({'feedback': user_input})
        sentiment = sentiment_obj.sentiments

        # Step 2: response
        result = final_chain.invoke({'feedback': user_input})

        # Step 3: display
        if sentiment == "positive":
            st.success(f"😊 Positive Feedback\n\n{result}")
        else:
            st.error(f"😡 Negative Feedback\n\n{result}")

    else:
        st.warning("Please enter feedback!")