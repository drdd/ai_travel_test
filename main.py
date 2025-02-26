from flask import Flask, request, jsonify
from openai import OpenAI
import json

app = Flask(__name__)

@app.route('/test_j', methods=['GET'])
def get_test_j():
    st = json.dumps("Отлично, спасибо за информацию! Сейчас я подберу для вас несколько вариантов туров в Батуми на март. Пожалуйста, подождите немного. \n\n(Проверка базы данных туров...)\n\nВот несколько вариантов туров в Батуми на март:\n\n1. **Тур \"Весенний Батуми\"**\n   - **Даты:** 5 марта - 12 марта\n   - **Количество участников:** 1 взрослый\n   - **Стоимость:** 500 долларов + 1,200 белорусских рублей\n   - **Описание:** Этот тур включает проживание в отеле 4*, экскурсии по Батуми и окрестностям, а также дегустацию местной кухни.\n\n2. **Тур \"Культурное погружение\"**\n   - **Даты:** 10 марта - 17 марта\n   - **Количество участников:** 1 взрослый\n   - **Стоимость:** 550 долларов + 1,100 белорусских рублей\n   - **Описание:** Включает посещение музеев, исторических мест и культурных мероприятий в Батуми. Проживание в отеле 3*.\n\n3. **Тур \"Активный отдых в Батуми\"**\n   - **Даты:** 15 марта - 22 марта\n   - **Количество участников:** 1 взрослый\n   - **Стоимость:** 600 долларов + 1,000 белорусских рублей\n   - **Описание:** Программа включает в себя активные виды отдыха: походы, велосипедные туры и водные виды спорта. Проживание в отеле 4*.\n\n4. **Тур \"Релакс и SPA\"**\n   - **Даты:** 20 марта - 27 марта\n   - **Количество участников:** 1 взрослый\n   - **Стоимость:** 650 долларов + 950 белорусских рублей\n   - **Описание:** Расслабляющий отдых с посещением SPA-комплексов, термальных источников и массажных процедур. Проживание в отеле 5*.\n\nЕсли какой-либо из этих вариантов вас заинтересовал или у вас есть дополнительные вопросы, пожалуйста, дайте знать!")
    return jsonify({"msg": st,
                    "thread_id": "thread_yev8zzPUofUPCPppgWEn6qLP"}), 200
@app.route('/test_f', methods=['GET'])
def get_test_f():
    return jsonify({"msg": 'Отлично, спасибо за информацию! Сейчас я подберу для вас несколько вариантов туров в Батуми на март. Пожалуйста, подождите немного. \n\n(Проверка базы данных туров...)\n\nВот несколько вариантов туров в Батуми на март:\n\n1. **Тур \"Весенний Батуми\"**\n   - **Даты:** 5 марта - 12 марта\n   - **Количество участников:** 1 взрослый\n   - **Стоимость:** 500 долларов + 1,200 белорусских рублей\n   - **Описание:** Этот тур включает проживание в отеле 4*, экскурсии по Батуми и окрестностям, а также дегустацию местной кухни.\n\n2. **Тур \"Культурное погружение\"**\n   - **Даты:** 10 марта - 17 марта\n   - **Количество участников:** 1 взрослый\n   - **Стоимость:** 550 долларов + 1,100 белорусских рублей\n   - **Описание:** Включает посещение музеев, исторических мест и культурных мероприятий в Батуми. Проживание в отеле 3*.\n\n3. **Тур \"Активный отдых в Батуми\"**\n   - **Даты:** 15 марта - 22 марта\n   - **Количество участников:** 1 взрослый\n   - **Стоимость:** 600 долларов + 1,000 белорусских рублей\n   - **Описание:** Программа включает в себя активные виды отдыха: походы, велосипедные туры и водные виды спорта. Проживание в отеле 4*.\n\n4. **Тур \"Релакс и SPA\"**\n   - **Даты:** 20 марта - 27 марта\n   - **Количество участников:** 1 взрослый\n   - **Стоимость:** 650 долларов + 950 белорусских рублей\n   - **Описание:** Расслабляющий отдых с посещением SPA-комплексов, термальных источников и массажных процедур. Проживание в отеле 5*.\n\nЕсли какой-либо из этих вариантов вас заинтересовал или у вас есть дополнительные вопросы, пожалуйста, дайте знать!',
                    "thread_id": "thread_yev8zzPUofUPCPppgWEn6qLP"}), 200

@app.route('/test_p', methods=['GET'])
def get_test_p():
    return jsonify({"msg": "Отлично, спасибо за информацию!\n\n Сейчас я подберу для вас несколько вариантов туров в Батуми на март. Пожалуйста, подождите немного. (Проверка базы данных туров...)Вот несколько вариантов туров в Батуми на март:1. **Тур Весенний Батуми**   - **Даты:** 5 марта - 12 марта   - **Количество участников:** 1 взрослый   - **Стоимость:** 500 долларов + 1,200 белорусских рублей   - **Описание:** Этот тур включает проживание в отеле 4*, экскурсии по Батуми и окрестностям, а также дегустацию местной кухни.2. **Тур Культурное погружение**   - **Даты:** 10 марта - 17 марта   - **Количество участников:** 1 взрослый   - **Стоимость:** 550 долларов + 1,100 белорусских рублей   - **Описание:** Включает посещение музеев, исторических мест и культурных мероприятий в Батуми. Проживание в отеле 3*.3. **Тур Активный отдых в Батуми**   - **Даты:** 15 марта - 22 марта  - **Количество участников:** 1 взрослый   - **Стоимость:** 600 долларов + 1,000 белорусских рублей   - **Описание:** Программа включает в себя активные виды отдыха: походы, велосипедные туры и водные виды спорта. Проживание в отеле 4*.4. **Тур Релакс и SPA**   - **Даты:** 20 марта - 27 марта   - **Количество участников:** 1 взрослый   - **Стоимость:** 650 долларов + 950 белорусских рублей   - **Описание:** Расслабляющий отдых с посещением SPA-комплексов, термальных источников и массажных процедур. Проживание в отеле 5*.Если какой-либо из этих вариантов вас заинтересовал или у вас есть дополнительные вопросы, пожалуйста, дайте знать!",
                    "thread_id": "thread_yev8zzPUofUPCPppgWEn6qLP"}), 200

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
                return jsonify({"msg": f"{answer}", "thread_id": f"{thread_id}"}), 200
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

                    assistent_queary(client, thread_id, data['msg'])
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

def assistent_queary(client, thread_id, message):
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message
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