class GlobalStateManager:
    def __init__(self):
        self.state = {}

    def set(self, key, value):
        self.state[key] = value

    def get(self, key):
        return self.state[key]

    def remove(self, key):
        del self.state[key]

    def clear(self):
        self.state = {}

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
