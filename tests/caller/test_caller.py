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


a, b, c, d, e, f, g, h = 1, 2, 3, 4, 5, 6, 7, 8
result = 10
result_2 = 21
result_3 = 36


def test_add_positional():
    # 1 way to pass args
    assert caller.add_positional(a, b, c, d) == result
    assert caller.add_positional(*[a, b, c, d]) == result
    assert caller.add_positional(**{'a': a, 'b': b, 'c': c, 'd': d}) == result
    assert caller.add_positional(a=a, c=c, b=b, d=d) == result
    # 2 ways to pass args
    assert caller.add_positional(a, *[b, c, d]) == result
    assert caller.add_positional(a, b, **{'c': c, 'd': d}) == result
    assert caller.add_positional(a, b, d=d, c=c) == result
    assert caller.add_positional(*[a, b], **{'c': c, 'd': d}) == result
    assert caller.add_positional(*[a, b], c=c, d=d) == result
    assert caller.add_positional(a=a, b=b, **{'c': c, 'd': d}) == result
    # 3 ways to pass args
    assert caller.add_positional(a, *[b, c], **{'d': d}) == result
    assert caller.add_positional(a, *[b, c], d=d) == result
    assert caller.add_positional(a, b, b=b, **{'c': c, 'd': d}) == result
    assert caller.add_positional(*[a, b], c=c, **{'d': d}) == result
    # 4 ways to pass args
    assert caller.add_positional(a, *[b], c=c, **{'d': d}) == result


# def test_add_default():
#     # no args at all
#     assert caller.add_default() == result
#     # 1 way to pass args
#     assert caller.add_default(a, b, c) == result
#     assert caller.add_default(*[a, b, c]) == result
#     assert caller.add_default(**{'a': a, 'b': b}) == result
#     assert caller.add_default(a=a, b=b) == result
#     # 2 ways to pass args
#     assert caller.add_default(a, *[b, c]) == result
#     assert caller.add_default(a, b, *[c]) == result
#     assert caller.add_default(a, **{'c': c, 'd': d}) == result
#     assert caller.add_default(a, b, **{'c': c}) == result
#     assert caller.add_default(a, c=c) == result
#     assert caller.add_default(*[a], **{'c': c, 'd': d}) == result
#     assert caller.add_default(*[a, b], **{'d': d}) == result
#     assert caller.add_default(*[a], c=c, d=d) == result
#     assert caller.add_default(*[a, b], d=d) == result
#     assert caller.add_default(a=a, **{'c': c, 'd': d}) == result
#     assert caller.add_default(a=a, b=b, **{'d': d}) == result
#     # 3 ways to pass args
    # assert caller.add_default_2(a, *[b, c], **{'e': e, 'f': f}) == result_2
    # assert caller.add_default_2(a, b, *[c], **{'e': e, 'f': f}) == result_2
    # assert caller.add_default_2(a, b, *[c, d], **{'f': f}) == result_2
    # assert caller.add_default_2(a, *[b, c], e=e, f=f) == result_2
    # assert caller.add_default_2(a, b *[c], e=e, f=f) == result_2
    # assert caller.add_default_2(a, b *[c, d], f=f) == result_2
    # assert caller.add_default_2(a, c=c, d=d, **{'e': e, 'f': f}) == result_2
    # assert caller.add_default_2(a, b, d=d, **{'e': e, 'f': f}) == result_2
    # assert caller.add_default_2(a, b, c=c, d=d, **{'f': f}) == result_2
    # assert caller.add_default_2(
    #     *[a], c=c, d=d, **{'e': e, 'f': f}
    # ) == result_2
    # assert caller.add_default_2(*[a, b], d=d, **{'e': e, 'f': f}) == result_2
    # assert caller.add_default_2(*[a, b], c=c, d=d, **{'f': f}) == result_2
#     # 4 ways to pass args
    # assert caller.add_default_3(
    #     a, *[b, c], e=e, f=f, **{'g': g, 'h': h}
    # ) == result_3
    # assert caller.add_default_3(
    #     a, b, *[c], e=e, f=f, **{'g': g, 'h': h}
    # ) == result_3
    # assert caller.add_default_3(
    #     a, b, *[c, d], f=f, **{'g': g, 'h': h}
    # ) == result_3
    # assert caller.add_default_3(
    #     a, b, *[c, d], e=e, f=f, **{'h': h}
    # ) == result_3


# def test_add_list():
#     assert caller.add_list() == 0
#     assert caller.add_list(a, b, c, d) == result
#     assert caller.add_list(*[a, b, c, d]) == result
#     assert caller.add_list(a, *[b, c, d]) == result


# def test_add_dict():
#     assert caller.add_dict() == 0
#     assert caller.add_dict(a=a, b=b, c=c, d=d) == result
#     assert caller.add_dict(**{'a': a, 'b': b, 'c': c, 'd': d}) == result
#     assert caller.add_dict(a=a, b=b, **{'c': c, 'd': d}) == result


# def add_positionald_and_default():
#     # 1 way to pass args
#     assert caller.add_positionald_and_default(a, b, c) == result
#     assert caller.add_positionald_and_default(*[a, b, c]) == result
#     assert caller.add_positionald_and_default(**{'a': a, 'b': b}) == result
#     assert caller.add_positionald_and_default(a=a, b=b) == result
#     # 2 ways to pass args
#     assert caller.add_positionald_and_default(a, *[b, c]) == result
#     assert caller.add_positionald_and_default(a, b, *[c]) == result
#     assert caller.add_positionald_and_default(a, **{'c': c, 'd': d}) == result
#     assert caller.add_positionald_and_default(a, b, **{'c': c}) == result
#     assert caller.add_positionald_and_default(a, c=c) == result
#     assert caller.add_positionald_and_default(*[a], **{'c': c, 'd': d}) == result
#     assert caller.add_positionald_and_default(*[a, b], **{'d': d}) == result
#     assert caller.add_positionald_and_default(*[a], c=c, d=d) == result
#     assert caller.add_positionald_and_default(*[a, b], d=d) == result
#     assert caller.add_positionald_and_default(a=a, **{'c': c, 'd': d}) == result
#     assert caller.add_positionald_and_default(a=a, b=b, **{'d': d}) == result
#     # 3 ways to pass args
    # assert caller.add_default_2(a, *[b, c], **{'e': e, 'f': f}) == result_2
    # assert caller.add_default_2(a, b, *[c], **{'e': e, 'f': f}) == result_2
    # assert caller.add_default_2(a, b, *[c, d], **{'f': f}) == result_2
    # assert caller.add_default_2(a, *[b, c], e=e, f=f) == result_2
    # assert caller.add_default_2(a, b *[c], e=e, f=f) == result_2
    # assert caller.add_default_2(a, b *[c, d], f=f) == result_2
    # assert caller.add_default_2(a, c=c, d=d, **{'e': e, 'f': f}) == result_2
    # assert caller.add_default_2(a, b, d=d, **{'e': e, 'f': f}) == result_2
    # assert caller.add_default_2(a, b, c=c, d=d, **{'f': f}) == result_2
    # assert caller.add_default_2(
    #     *[a], c=c, d=d, **{'e': e, 'f': f}
    # ) == result_2
    # assert caller.add_default_2(*[a, b], d=d, **{'e': e, 'f': f}) == result_2
    # assert caller.add_default_2(*[a, b], c=c, d=d, **{'f': f}) == result_2
#     # 4 ways to pass args
    # assert caller.add_default_3(
    #     a, *[b, c], e=e, f=f, **{'g': g, 'h': h}
    # ) == result_3
    # assert caller.add_default_3(
    #     a, b, *[c], e=e, f=f, **{'g': g, 'h': h}
    # ) == result_3
    # assert caller.add_default_3(
    #     a, b, *[c, d], f=f, **{'g': g, 'h': h}
    # ) == result_3
    # assert caller.add_default_3(
    #     a, b, *[c, d], e=e, f=f, **{'h': h}
    # ) == result_3


# def test_add_positionald_and_list():
#     assert caller.add_positionald_and_list(a, b) == result
#     assert caller.add_positionald_and_list(a, b, c, d) == result
#     assert caller.add_positionald_and_list(*[a, b, c, d]) == result
#     assert caller.add_positionald_and_list(a, b, *[c, d]) == result
#     assert caller.add_positionald_and_list(a, *[b, c, d]) == result


# def test_add_positional_and_dict():
#     assert caller.add_positional_and_dict(a, b) == result
#     assert caller.add_positional_and_dict(*[a, b]) == result
    # assert caller.add_positional_and_dict(
    #     **{'a': a, 'b': b, 'c': c, 'd': d}
    # ) == result
#     assert caller.add_positional_and_dict(a, *[b]) == result
#     assert caller.add_positional_and_dict(a, b, **{'c': c, 'd': d}) == result
    # assert caller.add_positional_and_dict(
    #     *[a, b], **{'c': c, 'd': d}
    # ) == result
    # assert caller.add_positional_and_dict(
    #     a, *[b], **{'c': c, 'd': d}
    # ) == result


# def test_add_default_and_list():
#     pass


# def test_add_default_and_dict():
#     pass


# def test_add_list_and_dict():
#     assert caller.add_list_and_dict() == result
#     # 1 way to pass args
#     assert caller.add_list_and_dict(a, b, c, d) == result
#     assert caller.add_list_and_dict(*[a, b, c, d]) == result
    # assert caller.add_list_and_dict(
    #     **{'a': a, 'b': b, 'c': c, 'd': d}
    # ) == result
#     assert caller.add_list_and_dict(a=a, c=c, b=b, d=d) == result
#     # 2 ways to pass args
#     assert caller.add_list_and_dict(a, *[b, c, d]) == result
#     assert caller.add_list_and_dict(a, b, **{'c': c, 'd': d}) == result
#     assert caller.add_list_and_dict(a, b, d=d, c=c) == result
#     assert caller.add_list_and_dict(*[a, b], **{'c': c, 'd': d}) == result
#     assert caller.add_list_and_dict(*[a, b], c=c, d=d) == result
#     assert caller.add_list_and_dict(a=a, b=b, **{'c': c, 'd': d}) == result
#     # 3 ways to pass args
#     assert caller.add_list_and_dict(a, *[b, c], **{'d': d}) == result
#     assert caller.add_list_and_dict(a, *[b, c], d=d) == result
#     assert caller.add_list_and_dict(a, b, b=b, **{'c': c, 'd': d}) == result
#     assert caller.add_list_and_dict(*[a, b], c=c, **{'d': d}) == result
#     # 4 ways to pass args
#     assert caller.add_list_and_dict(a, *[b], c=c, **{'d': d}) == result


# def test_add_positional_default_and_list():
#     pass


# def test_add_positional_default_and_dict():
#     pass


# def test_add_positional_list_and_dict():
#     assert caller.add_positional_list_and_dict(a, b) == result
#     # 1 way to pass args
#     assert caller.add_positional_list_and_dict(a, b, c, d) == result
#     assert caller.add_positional_list_and_dict(*[a, b, c, d]) == result
    # assert caller.add_positional_list_and_dict(
    #     **{'a': a, 'b': b, 'c': c, 'd': d}
    # ) == result
#     assert caller.add_positional_list_and_dict(a=a, c=c, b=b, d=d) == result
#     # 2 ways to pass args
#     assert caller.add_positional_list_and_dict(a, *[b, c, d]) == result
    # assert caller.add_positional_list_and_dict(
    #     a, b, **{'c': c, 'd': d}
    # ) == result
#     assert caller.add_positional_list_and_dict(a, b, d=d, c=c) == result
    # assert caller.add_positional_list_and_dict(
    #     *[a, b], **{'c': c, 'd': d}
    # ) == result
#     assert caller.add_positional_list_and_dict(*[a, b], c=c, d=d) == result
    # assert caller.add_positional_list_and_dict(
    #     a=a, b=b, **{'c': c, 'd': d}
    # ) == result
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


# def test_add_default_list_and_dict():
#     pass


# def test_add_positional_default_list_and_dict():
#     pass
