from abc import ABC, abstractmethod


class PlayerState(ABC):
    @abstractmethod
    def play(self, player):
        pass

    @abstractmethod
    def stop(self, player):
        pass

    @abstractmethod
    def pause(self, player):
        pass


class Player:
    def __init__(self):
        self.state = StoppedState()

    def play(self):
        self.state.play(self)

    def stop(self):
        self.state.stop(self)

    def pause(self):
        self.state.pause(self)


class StoppedState(PlayerState):
    def play(self, player):
        player.state = PlayingState()
        print("Player is playing.")

    def stop(self, player):
        print("Player is already stopped.")

    def pause(self, player):
        print("Cannot pause a stopped media.")


class PlayingState(PlayerState):
    def play(self, player):
        print("Media is already playing.")

    def stop(self, player):
        player.state = StoppedState()
        print("Player is stopped.")

    def pause(self, player):
        player.state = PausedState()
        print("Player is paused.")


class PausedState(PlayerState):
    def play(self, player):
        player.state = PlayingState()
        print("Player is playing")

    def stop(self, player):
        player.state = StoppedState()
        print("Player is stopped.")

    def pause(self, player):
        print("PLayer is already paused.")


def main():
    player = Player()
    # Test valid state transitions
    player.play()
    player.pause()
    player.stop()

    # Test invalid state transitions
    player.pause()


if __name__ == "__main__":
    main()
