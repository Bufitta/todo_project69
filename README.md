1.  Перейдите в рабочую директорию:
Под Windows (на вашем компьютере адрес может отличаться):
    >cd D:\Dev\

    Под macOS или Linux:
    >cd ~/Dev/

2.  Клонируйте репозиторий с сайта Github:
    >git clone https://github.com/Bufitta/todo_project69.git

    У вас создастся папка todo_project69, переходим в нее.


3.  Создаем виртуальное окружение как в [уроке](https://practicum.yandex.ru/learn/backend-developer/courses/1b78b2c9-df6f-4349-a831-7ef978dd092f/sprints/24404/topics/d0d00761-9dd8-42b1-b5a0-e3bd52f05c51/lessons/775bd6f8-30c7-4ce3-9908-ec54d0098f83/).

Для установки пакетов используем команду pip install -r requirements.txt (виртуальное окружение должно быть активировано).

База данных содержится в файлах, чтобы меньше нужно было телодвижений для запуска проекта. Можете удалить и создать свою.
Для корректной работы статики, не забываем про collectstatic