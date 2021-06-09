from . import common


def test_empty_login_and_pswd():
    try:
        ctx = common.create_context('', '')
        ctx.check_new_messages()
    except RuntimeError as err:
        assert str(err) == 'Неверный логин и пароль!'
