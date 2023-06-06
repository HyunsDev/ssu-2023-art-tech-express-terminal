def useState(initialState):
    state = initialState

    def setState(newState):
        nonlocal state
        state = newState

    return (state, setState)
