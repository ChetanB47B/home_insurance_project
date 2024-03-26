import os

from dotenv import load_dotenv
from openai import OpenAI

from questions import QUESTION

load_dotenv()

openai_key = os.environ.get('OPENAI_API_KEY')
# print(f'openai ---  {openai_key}')
client = OpenAI()


def data_filter(option, base64_encoded_image):
    print(option)
    SYS_PROMPT = QUESTION[option]
    completion = client.chat.completions.create(
        model="gpt-4-vision-preview",
        temperature=0.35,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": SYS_PROMPT},
                    {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_encoded_image}"}
                ]
            }
        ],
    )
    try:
        reply = completion.choices[0].message.content
        # if isinstance(reply, dict):
        #     return reply
        # else:
        #     return "Sorry I'm Not able to Answer at this time"
        return reply
    except:
        reply = "Sorry I'm Not able to Answer at this time"
        return reply
