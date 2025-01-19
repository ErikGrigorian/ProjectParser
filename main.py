# 4 вариант составьте парсер, который собирает названия книг и цену с первой страницы раздела классической литературы. используйте пакет bs4. http://books.toscrape.com/catalogue/category/books/classics_6/index.html  (минимум две функции)
import requests
# используется для отправки запроса на сервер и получения данных
from bs4 import BeautifulSoup
# beautifulsoup является частью библиотеки bs4. помогает получать данные с веб-страницы
from parser  import parse_classics_page, get_page_content
def main():
    """
    Основная функция, которая выполняет процесс извлечения данных о книгах.
    """
    # URL страницы с классическими книгами
    url = 'http://books.toscrape.com/catalogue/category/books/classics_6/index.html'

    # Извлекаем названия книг и их цены
    titles,prices = parse_classics_page(url)

    # Выводим названия книг и их цены
    print("Книги и их цены:")
    for title, price in zip(titles, prices):
        print(f"Название: {title}, Цена: {price}")

if __name__ == "__main__":
    main()



