#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    ticket_cache = {}
    route = []

    for ticket in tickets:
        ticket_cache[ticket.source] = ticket.destination

    stop = 0
    current_stop = 'NONE'

    while stop < len(tickets):
        next_stop = ticket_cache[current_stop]
        route.append(next_stop)

        current_stop = next_stop
        stop += 1

    return route