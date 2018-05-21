
"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""


# Counter
"""
Allows us to count things. Give it a iterable or a mapping (such as a dict) and it will turn into a counter of elements.
"""
from collections import Counter

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]
temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])

print('\n')

# defaultdict
"""
The `defaultdict` never raises a `KeyError`. Instead, it returns the value returned by the function specified when the object was instantiated.
"""

from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_maters = defaultdict(list)


for coworker, place  in coworkers:
    alma_maters[coworker].append(place)

print(alma_maters)
print(alma_maters['Anne'])
print(alma_maters)

print('\n')


# OrderedDict

from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 10
o['Jen'] = 3

print(o)  # keys are always in the order in which they were inserted

o.move_to_end('Rolf')
o.move_to_end('Jose', last=False)

print(o)

o.popitem()  # Pop off the last item from the list

print(o)

print('\n')


# namedtuple
"""
A namedtuple is another object that we can use like a tuple, where each of the elements of the tuple has a name. In addition, the tuple itself also has a name.

It improves on tuples by making more explicit what it means.

Take this as an example using normal tuples:
"""

from collections import namedtuple

# Normal Tuples

account = ('checking', 1850.90)

print(account[0])  # name
print(account[1])  # balance

print('\n')

# named tuples

Account = namedtuple('Account', ['name', 'balance'])
account = Account('checking', 1850.90)
print(account.name)
print(account.balance)
print(account)

print('\n')

## Deque
"""
The last element we’ll look at today is the `deque`, which stands for “Double-ended queue”.

(Watch presentation about queues if you haven’t already).

In a `deque`, we can push elements at the start or the end, and we can also remove elements from the start or the end.

It is very efficient, performing very well, and also it’s thread-safe (we’ll be looking at threads soon!). 

When we look at asynchronous development, we’ll be talking more about the `deque` as we use it. For now, just remember it’s like a list on which you do operations like a list:
"""

from collections import deque

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))

friends.append('Jose')
friends.appendleft('Anthony')
print(friends)

friends.pop()
print(friends)

friends.popleft()
print(friends)