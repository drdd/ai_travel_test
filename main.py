from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


#client = OpenAI(api_key=os.getenv('API_OAI_KEY'))
#assistant = client.beta.assistants.retrieve(os.getenv('OAI_ASSISTANT_ID'))


app = Flask(__name__)

@app.route('/q', methods=['POST'])
def your_route():
    return jsonify({"msg": "ответ от опенАИ"}), 200
    # if request.is_json:
    #     data = request.get_json()
    #     if "uid" in data and "msg" in data:
    #         return jsonify({"msg": assistent_queary(data['uid'],data['msg'])}), 200
    #     return jsonify({"error": "uid или msg не задан"}), 400
    # else:
    #     return jsonify({"error": "Данные не в формате JSON"}), 400


# def assistent_queary(user_id, message):
#     thread = client.beta.threads.create()
#     client.beta.threads.messages.create(
#         thread_id=thread.id,
#         role="user",
#         content=message
#     )
#
#     run = client.beta.threads.runs.create_and_poll(
#         thread_id=thread.id,
#         assistant_id=assistant.id,
#         instructions="",
#     )
#
#     if run.status == "completed":
#         messages = client.beta.threads.messages.list(thread_id=thread.id)
#
#         for msg in messages:
#             assert msg.content[0].type == "text"
#             return msg.content[0].text.value

if __name__ == '__main__':
    app.run(debug=True)