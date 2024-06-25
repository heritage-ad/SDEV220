from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {
        'id': 1,
        'book_name': 'The Midnight Library',
        'author': 'Matt Haig',
        'publisher': 'Canongate Books'
    },
    {
        'id': 2,
        'book_name': 'Where the Crawdads Sing',
        'author': 'Delia Owens',
        'publisher': 'G.P Putnam\'s Sons'
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book)

@app.route('/books', methods=['POST'])
def add_book():
    new_id = books[-1]['id'] + 1 if books else 1
    book = {
        'id': new_id,
        'book_name': request.json['book_name'],
        'author': request.json['author'],
        'publisher': request.json['publisher']
    }
    books.append(book)
    return jsonify(book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    book['book_name'] = request.json.get('book_name', book['book_name'])
    book['author'] = request.json.get('author', book['author'])
    book['publisher'] = request.json.get('publisher', book['publisher'])
    return jsonify(book)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    books.remove(book)
    return jsonify({'result': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
