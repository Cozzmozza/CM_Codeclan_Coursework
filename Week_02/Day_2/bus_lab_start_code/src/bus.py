class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination  = destination
        self.passengers = []

    def drive(self):
        return 'Brum brum'

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)
        # person_to_pick_up
    
    def drop_off(self, person):
        self.passengers.remove(person)
        # person_to_drop_off

    def empty(self):
        self.passengers = []
        # self.passengers.clear() 
        # should use the clear method. As what we've done is basically ended up with two cleared lists

    def pick_up_from_stop(self, bus_stop):
        self.passengers += bus_stop.queue
        # Alternative:
        #   self.passengers.extend(bus_stop.queue)
        # Should also add:
        #   bus_stop.clear()

    # Solution:
    # def pick_up_from_stop(self, bus_stop_to_pick_up_from):
    #     for passenger in bus_stop_to_pick_up_from.queue:
    #         self.passengers.append(passenger)

    # For each passenger in the bus stop queue, add onto the passenger list

    