#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Chat engine.

:copyright: DreamTeam, 2021
"""

import dataclasses
import datetime
import hashlib
import pymongo
import gettext
import sys
import os.path

datapath = os.path.dirname(sys.argv[0])
gettext.install('app', os.path.join('po'), names=("ngettext",))


@dataclasses.dataclass(frozen=True)
class User:
    """Класс Пользователь."""

    _id: str
    login: str
    password: str


class Context:
    """Класс Контекст."""

    def __init__(self, db, login, password) -> None:
        """Конструктор."""
        self._db = db
        self._login = login
        self._password = password

    def check_new_messages(self):
        """Проверка новых сообщений."""
        current_user = self._get_user_data()
        query = {
            'receiver_id': current_user._id,
            'seen': False,
        }
        messages = list(self._db.messages.find(query))
        msg_ids = []
        messages_list = []
        if len(messages) == 0:
            print(_('You have not any new messages'))
            return
        for msg in messages:
            sender = self._db.users.find_one(
                {
                    '_id': msg['sender_id']
                }
            )
            sender_login = sender['login']
            text = msg['text']
            ts = msg['ts']
            print(f'{sender_login} at {ts}: {text}')
            messages_list.append(f'{sender_login} at @@@: {text}')
            msg_ids.append(msg['_id'])
        bulk_query = [
            pymongo.UpdateOne({'_id': msg_id}, {'$set': {'seen': True}})
            for msg_id in msg_ids
        ]
        self._db.messages.bulk_write(bulk_query)
        return messages_list

    def create_new_user(self):
        """Создание нового пользователя."""
        user = self._db.users.find_one({
            'login': self._login,
        })
        if user:
            raise RuntimeError(f'Login {self._login} already used!')
        res = self._db.users.insert_one(
            {
                'login': self._login,
                'password': hashlib.md5(self._password.encode('utf-8')).hexdigest()
            }
        )
        print(_('User was succefully created'))

    def send_new_message(self, receiver_login=None, msg_text=None):
        """Отправка нового сообщения."""
        current_user = self._get_user_data()
        if receiver_login is None:
            receiver_login = input('Write receiver login >>> ')
        receiver = self._db.users.find_one({'login': receiver_login})
        if not receiver:
            raise RuntimeError(_('Can\'t find any user with such login!'))
        if msg_text is None:
            msg_text = input(_('Write your message >>> '))
        self._db.messages.insert_one(
            {
                'receiver_id': receiver['_id'],
                'sender_id': current_user._id,
                'text': msg_text,
                'seen': False,
                'ts': datetime.datetime.utcnow()
            }
        )
        print(_('Message was succefully sent'))

    def _get_user_data(self):
        """Получение данных о пользователе."""
        query = {
            'login': self._login,
            'password': hashlib.md5(self._password.encode('utf-8')).hexdigest(),
        }
        user_data = self._db.users.find_one(query)
        if not user_data:
            raise RuntimeError(_('Invalid login and password!'))
        return User(**user_data)


def create_context(login, password):
    """Создание контекста."""
    client = pymongo.MongoClient()
    return Context(client.chat_db, login, password)
