import json

def load_posts_from_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

def search(path, search_word):
    posts_to_show = []

    for post in load_posts_from_json(path):
        if search_word.lower() in post['content'].lower():
            posts_to_show.append(post)
    return posts_to_show

def write_post(post, path):
    posts = load_posts_from_json(path)
    posts.append(post)

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post


