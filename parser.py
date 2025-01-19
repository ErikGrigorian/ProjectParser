import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

def get_page_content(url):
    """
    Запрашивает содержимое HTML-страницы по указанному URL и возвращает его.

    :param url: Строка, представляющая URL страницы для запроса.
    :return: Содержимое страницы, если запрос успешен, иначе None.
    """
    # Отправляем GET-запрос к указанному URL
    response = requests.get(url)

    # Проверяем, был ли запрос успешным
    if response.status_code == 200:
        # Если успешный ответ, возвращаем содержимое страницы
        return response.content
    else:
        # Если произошла ошибка, выводим код статуса
        print(f"Ошибка {response.status_code}: Не удалось получить содержимое страницы {url}.")
        return None

def parse_classics_page(url):
    """
    Извлекает названия книг и их цены с классической страницы по указанному URL.

    :param url: Строка, представляющая URL страницы с книгами.
    :return: Кортеж, содержащий два списка: названия книг и их цены.
    """
    # Получаем содержимое страницы
    page_content = get_page_content(url)

    # Проверяем, содержимое страницы было успешно получено
    if page_content:
        # Создаем объект BeautifulSoup для парсинга HTML-кода
        soup = BeautifulSoup(page_content, 'html.parser')

        # Находим все заголовки книг и извлекаем текст из них
        titles = [title.text.strip() for title in soup.select('h3 a')]

        # Находим все элементы с ценами и извлекаем текст из них
        prices = [price.text.strip() for price in soup.select('p.price_color')]

        # Возвращаем два списка: с названиями книг и с их ценами
        return titles, prices
    else:
        # Если содержимое страницы не было получено, возвращаем пустые списки
        print("Содержимое страницы не было получено.")
        return [], []

# Пример использования функции
if __name__ == "__main__":
    url = "http://books.toscrape.com/catalogue/category/books/classics_6/index.html"  # Пример URL
    titles, prices = parse_classics_page(url)

    # Выводим названия книг и их цены
    print("Книги и их цены:")
    for title, price in zip(titles, prices):
        print(f"{title}: {price}")