# Тестовое задание для backend разработчика (загрузка/изменение изображений)

## Установка (необходимые библиотеки). Проект разрабатывался на windows 10, python 3.8.3
```bash
pip install Django
pip install requests
pip install Pillow
pip install urllib3
```
## Использование
### Как развернуть
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### Основной функционал
http://127.0.0.1:8000/ или http://127.0.0.1:8000/images_list/ - Выводит список загруженных изображений
http://127.0.0.1:8000/add_image/ - Загрузить изображение
http://127.0.0.1:8000/edit_image/image_name - Изменить изображение