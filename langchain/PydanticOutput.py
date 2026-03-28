from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated,Optional,List
import json
from pydantic import BaseModel,Field
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4o-mini')

#schema
class Review(BaseModel):
    key_themes:List[str]=Field(description='mention the key themes of the movie in a list')
    summary :str=Field('give the summary')
    pros:Optional[List[str]]=Field('mention the pros of the movie in a list')
    cons:Optional[list[str]]=Field('mention the cons of the movie in a list')
    name:str=Field('mention the name of the reviewer')

final_model=model.with_structured_output(Review)

result=final_model.invoke(
    '''
Reviewed by Yashvi Inception is a sci-fi thriller that explores themes of reality vs illusion, guilt, and the power of ideas, following a man who enters dreams to steal secrets but is instead given the task of planting an idea in someone’s mind. The story feels engaging and thought-provoking, though slightly complex at times, which keeps you attentive throughout. The overall sentiment is very positive because of its originality and strong execution. Its main pros are the unique concept, powerful performances, and visually impressive scenes, while the cons include moments of confusion and a storyline that can be difficult to fully understand on the first watch. Overall, it is a compelling and creative film that is definitely worth watching.
'''
)
#json_output=json.dumps(result,indent=4)
print(result)

