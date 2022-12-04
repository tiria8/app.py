import logging

from flask import Blueprint, render_template, request
from functions import load_posts_from_json, search

POST_PATH = "posts.json"


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def page_index():
    return render_template('index.html')

@main_blueprint.route("/search")
def search_page():
    s = request.args['s']
    logging.info('Идет поиск')

    try:
        result = search(POST_PATH, s)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Ошибка обработки файла'
    return render_template('post_list.html', search_word=s, search_result=result)