import json

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def show_all_books(data_file):
    with open(data_file, "r", encoding='utf-8') as f:
        books_json = f.read()
    books = json.loads(books_json)

    book_on_page = []
    for book in books:
        book_on_page.append({
            'title': book['title'],
            'author': book['author'],
            'img_src': book['img_src'],
            'book_path': book['book_path'],
            'comments': book['comments'],
            'genres': book['genres'],
        })

    return book_on_page


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        books_file=show_all_books('meta_data.json'),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
