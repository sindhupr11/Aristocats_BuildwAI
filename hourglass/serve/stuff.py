from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()

genai.configure(api_key="AIzaSyCnxYh65pGuXFIYFLGN45hAFbkDtaem3zs")
class Item(BaseModel):
    curr_sc: str = "{\n  \"Monday\": [\n    { \"time\": [2, 2.5], \"task\": \"swimming\" },\n    { \"time\": [2.5, 3.5], \"task\": \"Language\" },\n    { \"time\": [3.5, 4], \"task\": \"free\" }\n  ],\n  \"Tuesday\": [\n    { \"time\": [2, 3], \"task\": \"Language\" },\n    { \"time\": [3, 4], \"task\": \"swimming\" },\n    { \"time\": [4, 5], \"task\": \"free\" }\n  ],\n  \"Wednesday\": [\n    { \"time\": [2, 2.5], \"task\": \"free\" },\n    { \"time\": [2.5, 3.5], \"task\": \"swimming\" },\n    { \"time\": [3.5, 4], \"task\": \"Language\" }\n  ],\n  \"Thursday\": [\n    { \"time\": [2, 3], \"task\": \"Language\" },\n    { \"time\": [3, 4], \"task\": \"swimming\" },\n    { \"time\": [4, 5], \"task\": \"free\" }\n  ],\n  \"Friday\": [\n    { \"time\": [2, 2.5], \"task\": \"swimming\" },\n    { \"time\": [2.5, 3.5], \"task\": \"Language\" },\n    { \"time\": [3.5, 4], \"task\": \"free\" }\n  ],\n  \"Saturday\": [\n    { \"time\": [2, 3], \"task\": \"free\" },\n    { \"time\": [3, 4], \"task\": \"swimming\" },\n    { \"time\": [4, 5], \"task\": \"Language\" }\n  ],\n  \"Sunday\": [\n    { \"time\": [2, 2.5], \"task\": \"Language\" },\n    { \"time\": [2.5, 3.5], \"task\": \"swimming\" },\n    { \"time\": [3.5, 4], \"task\": \"free\" }\n  ]\n}"
    act_name: str = "Shopping"
    mtpd: int = 40
    mtpw: int = 280

@app.post("/generate_schedule/")
async def generate_schedule(item: Item):

    prompt_parts = [
    "Current Schedule:  {\n\"Monday\":[{\"time\":[2,4], \"task\":\"free\"}, {\"time\":[4,5], \"task\":\"workout\"},{\"time\":[5,6], \"task\":\"study\"}],\n\"Tuesday\":[{\"time\":[2,3], \"task\":\"study\"}, {\"time\":[4,5], \"task\":\"workout\"},{\"time\":[5,6], \"task\":\"free\"}],\n\"Wednesday\":[{\"time\":[2,3], \"task\":\"study\"}, {\"time\":[4,5], \"task\":\"workout\"},{\"time\":[5,6], \"task\":\"free\"}],\n\"Thursday\":[{\"time\":[2,3], \"task\":\"workout\"}, {\"time\":[4,6], \"task\":\"study\"}],\n\"Friday\":[{\"time\":[2,4], \"task\":\"free\"}, {\"time\":[4,5],  \"task\":\"workout\"},{\"time\":[5,6], \"task\":\"study\"}],\n\"Saturday\":[{\"time\":[2,4], \"task\":\"free\"}, {\"time\":[4,6], \"task\":\"study\"}],\n\"Sunday\":[{\"time\":[2,3], \"task\":\"study\"}, {\"time\":[4,6], \"task\":\"free\"}]\n}",
    "New Activity Name: Assignment",
    "Max min per day: 60",
    "Max min per week: 240",
    "output: {\n  \"Monday\": [\n    { \"time\": [2, 3.3], \"task\": \"free\" },\n    { \"time\": [3.3, 4.3], \"task\": \"Assignment\" }, \n    { \"time\": [4.3, 5], \"task\": \"workout\" },\n    { \"time\": [5, 6], \"task\": \"study\" }\n  ],\n  \"Tuesday\": [\n    { \"time\": [2, 2.3], \"task\": \"study\" },\n    { \"time\": [2.3, 3.3], \"task\": \"Assignment\" },\n    { \"time\": [3.3, 4], \"task\": \"workout\" },\n    { \"time\": [4, 5], \"task\": \"free\" },\n    { \"time\": [5, 6], \"task\": \"free\" }\n  ],\n  \"Wednesday\": [\n    { \"time\": [2, 3], \"task\": \"study\" },\n    { \"time\": [3, 4], \"task\": \"workout\" },\n    { \"time\": [4, 5], \"task\": \"free\" }, \n    { \"time\": [5, 5.3], \"task\": \"Assignment\" }, \n    { \"time\": [5.3, 6], \"task\": \"free\" }\n  ],\n  \"Thursday\": [\n    { \"time\": [2, 3], \"task\": \"workout\" }, \n    { \"time\": [3, 4], \"task\": \"Assignment\" }, \n    { \"time\": [4, 6], \"task\": \"study\" }\n  ],\n  \"Friday\": [\n    { \"time\": [2, 4], \"task\": \"free\" },\n    { \"time\": [4, 5], \"task\": \"workout\" },\n    { \"time\": [5, 6], \"task\": \"study\" }\n  ],\n  \"Saturday\": [\n    { \"time\": [2, 4], \"task\": \"free\" },\n    { \"time\": [4, 6], \"task\": \"study\" }\n  ],\n  \"Sunday\": [\n    { \"time\": [2, 3], \"task\": \"study\" },\n    { \"time\": [3, 4.3], \"task\": \"Assignment\" },\n    { \"time\": [4.3, 6], \"task\": \"free\" }\n  ]\n}",
    "Current Schedule:  {\n\"Monday\": [\n{ \"time\": [2, 2.3], \"task\": \"free\" },\n{ \"time\": [2.3, 3], \"task\": \"Meeting\" },\n{ \"time\": [3, 4], \"task\": \"workout\" },\n{ \"time\": [4, 5], \"task\": \"study\" }\n],\n\"Tuesday\": [\n{ \"time\": [2, 2.3], \"task\": \"study\" },\n{ \"time\": [2.3, 3.3], \"task\": \"Meeting\" },\n{ \"time\": [3.3, 4], \"task\": \"workout\" },\n{ \"time\": [4, 5], \"task\": \"free\" },\n{ \"time\": [5, 6], \"task\": \"free\" }\n],\n\"Wednesday\": [\n{ \"time\": [2, 3], \"task\": \"study\" },\n{ \"time\": [3, 3.3], \"task\": \"Meeting\" },\n{ \"time\": [3.3, 4], \"task\": \"workout\" },\n{ \"time\": [4, 4.3], \"task\": \"free\" },\n{ \"time\": [4.3, 5], \"task\": \"Meeting\" },\n{ \"time\": [5, 6], \"task\": \"free\" }\n],\n\"Thursday\": [\n{ \"time\": [2, 2.3], \"task\": \"workout\" },\n{ \"time\": [2.3, 3.3], \"task\": \"Meeting\" },\n{ \"time\": [3.3, 6], \"task\": \"study\" }\n],\n\"Friday\": [\n{ \"time\": [2, 4], \"task\": \"free\" },\n{ \"time\": [4, 4.3], \"task\": \"Meeting\" },\n{ \"time\": [4.3, 5], \"task\": \"workout\" },\n{ \"time\": [5, 6], \"task\": \"study\" }\n],\n\"Saturday\": [\n{ \"time\": [2, 4], \"task\": \"free\" },\n{ \"time\": [4, 6], \"task\": \"study\" }\n],\n\"Sunday\": [\n{ \"time\": [2, 3], \"task\": \"study\" },\n{ \"time\": [3, 3.3], \"task\": \"Meeting\" },\n{ \"time\": [3.3, 6], \"task\": \"free\" }\n]\n}",
    "New Activity Name: Learn Instrument",
    "Max min per day: 45",
    "Max min per week: 315",
    "output: {\n  \"Monday\": [\n    { \"time\": [2, 2.3], \"task\": \"free\" },\n    { \"time\": [2.3, 3], \"task\": \"Meeting\" },\n    { \"time\": [3, 3.45], \"task\": \"Learn Instrument\" },\n    { \"time\": [3.45, 4], \"task\": \"workout\" },\n    { \"time\": [4, 5], \"task\": \"study\" }\n  ],\n  \"Tuesday\": [\n    { \"time\": [2, 2.3], \"task\": \"study\" },\n    { \"time\": [2.3, 3.3], \"task\": \"Meeting\" },\n    { \"time\": [3.3, 3.45], \"task\": \"Learn Instrument\" },\n    { \"time\": [3.45, 4], \"task\": \"workout\" },\n    { \"time\": [4, 5], \"task\": \"free\" },\n    { \"time\": [5, 6], \"task\": \"free\" }\n  ],\n  \"Wednesday\": [\n    { \"time\": [2, 3], \"task\": \"study\" },\n    { \"time\": [3, 3.3], \"task\": \"Meeting\" },\n    { \"time\": [3.3, 3.45], \"task\": \"Learn Instrument\" },\n    { \"time\": [3.45, 4], \"task\": \"workout\" },\n    { \"time\": [4, 4.3], \"task\": \"free\" },\n    { \"time\": [4.3, 5], \"task\": \"Meeting\" },\n    { \"time\": [5, 6], \"task\": \"free\" }\n  ],\n  \"Thursday\": [\n    { \"time\": [2, 2.3], \"task\": \"workout\" },\n    { \"time\": [2.3, 3.3], \"task\": \"Meeting\" },\n    { \"time\": [3.3, 3.45], \"task\": \"Learn Instrument\" },\n    { \"time\": [3.45, 6], \"task\": \"study\" }\n  ],\n  \"Friday\": [\n    { \"time\": [2, 2.45], \"task\": \"free\" },\n    { \"time\": [2.45, 4], \"task\": \"Learn Instrument\" },\n    { \"time\": [4, 4.3], \"task\": \"Meeting\" },\n    { \"time\": [4.3, 5], \"task\": \"workout\" },\n    { \"time\": [5, 6], \"task\": \"study\" }\n  ],\n  \"Saturday\": [\n    { \"time\": [2, 2.45], \"task\": \"free\" },\n    { \"time\": [2.45, 4], \"task\": \"Learn Instrument\" },\n    { \"time\": [4, 6], \"task\": \"study\" }\n  ],\n  \"Sunday\": [\n    { \"time\": [2, 3], \"task\": \"study\" },\n    { \"time\": [3, 3.3], \"task\": \"Meeting\" },\n    { \"time\": [3.3, 3.45], \"task\": \"Learn Instrument\" },\n    { \"time\": [3.45, 6], \"task\": \"free\" }\n  ]\n}",
    "Current Schedule:  {\n  \"Monday\": [\n    { \"time\": [2, 2.5], \"task\": \"running\" },\n    { \"time\": [2.5, 3.5], \"task\": \"cleaning\" },\n    { \"time\": [3.5, 4], \"task\": \"free\" }\n  ],\n  \"Tuesday\": [\n    { \"time\": [2, 3], \"task\": \"cleaning\" },\n    { \"time\": [3, 4], \"task\": \"running\" },\n    { \"time\": [4, 5], \"task\": \"free\" }\n  ],\n  \"Wednesday\": [\n    { \"time\": [2, 2.5], \"task\": \"free\" },\n    { \"time\": [2.5, 3.5], \"task\": \"running\" },\n    { \"time\": [3.5, 4], \"task\": \"cleaning\" }\n  ],\n  \"Thursday\": [\n    { \"time\": [2, 3], \"task\": \"cleaning\" },\n    { \"time\": [3, 4], \"task\": \"running\" },\n    { \"time\": [4, 5], \"task\": \"free\" }\n  ],\n  \"Friday\": [\n    { \"time\": [2, 2.5], \"task\": \"running\" },\n    { \"time\": [2.5, 3.5], \"task\": \"cleaning\" },\n    { \"time\": [3.5, 4], \"task\": \"free\" }\n  ],\n  \"Saturday\": [\n    { \"time\": [2, 3], \"task\": \"free\" },\n    { \"time\": [3, 4], \"task\": \"running\" },\n    { \"time\": [4, 5], \"task\": \"cleaning\" }\n  ],\n  \"Sunday\": [\n    { \"time\": [2, 2.5], \"task\": \"cleaning\" },\n    { \"time\": [2.5, 3.5], \"task\": \"running\" },\n    { \"time\": [3.5, 4], \"task\": \"free\" }\n  ]\n}",
    "New Activity Name: Read Book",
    "Max min per day: 30",
    "Max min per week: 210",
    "output: {\n  \"Monday\": [\n    { \"time\": [2, 2.5], \"task\": \"running\" },\n    { \"time\": [2.5, 3.2], \"task\": \"cleaning\" },\n    { \"time\": [3.2, 3.5], \"task\": \"Read Book\" },\n    { \"time\": [3.5, 4], \"task\": \"free\" }\n  ],\n  \"Tuesday\": [\n    { \"time\": [2, 2.5], \"task\": \"cleaning\" },\n    { \"time\": [2.5, 3], \"task\": \"Read Book\" },\n    { \"time\": [3, 4], \"task\": \"running\" },\n    { \"time\": [4, 5], \"task\": \"free\" }\n  ],\n  \"Wednesday\": [\n    { \"time\": [2, 2.5], \"task\": \"free\" },\n    { \"time\": [2.5, 3.5], \"task\": \"running\" },\n    { \"time\": [3.5, 4], \"task\": \"cleaning\" }\n  ],\n  \"Thursday\": [\n    { \"time\": [2, 2.5], \"task\": \"cleaning\" },\n    { \"time\": [2.5, 3], \"task\": \"Read Book\" },\n    { \"time\": [3, 4], \"task\": \"running\" },\n    { \"time\": [4, 5], \"task\": \"free\" }\n  ],\n  \"Friday\": [\n    { \"time\": [2, 2.5], \"task\": \"running\" },\n    { \"time\": [2.5, 3.2], \"task\": \"cleaning\" },\n    { \"time\": [3.2, 3.5], \"task\": \"Read Book\" },\n    { \"time\": [3.5, 4], \"task\": \"free\" }\n  ],\n  \"Saturday\": [\n    { \"time\": [2, 2.5], \"task\": \"free\" },\n    { \"time\": [2.5, 3], \"task\": \"Read Book\" },\n    { \"time\": [3, 4], \"task\": \"running\" },\n    { \"time\": [4, 5], \"task\": \"cleaning\" }\n  ],\n  \"Sunday\": [\n    { \"time\": [2, 2.5], \"task\": \"cleaning\" },\n    { \"time\": [2.5, 3], \"task\": \"Read Book\" },\n    { \"time\": [3, 3.5], \"task\": \"running\" },\n    { \"time\": [3.5, 4], \"task\": \"free\" }\n  ]\n}",
    ]
    new = [
        "Current Schedule:  " + item.curr_sc,
    "New Activity Name: " + item.act_name,
    "Max min per day: " + str(item.mtpd),
    "Max min per week: "+ str(item.mtpw) ,
    "output: ",
    ]
    prompt_parts.extend(new)
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    response = model.generate_content(prompt_parts)
    response = response.text.split("```json")[1].split("```")[0]
    
    return {"output": response}
