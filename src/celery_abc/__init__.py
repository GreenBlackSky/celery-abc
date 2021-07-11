"""
Set of tools to create microservice app with `celery` as message brocker.

Say, you want to write some microservices with python.And you want them to
work seamlessly with each other - call methods of one service from another
like it is a single app. You may use `celery` just for that. But you actually
need to register tasks in the same app. Isn't that a little strange - to keep
the code base of ALL the services in each and every of them? Wouldn't it be
more convinient, to share only interfaces? That way each developer could track
what they can use of other services, but without actully storing their code.

How to use it?
We'll need at least two services and a shared directory. In shared directory
we'll create an abstract class `Interface`. Let's call one service `Caller`
and the other - `Worker`. `Caller` has `Interface` imported, but knows nothing
about the implementation. `Worker` has `Interface` implemented.

1. Create common directory, share it with all your services.
2. In the shared folder create python module. Define your
interfaces there. For now, `celery-abc` requires for `Interface`
to be abstract.
>>> from abc import ABC, abstractmethod

>>> class Interface(ABC):
>>>     @abstractmethod
>>>     def do_some_stuff(self, arg):
>>>         pass
>>>     @abstractmethod
>>>     def do_more_stuff(self, arg):
>>>         pass
3. In your `Worker` service import `Interface` from shared module
and implement it. Metaclass for your implementation should be
`WorkerMetaBase` from `celery-abc`. You don't need to register
it's methods, just instantiate your class with `celery`.
Run your `worker` as a celery worker.
>>> from celery import Celery
>>> from celery_abc import WorkerMetaBase
>>> from shared import Interface

>>> class Worker(Interface, metaclass=WorkerMetaBase):
>>>     def do_some_stuff(self, arg):
>>>         return self.do_more_stuff(arg)

>>>     def do_more_stuff(self, arg):
>>>         return f"Doing stuff {arg}"

>>> celery_app = Celery(...)
>>> Worker(celery)
4. In `Caller` service import `CallerMetaBase`, create a new
class, that inherits from `Interface` and have `CallerMetaBase`
as a metaclass. Instantiate it with your `celery` app.
Unlike `worker`, `caller` may run just as regular python app.
>>> class Caller(Interface, metaclass=CallerMetaBase):
>>>     pass

>>> celery_app = Celery(...)
>>> caller = Caller(celery)
>>> result = caller.do_some_stuff('Hello!')
Now, you can call methods, that are implemented in the `Worker` =)

Here you go, now you can seamlessly call methods of `Worker` from
`Caller`. As you can see, you can call `Worker`'s methods from each
other. But you can not keep any instnce variables in `Worker`'s `self`.
In the end, microservices are better when they are stateless.

Resrictions and limitations:
If you want to create statefull microservices - you still can use `celery-abc`,
if only for comunication. But there may be other solutions.

If you want to create complex system of classes. OOP is cool,
but multiple and chaind inheritance are not supported at the moment.
"""

from .caller import CallerMetaBase
from .worker import WorkerMetaBase
