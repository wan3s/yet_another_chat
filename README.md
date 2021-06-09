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
- хранить будем в mongodb
- возможно будем использовать Django и добавим немного JS

# Сдача проекта
0) git clean -fd
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
5) doit test
6) 
```
pip install virtualenv
mkdir python-virtual-environments && cd python-virtual-environments
python3 -m venv env 
source env/bin/activate (подняли чистое окружение)
cd ..
pip install doit
pip install pydocstyle
doit wheel
pip install ~/yet_another_chat/dist/test_wheel-0.0.1-py3-none-any.whl (установили приложение)
python3 chat --new-messages --login boris --password 1234
pip install -U pytest
doit test
```
