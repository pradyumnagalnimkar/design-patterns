from abc import ABC, abstractmethod


class TicketState(ABC):
    @abstractmethod
    def assign(self, ticket):
        pass

    @abstractmethod
    def resolve(self, ticket):
        pass

    @abstractmethod
    def close(self, ticket):
        pass


class NewState(TicketState):
    def assign(self, ticket):
        ticket.state = AssignedState()
        print("Ticket has been assigned")

    def resolve(self, ticket):
        print("New ticket cannot be resolved without assignment")

    def close(self, ticket):
        ticket.state = ClosedState()
        print("Ticket has been closed.")


class AssignedState(TicketState):
    def assign(self, ticket):
        print("Ticket is already assigned.")

    def resolve(self, ticket):
        ticket.state = ResolvedState()
        print("Ticket has been resolved.")

    def close(self, ticket):
        ticket.state = ClosedState()
        print("Ticket has been closed.")


class ResolvedState(TicketState):
    def assign(self, ticket):
        print("Cannot assign a resolved ticket")

    def resolve(self, ticket):
        print("Ticket is already resolved.")

    def close(self, ticket):
        ticket.state = ClosedState()
        print("Ticket has been closed.")


class ClosedState(TicketState):
    def assign(self, ticket):
        print("Cannot assign closed ticket.")

    def resolve(self, ticket):
        print("Cannot resolve closed ticket.")

    def close(self, ticket):
        print("Ticket is already closed.")


class Ticket:
    def __init__(self):
        self.state = NewState()

    def assign(self):
        self.state.assign(self)

    def resolve(self):
        self.state.resolve(self)

    def close(self):
        self.state.close(self)


def main():
    ticket = Ticket()
    # Test valid state transitions
    ticket.assign()
    ticket.resolve()
    ticket.close()

    # Test invalid state transitions
    ticket.resolve()
    ticket.close()


if __name__ == "__main__":
    main()