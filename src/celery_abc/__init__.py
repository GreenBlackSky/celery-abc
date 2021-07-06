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
3. In your `Worker` service import `Interface` from shared module
and implement it. Metaclass for your implementation should be
`WorkerMetaBase` from `celery-abc`. You don't need to register
it's methods, just instantiate your class with `celery`.
4. In `Caller` service import `CallerMetaBase`, create a new
class, that inherits from `Interface` and have `CallerMetaBase`
as a metaclass. Instantiate it with your `celery` app. Now, you
can call methods, that are implemented in the `Worker` =)

Here you go, now you can seamlessly call methods of `Worker` from
`Caller`. As you can see, you can call `Worker`'s methods from each
other. But you can not keep any instnce variables in `Worker`'s `self`.
In the end, microservices are better when they are stateless.
"""

from .caller import CallerMetaBase
from .worker import WorkerMetaBase
