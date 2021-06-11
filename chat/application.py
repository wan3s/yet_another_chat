#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Chat interface.

:copyright: DreamTeam, 2021
"""

import argparse

from . import common


def run():
    """Return nothing. Connection to the chat.

    :return: nothing
    """
    parser = argparse.ArgumentParser(description='Yet another chat')
    parser.add_argument('--new-messages',
                        action='store_true',
                        help='Check new messages that you\'ve received')
    parser.add_argument('--send-message',
                        action='store_true',
                        help='Write new message')
    parser.add_argument('--new-user',
                        action='store_true',
                        help='Create new user')
    parser.add_argument('--login',
                        help='Your login',
                        required=True)
    parser.add_argument('--password',
                        help='Your password',
                        required=True)
    args = parser.parse_args()
    ctx = common.create_context(args.login, args.password)
    if args.new_messages:
        ctx.check_new_messages()
    elif args.send_message:
        ctx.send_new_message()
    elif args.new_user:
        ctx.create_new_user()
