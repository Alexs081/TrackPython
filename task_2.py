-# TODO Найдите количество книг, которое можно разместить на дискете
information_volume = 1.44
pages = 100
line_numbers = 50
numbers_of_characters = 25
code_bytes = 4
information_volume_bytes = information_volume * 1024 * 1024
total_numbers = numbers_of_characters * line_numbers *pages
volume_book = total_numbers * code_bytes
total_books = int(information_volume_bytes // volume_book)
print("Количество книг, помещающихся на дискету:", total_books)
