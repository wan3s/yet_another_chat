import hashlib
import pymongo

from . import common


def test_empty_login_and_pswd():
    client = pymongo.MongoClient()
    client.test_chat_db.users.delete_many(filter={})
    client.test_chat_db.messages.delete_many(filter={})
    ctx = common.Context(client.test_chat_db, '', '')
    try:
        ctx._get_user_data()
    except RuntimeError as err:
        assert str(err) == 'Неверный логин и пароль!'

def test_create_new_user():
    client = pymongo.MongoClient()
    client.test_chat_db.users.delete_many(filter={})
    client.test_chat_db.messages.delete_many(filter={})
    ctx = common.Context(client.test_chat_db, 'vasya', '123')
    ctx.create_new_user()
    res = ctx._get_user_data()
    assert res.login == 'vasya'
    assert res.password == hashlib.md5(('123').encode('utf-8')).hexdigest()

def test_logins_duplicates():
    client = pymongo.MongoClient()
    client.test_chat_db.users.delete_many(filter={})
    client.test_chat_db.messages.delete_many(filter={})
    ctx1 = common.Context(client.test_chat_db, 'vasya', '123')
    ctx1.create_new_user()
    ctx2 = common.Context(client.test_chat_db, 'vasya', '1234')
    try:
        ctx2.create_new_user()
    except RuntimeError as err:
        assert str(err) == 'Login vasya already used!'


def test_send_new_message():
    client = pymongo.MongoClient()
    client.test_chat_db.users.delete_many(filter={})
    client.test_chat_db.messages.delete_many(filter={})
    ctx1 = common.Context(client.test_chat_db, 'vasya', '123')
    ctx1.create_new_user()
    ctx2 = common.Context(client.test_chat_db, 'igor', '1234')
    ctx2.create_new_user()
    ctx1.send_new_message(receiver_login='igor', msg_text='hello')
    res = client.test_chat_db.messages.find_one()
    assert res['text'] == 'hello'
    assert res['seen'] == False
    
def test_send_check_new_message():
    client = pymongo.MongoClient()
    client.test_chat_db.users.delete_many(filter={})
    client.test_chat_db.messages.delete_many(filter={})
    ctx1 = common.Context(client.test_chat_db, 'vasya', '123')
    ctx1.create_new_user()
    ctx2 = common.Context(client.test_chat_db, 'igor', '1234')
    ctx2.create_new_user()
    ctx1.send_new_message(receiver_login='igor', msg_text='hello')
    res = ctx2.check_new_messages()
    assert res == [f'vasya at @@@: hello']
