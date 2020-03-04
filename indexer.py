from models import User, Organization, Tickets

class Indexer:
    def __init__(self):
        self.userDoc = User.materialize_data('./data/')
        self.ticketDoc = Tickets.materialize_data('./data/')
        self.organizationDoc = Organization.materialize_data('./data/')

