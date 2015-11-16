# Interview Question 3.7


import collections


class Animal(object):

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)


class AnimalShelter(object):

    def __init__(self):
        self._queues = {}
        self._time = 0

    def enqueue(self, animal):
        if type(animal) not in self._queues:
            self._queues[type(animal)] = collections.deque()
        self._queues[type(animal)].append((self._time, animal))
        self._time += 1

    def _dequeue(self, animal_type):
        queue = self._queues.get(animal_type, None)
        if queue:
            _, animal = queue.popleft()
            return animal
        else:
            raise IndexError('Empty shelter')

    def dequeueAny(self):
        oldest_type = oldest_queue = None
        for type_, queue in self._queues.items():
            if (queue and (oldest_queue is None or
                           queue[0][0] < oldest_queue[0][0])):
                oldest_type = type_
                oldest_queue = queue
        return self._dequeue(oldest_type)

    def dequeueDog(self):
        return self._dequeue(Dog)

    def dequeueCat(self):
        return self._dequeue(Cat)


if __name__ == '__main__':
    shelter = AnimalShelter()

    tom = Cat('Tom')
    butch = Cat('Butch')
    spike = Dog('Spike')
    tyke = Dog('Tyke')
    shelter.enqueue(tom)
    shelter.enqueue(spike)
    shelter.enqueue(butch)
    shelter.enqueue(tyke)

    print(shelter.dequeueAny())
    print(shelter.dequeueDog())
    print(shelter.dequeueDog())
    print(shelter.dequeueAny())
