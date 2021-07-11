"""Test how does caller work."""

import os
from time import sleep

from celery import Celery
from celery_abc import CallerMetaBase
import pytest

from shared.interface import Interface


class Caller(Interface, metaclass=CallerMetaBase):
    """Caller class example."""

    pass


celery = Celery(
    broker='amqp://{}:{}@{}:{}//'.format(
        os.environ['RABBITMQ_DEFAULT_USER'],
        os.environ['RABBITMQ_DEFAULT_PASS'],
        os.environ['RABBITMQ_HOST'],
        os.environ['RABBITMQ_PORT']
    ),
    backend='rpc://'
)


caller = Caller(celery)


a, b, c, d = 1, 2, 3, 4
lst = [a, b, c, d]
lst2 = [b, c, d]
lst3 = [a, b, c]
dct = {'a': a, 'b': b, 'c': c, 'd': d}
dct2 = {'a': a, 'b': b}
dct3 = {'c': c, 'd': d}
result = sum(lst)


def test_add_positional():
    # 1 way to pass args
    assert caller.add_positional(a, b, c, d) == result
    assert caller.add_positional(*lst) == result
    assert caller.add_positional(**dct) == result
    assert caller.add_positional(a=a, c=c, b=b, d=d) == result
    # 2 ways to pass args
    assert caller.add_positional(a, *lst2) == result
    assert caller.add_positional(a, b, **dct3) == result
    assert caller.add_positional(a, b, d=d, c=c) == result
    assert caller.add_positional(*[a, b], **dct3) == result
    assert caller.add_positional(*[a, b], c=c, d=d) == result
    assert caller.add_positional(a=a, b=b, **dct3) == result
    # 3 ways to pass args
    assert caller.add_positional(a, *[b, c], **{'d': d}) == result
    assert caller.add_positional(a, *[b, c], d=d) == result
    assert caller.add_positional(a, b, b=b, **{'c': c, 'd': d}) == result
    assert caller.add_positional(*[a, b], c=c, **{'d': d}) == result
    # 4 ways to pass args
    assert caller.add_positional(a, *[b], c=c, **{'d': d}) == result


# def test_add_list():
#     assert caller.add_list() == 0
#     assert caller.add_list(a, b, c, d) == result
#     assert caller.add_list(*lst) == result
#     assert caller.add_list(a, *lst2) == result


# def test_add_dict():
#     assert caller.add_dict() == 0
#     assert caller.add_dict(a=a, b=b, c=c, d=d) == result
#     assert caller.add_dict(**dct) == result
#     assert caller.add_dict(a=a, b=b, **dct3) == result


# def test_add_positionald_and_list():
#     assert caller.add_positionald_and_list(a, b) == result
#     assert caller.add_positionald_and_list(a, b, c, d) == result
#     assert caller.add_positionald_and_list(*lst) == result
#     assert caller.add_positionald_and_list(a, b, *[c, d]) == result
#     assert caller.add_positionald_and_list(a, *lst2) == result


# def test_add_positional_and_dict():
#     assert caller.add_positional_and_dict(a, b) == result
#     assert caller.add_positional_and_dict(*[a, b]) == result
#     assert caller.add_positional_and_dict(**dct) == result
#     assert caller.add_positional_and_dict(a, *[b]) == result
#     assert caller.add_positional_and_dict(a, b, **dct3) == result
#     assert caller.add_positional_and_dict(*[a, b], **dct3) == result
#     assert caller.add_positional_and_dict(a, *[b], **dct3) == result


# def test_add_list_and_dict():
#     assert caller.add_list_and_dict() == result
#     # 1 way to pass args
#     assert caller.add_list_and_dict(a, b, c, d) == result
#     assert caller.add_list_and_dict(*lst) == result
#     assert caller.add_list_and_dict(**dct) == result
#     assert caller.add_list_and_dict(a=a, c=c, b=b, d=d) == result
#     # 2 ways to pass args
#     assert caller.add_list_and_dict(a, *lst2) == result
#     assert caller.add_list_and_dict(a, b, **dct3) == result
#     assert caller.add_list_and_dict(a, b, d=d, c=c) == result
#     assert caller.add_list_and_dict(*[a, b], **dct3) == result
#     assert caller.add_list_and_dict(*[a, b], c=c, d=d) == result
#     assert caller.add_list_and_dict(a=a, b=b, **dct3) == result
#     # 3 ways to pass args
#     assert caller.add_list_and_dict(a, *[b, c], **{'d': d}) == result
#     assert caller.add_list_and_dict(a, *[b, c], d=d) == result
#     assert caller.add_list_and_dict(a, b, b=b, **{'c': c, 'd': d}) == result
#     assert caller.add_list_and_dict(*[a, b], c=c, **{'d': d}) == result
#     # 4 ways to pass args
#     assert caller.add_list_and_dict(a, *[b], c=c, **{'d': d}) == result


# def test_add_positional_list_and_dict():
#     assert caller.add_positional_list_and_dict(a, b) == result
#     # 1 way to pass args
#     assert caller.add_positional_list_and_dict(a, b, c, d) == result
#     assert caller.add_positional_list_and_dict(*lst) == result
#     assert caller.add_positional_list_and_dict(**dct) == result
#     assert caller.add_positional_list_and_dict(a=a, c=c, b=b, d=d) == result
#     # 2 ways to pass args
#     assert caller.add_positional_list_and_dict(a, *lst2) == result
#     assert caller.add_positional_list_and_dict(a, b, **dct3) == result
#     assert caller.add_positional_list_and_dict(a, b, d=d, c=c) == result
#     assert caller.add_positional_list_and_dict(*[a, b], **dct3) == result
#     assert caller.add_positional_list_and_dict(*[a, b], c=c, d=d) == result
#     assert caller.add_positional_list_and_dict(a=a, b=b, **dct3) == result
#     # 3 ways to pass args
#     assert caller.add_positional_list_and_dict(
#         a, *[b, c], **{'d': d}
#     ) == result
#     assert caller.add_positional_list_and_dict(a, *[b, c], d=d) == result
#     assert caller.add_positional_list_and_dict(
#         a, b, b=b, **{'c': c, 'd': d}
#     ) == result
#     assert caller.add_positional_list_and_dict(
#         *[a, b], c=c, **{'d': d}
#     ) == result
#     # 4 ways to pass args
#     assert caller.add_positional_list_and_dict(
#         a, *[b], c=c, **{'d': d}
#     ) == result
