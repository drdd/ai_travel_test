from flask import Flask, request, jsonify
from openai import OpenAI
import json
import urllib.parse


app = Flask(__name__)

@app.route('/t', methods=['POST'])
def get_thread():
    """
    Обрабатывает POST запросы на /t.

    Ожидаемые параметры JSON:
    - api_key (str): API ключь для OpenAI. Обязательный.
    """
    if request.is_json:
        data = request.get_json()
        if "api_key" in data:
            try:
                client = make_client_openai(data['api_key'])
                thread = client.beta.threads.create()
                return jsonify({"msg": "ok", "thread_id": f"{thread.id}"}), 200
            except Exception as e:
                return jsonify({"msg": "Неверный api_key"}), 400

@app.route('/g', methods=['POST'])
def get_message():
    """
    Получает последнее сообщение по thread_id POST /g.

    Ожидаемые параметры JSON:
    - api_key (str): API ключь для OpenAI. Обязательный.
    - assistant_id (str): ASSISTANT ID для OpenAI. Обязательный.
    - thread_id (str): thread_id для OpenAI. Обязательный.
    """
    if request.is_json:
        data = request.get_json()
        if "assistant_id" in data and "api_key" in data and "thread_id" in data:
            try:
                client = make_client_openai(data['api_key'])
                assistant = make_assistant_openai(client, data['assistant_id'])
                thread_id = get_exists_thread_id(client, data['thread_id'])
                if thread_id == "":
                    return jsonify({"msg": f"Ошибка потока OpenAI"}), 400
                answer = get_response(client, assistant, thread_id)

                answer = answer.replace("*","+")
                return jsonify({"msg": f'{answer}', "thread_id": f"{thread_id}"}), 200
            except Exception as e:
                return jsonify({"msg": f"Ошибка {e}"}), 400
        else:
            return jsonify({"msg": "Недостатачный пакет данных в запросе"}), 400
    else:
        return jsonify({"msg": "Данные не в формате JSON"}), 400

@app.route('/q', methods=['POST'])
def send_message():
    """
    Отправляет запрос на добавление вопроса к OpenAI /q.

    Ожидаемые параметры JSON:
    - api_key (str): API ключь для OpenAI. Обязательный.
    - assistant_id (str): ASSISTANT ID для OpenAI. Обязательный.
    - thread_id (str): thread_id для OpenAI. Обязательный.
    - msg (str): Текст сообщения для обработки OpenAI. Обязательный.
    """
    if request.is_json:
        data = request.get_json()
        if "assistant_id" in data and "api_key" in data and "thread_id" in data and "msg" in data:
            if data['msg'].strip() == "":
                return jsonify({"msg": "Повторите я не понял."}), 400
            else:
                try:
                    client = make_client_openai(data['api_key'])
                    assistant = make_assistant_openai(client, data['assistant_id'])
                    thread_id = get_exists_thread_id(client, data['thread_id'])
                    if thread_id == "":
                        return jsonify({"msg": f"Ошибка потока OpenAI"}), 400

                    assistent_queary(client, assistant, thread_id, data['msg'])
                    return jsonify({"msg": "ok", "thread_id": f"{thread_id}"}), 200
                except Exception as e:
                    return jsonify({"msg": f"Ошибка {e}"}), 400
        else:
            return jsonify({"msg": "Недостатачный пакет данных в запросе"}), 400
    else:
        return jsonify({"msg": "Данные не в формате JSON"}), 400

def make_client_openai(api_key):
    client = OpenAI(api_key=api_key)
    return client
def make_assistant_openai(client, assistant_id):
    assistant = client.beta.assistants.retrieve(assistant_id)
    return assistant

def get_exists_thread_id(client, thread_id):
    try:
        thread = client.beta.threads.retrieve(thread_id=thread_id)
        if thread:
            return thread_id
    except Exception as e:
        try:
            error_type = e.response.json()['error']['type']
            if error_type == 'invalid_request_error':
                thread = client.beta.threads.create()
                return thread.id
        except (AttributeError, KeyError):
            return ""
        return ""

def assistent_queary(client, assistant, thread_id, message):
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message
    )
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant.id,
        instructions=""
    )

def get_response(client, assistant, thread_id):
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant.id,
        instructions=""
    )

    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(run_id=run.id, thread_id=thread_id)

    if run.status == "completed":
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        for msg in messages:
            if msg.content[0].type == "text":
                return msg.content[0].text.value


if __name__ == '__main__':
    app.run(debug=True)