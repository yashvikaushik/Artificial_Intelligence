from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import json
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4o-mini')



#schema
json_schema={
  "title": "movie_review_schema",
  "description": "Schema for structured movie review output",
  "type": "object",
  "properties": {
    "movie": {
      "type": "object",
      "properties": {
        "title": { "type": "string" },
        "release_year": { "type": "integer" },
        "genre": {
          "type": "array",
          "items": { "type": "string" }
        },
        "duration_minutes": { "type": "integer" },
        "language": { "type": "string" }
      },
      "required": ["title", "release_year"]
    },
    "review": {
      "type": "object",
      "properties": {
        "reviewer_name": { "type": "string" },
        "rating": {
          "type": "number",
          "minimum": 0,
          "maximum": 10
        },
        "summary": { "type": "string" },
        "pros": {
          "type": "array",
          "items": { "type": "string" }
        },
        "cons": {
          "type": "array",
          "items": { "type": "string" }
        },
        "verdict": { "type": "string" }
      },
      "required": ["rating", "summary"]
    },
    "cast": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "actor": { "type": "string" },
          "character": { "type": "string" }
        },
        "required": ["actor"]
      }
    },
    "technical_details": {
      "type": "object",
      "properties": {
        "director": { "type": "string" },
        "writer": { "type": "string" },
        "music_director": { "type": "string" },
        "cinematography": { "type": "string" },
        "production_company": { "type": "string" }
      }
    },
    "analysis": {
      "type": "object",
      "properties": {
        "story": { "type": "string" },
        "acting": { "type": "string" },
        "direction": { "type": "string" },
        "music": { "type": "string" },
        "visuals": { "type": "string" }
      }
    },
    "recommendation": {
      "type": "object",
      "properties": {
        "recommended": { "type": "boolean" },
        "target_audience": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    }
  },
  "required": ["movie", "review"]
}

final_model=model.with_structured_output(json_schema)

result=final_model.invoke(
    '''
Reviewed by Yashvi Inception is a sci-fi thriller that explores themes of reality vs illusion, guilt, and the power of ideas, following a man who enters dreams to steal secrets but is instead given the task of planting an idea in someone’s mind. The story feels engaging and thought-provoking, though slightly complex at times, which keeps you attentive throughout. The overall sentiment is very positive because of its originality and strong execution. Its main pros are the unique concept, powerful performances, and visually impressive scenes, while the cons include moments of confusion and a storyline that can be difficult to fully understand on the first watch. Overall, it is a compelling and creative film that is definitely worth watching.
'''
)
#json_output=json.dumps(result,indent=4)
print(result)

