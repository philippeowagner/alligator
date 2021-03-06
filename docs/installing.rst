.. _installing:

====================
Installing Alligator
====================

Installation of Alligator itself is a relatively simple affair. For the most
recent stable release, simply use pip_ to run::

    $ pip install alligator

Alternately, you can download the latest development source from Github::

    $ git clone https://github.com/toastdriven/alligator.git
    $ cd alligator
    $ python setup.py install

.. _pip: http://pip-installer.org/


Queue Backends
==============

Alligator includes a ``Local Memory Client``, which is useful for development
or testing (no setup required). However, this is not very scalable.

For production use, you should install one of the following servers used for
queuing:


Redis
-----

A in-memory data structure server, it offers excellent speed as well as being
a frequently-already-installed server. Official releases can be found at
http://redis.io/download.

You'll also need to install the ``redis`` package::

    $ pip install redis

You can also install via other package managers::

    # On Mac with Homebrew
    $ brew install redis

    # On Ubuntu
    $ sudo aptitude install redis


Beanstalk
---------

A simple & fast queue. Official releases can be found at
http://kr.github.io/beanstalkd/.

.. warning::

    This backend does not support Python 3.3+, as the underlying dependencies
    have not been ported.

You'll also need to install the both the ``beanstalkc`` & ``PyYAML`` packages::

    $ pip install beanstalkc
    $ pip install PyYAML

You can also install via other package managers::

    # On Mac with Homebrew
    $ brew install beanstalk

    # On Ubuntu
    $ sudo aptitude install beanstalkd

.. warning::

    Beanstalk works differently than the other queues in several notable ways:

    1. It does **NOT** support custom ``task_id``s. You can still set them
       and it will be preseved in the task, but the backend will overwrite
       your ``task_id`` choice once it's in the queue.
    2. Dropping a whole queue is **VERY** inefficient.
    3. It depends on **PyYAML** & uses a known-unsafe parsing method, which
       could make you susceptible to MiTM attacks.

    It's still an excellent choice at large volumes, but you should be aware of
    the shortcomings.


SQS
---

`Amazon SQS`_ is a queue service created by Amazon Web Services. It works well
in large-scale environments or if you're already using other AWS services.

It has the benefit of not requiring an installed setup, only an AWS account &
a credit card, making it the easiest of the production queues to setup.

You'll need to install the ``boto`` packages::

    $ pip install 'boto>=2.35.0'

.. warning::

    SQS works differently than the other queues in a couple ways:

    1. It does **NOT** support custom ``task_id``s. You can still set them
       and it will be preseved in the task, but the backend will overwrite
       your ``task_id`` choice once it's in the queue.
    2. You must **manually** create queues! Alligator will not auto-create them
       (to save on requests performed & therefore how much you are billed).
       Create the ``Gator`` queues at the AWS console before trying to use them.
    3. It does **NOT** support ``gator.get(...)``, as this functionality is not
       supported by the SQS service itself.

    It's also an excellent choice at large volumes, but you should be aware of
    the shortcomings.
