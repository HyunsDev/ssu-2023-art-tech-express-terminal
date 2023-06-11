from p5react import *


class GlobalState:
    def __init__(self, state):
        self.state = state

    def setState(self, state):
        if callable(state):
            state = state(self.state)

        self.state = state

    def getState(self):
        return self.state


def useGlobalState(globalState):
    return [globalState.state, globalState.setState]
