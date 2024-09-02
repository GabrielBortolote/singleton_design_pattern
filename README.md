# Singleton

This project implements a use case for a Design Pattern, the Singleton. To know more about this pattern you can access [this website](https://refactoring.guru/design-patterns/singleton).

## What it is?

Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

## Project

There's many ways to implement Singletons in python, let's explore one of them: customizing the **metaclass** customization.

Maybe you don't know, but every time you create define a class you are creating a Class object. Note, I said a class object, not an object of that class. If this is your code:

```python
class Foo: pass
```

An object was create to store the Foo class definition. Every class object it's created by a Factory named **type**, type is the default metaclass. We can customize the *type* class, extending it and modifying its methods and attributes and then use this customization on our class definition. So let's implement this:

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
```

Here we are extending *type*, adding the attribute *_instances* and modifying the *\_\_call\_\_* method. The method now is going to create a new class object only in the first call, creating an instance that we can name the singleton of that class, because it is going to be unique instance. The *_instances* attribute works like a map between class objects and a singleton object of that class. Every time the client code asks for a new instance, the meta class is going to act and return the singleton. Now we can use this metaclass implementation inside a class:

```python
from singleton_meta import SingletonMeta

class ClickCounter(metaclass=SingletonMeta):
    counter = 0
    
    def click(cls):
        cls.counter += 1
```

Now let's write some client code to use our singleton inside the file *main.py*:

```python
from click_counter import ClickCounter

if __name__ == '__main__':
    # click counter 1
    click_counter_1 = ClickCounter()
    for _ in range(0, 10):
        click_counter_1.click()

    print(f'{click_counter_1.counter} clicks were counted.')

    # click counter 1
    click_counter_2 = ClickCounter()
    for _ in range(0, 10):
        click_counter_2.click()

    print(f'{click_counter_2.counter} clicks were counted.')
```

Executing the client code *main.py* we can check the behaviour of a singleton:

```bash
python main.py
10 clicks were counted.
20 clicks were counted.
```

Thanks for reading.
