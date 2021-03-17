class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def queue_length(self):
        return len(self.queue)

    def add_to_queue(self, person):
        self.queue.append(person)
        # person_to_add

    def clear(self):
        self.queue = []
        # Can also do:
        # self.queue.clear()