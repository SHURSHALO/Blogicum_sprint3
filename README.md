 # Blogicum
> Blogicum - это блоговая платформа на базе Django, которая позволяет пользователям создавать и публиковать собственные блоги. Она предоставляет простой и интуитивно понятный интерфейс для управления записями, категориями и статическими страницами.

## Что было добавлено к предыдущей версии

### У каждой публикации на проекте такие атрибуты:
• Заголовок поста.

• Основной текст поста.

• Дата публикации. Автор поста (или суперпользователь) могут установить любую дату публикации, в том числе — ещё не наступившую, в будущем.

• Дата добавления публикации в базу данных.

• Флаг «опубликовано».

• Автор: зарегистрированный на проекте пользователь. Авторов могут добавлять суперпользователи.

• Локация: одно определённое местоположение, к которому относится пост; локация может быть не указана, тогда на уровне шаблона в качестве локации отображается значение «Планета Земля».

• Категория: подборка, в которой собраны посты по определённой теме.

### Логика работы проекта
• Без указания какой-либо одной категории новый пост добавить нельзя.

• Локацию для поста указывать необязательно.

• Администратор сайта может снять с публикации любой пост, категорию и локацию.

• Пост отображается на страницах проекта, если у него одновременно:

   ‣  дата публикации — не позже текущего времени,

   ‣  он опубликован,

   ‣  категория, к которой он принадлежит, не снята с публикации;

   ‣  Локация, снятая с публикации, не влияет на отображение связанных с ней постов.

Предыдущая версия https://github.com/SHURSHALO/Blogicum_sprint1
## Установка
1. Клонируйте репозиторий на свою локальную машину:
```
git clone git@github.com:SHURSHALO/Blogicum_sprint3.git
```
2. Перейдите в директорию проекта:
```
cd Blogicum_sprint3
```
3. Создайте и активируйте виртуальное окружение (опционально):
```
py -3.9 -m venv venv
```
```
source venv/Scripts/activate
```

4. Установите необходимые зависимости:
```
pip install -r requirements.txt
```
5. Примените миграции базы данных:
```
cd blogicum
```
```
python manage.py migrate
```
6. Создайте суперпользователя:
```
python manage.py createsuperuser
```
### Запуск
```
python manage.py runserver
```
Откройте веб-браузер и перейдите по адресу http://localhost:8000/, чтобы получить доступ к приложению Blogicum.

Админка доступна по адресу http://127.0.0.1:8000/admin/

