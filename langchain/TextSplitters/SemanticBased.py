from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings 

from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)


sample= """
The mountains were covered in snow, and the air was cold and crisp. Travelers enjoyed the scenic beauty and peaceful environment while hiking through the trails. Nature provided a sense of calm and escape from busy city life.

Artificial Intelligence is transforming the technology industry. Companies are building smarter systems that can learn from data and make predictions. AI is being used in chatbots, recommendation systems, and automation tools.

Football is one of the most popular sports in the world. Millions of fans watch matches and support their favorite teams. Major tournaments like the FIFA World Cup bring countries together in celebration.

Cooking at home can be both relaxing and creative. People experiment with different ingredients and recipes to create delicious meals. It also promotes healthier eating habits compared to fast food.

Space exploration has always fascinated humans. Scientists are working on missions to Mars and beyond, aiming to discover new possibilities for life outside Earth.
"""


docs=text_splitter.create_documents([sample])

print(docs)