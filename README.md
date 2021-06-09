# Yet another chat

Плланируем реализовать такой функционал:
- Отправка и просмотр сообщений
- Авторизация и регистрация
- Простейший интерфейс

Если успеем:
- Отправка картинок
- Добавим стикеры
- Forward сообщений
- Созданий групповых чатов
- Доставлено / просмотрено
- Кастомизация интерфейса

Предполагаемый стек:
- будем использовать Django
- хранить будем в mongodb
- возможно добавим немного JS

Схематичный интерфейс:
![image](https://user-images.githubusercontent.com/38588985/113776663-d0aba180-9732-11eb-932b-b1810fbfb401.png)


Инструкция для запуска монги на MacOS:
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/

# Сдача проекта
0) git clean -fd (по идее ничего лишнего удалить не должен)
1) Открываем дерево коммитов, смотрим кто что делал
2) doit lint
3) 
```
doit html
firefox build/html/index.html
```
4) 
```
doit mo
python3 chat --new-user --login boris --password 1234 (создали пользователя)
python3 chat --new-messages --login boris --password 1234 (получили сообщение на русском)
LC_ALL=en python3 chat --new-messages --login boris --password 1234 (получили сообщение на английском)
```
5) Здесь ты запускаешь свои тесты
6) 
```
pip install virtualenv (если ещё не сделал)
mkdir python-virtual-environments && cd python-virtual-environments
python3 -m venv env 
source env/bin/activate (подняли чистое окружение)
cd ..
doit wheel
pip install ~/yet_another_chat/dist/test_wheel-0.0.1-py3-none-any.whl (установили приложение)
python3 chat --new-messages --login boris --password 1234 (не потребует библиотеки)
```
