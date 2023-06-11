def P5React():
    hooks = {}

    def render(component, *args, **kwargs):
        comp = component(*args, **kwargs)
        return comp

    def getHook(keys):
        nonlocal hooks

        hook = hooks
        for key in keys:
            hook = hook.get(key, {})

        return hook.get("__value", None)

    def setHook(keys, value):
        nonlocal hooks

        hook = hooks
        for key in keys:
            hook[key] = hook.get(key, {})
            hook = hook[key]

        hook["__value"] = value

    def resetHook(keys):
        nonlocal hooks

        hook = hooks
        for key in keys:
            if key not in hook:
                return
            if key == keys[-1]:

                def cleanUp(hook):
                    value = hook.get("__value", None)
                    if (
                        isinstance(value, dict)
                        and "cleanUp" in value
                        and callable(value["cleanUp"])
                    ):
                        value["cleanUp"]()

                    keys = hook.keys()
                    for key in keys:
                        if key == "__value":
                            continue
                        cleanUp(hook[key])

                cleanUp(hook[key])

                del hook[key]
            else:
                hook = hook[key]

    def useEffect(keys, effect, depArray=None):
        key = [*keys, "useEffect"]

        nonlocal hooks
        hasNoDeps = depArray is None

        if getHook(key) is None:
            cleanUp = effect()
            setHook(key, {"deps": depArray, "cleanUp": cleanUp})

        deps = getHook(key)
        hasChangedDeps = deps["deps"] and (
            depArray is None
            or not all(dep == deps["deps"][i] for i, dep in enumerate(depArray))
        )

        if hasNoDeps or hasChangedDeps:
            cleanUp = effect()
            setHook(key, {"deps": depArray, "cleanUp": cleanUp})

    def useState(keys, initialValue):
        key = [*keys, "useState"]

        nonlocal hooks

        if getHook(key) is None:
            setHook(key, initialValue)

        def setState(newState):
            nonlocal hooks
            if callable(newState):
                newState = newState(getHook(key))

            setHook(key, newState)

        return [getHook(key), setState]

    def useRef(keys, initialValue):
        key = [*keys, "useRef"]

        nonlocal hooks

        if getHook(key) is None:
            setHook(key, {"current": initialValue})

        return getHook(key)

    def refresh():
        nonlocal hooks

    return {
        "useState": useState,
        "useEffect": useEffect,
        "render": render,
        "refresh": refresh,
        "useRef": useRef,
        "resetHook": resetHook,
    }


p5react = P5React()
render = p5react["render"]
useEffect = p5react["useEffect"]
useState = p5react["useState"]
useRef = p5react["useRef"]
refresh = p5react["refresh"]
resetHook = p5react["resetHook"]
__all__ = ["render", "useEffect", "useState", "useRef", "refresh", "resetHook"]
