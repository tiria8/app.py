import logging

from flask import Blueprint, render_template, request
from loader.utils import upload_picture
from functions import write_post

POST_PATH = "posts.json"

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route('/post')

def get_post():
    return render_template('post_form.html')

@loader_blueprint.route('/post', methods=["POST"])

def add_post():
    picture = request.files.get("picture")
    content = request.form.get("content")

    if not picture or not content:
        return 'Ошибка загрузки'
    if picture.filename.split(".")[-1] not in ["jpeg", "png"]:
        logging.info('Неверное расширение файла')
        return 'Неверное расширение файла'

    try:
        pic_path = upload_picture(picture)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Ошибка обработки файла'
    post = write_post({'pic': pic_path, 'content': content}, POST_PATH)

    return render_template('post_uploaded.html', post=post)



