
import requests

class ApiClient:

    # Базовый адрес API, например "https://jsonplaceholder.typicode.com/"
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

    # Вспомогательный метод - формируем полный URL
    def _url(self, path: str) -> str:
        return f'{self.base_url}/{path.lstrip("/")}'

    # ----------------------- Методы для работы с API --------------------

    # Получить пост по ID
    def get_post(self, post_id: int):
        return self.session.get(self._url(f"posts/{post_id}"))

    # Получить список всех постов
    def get_all_posts(self):
        return self.session.get(self._url('/posts'))

    # Создать новый пост
    def create_post(self, title: str, body: str, user_id: int):
        payload = {"title": title, "body": body, "userId": user_id}
        return self.session.post(self._url("posts"), json=payload)

    # Удалить пост
    def delete_post(self, post_id: int):
        return self.session.delete(self._url(f"posts/{post_id}"))

    # Полное обновление поста
    def update_post(self, post_id: int, title: str, body: str, user_id: int):
        payload = {"title": title, "body": body, "userId": user_id}
        return self.session.put(self._url(f"posts/{post_id}"), json=payload)

    # Частичное обновление поста
    def update_patch(self, post_id: int, title: str, user_id: int):
        payload = {"title": title, "userId": user_id}
        return self.session.patch(self._url(f"posts/{post_id}"), json=payload)





