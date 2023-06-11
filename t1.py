hooks = {}


def getHook(keys):
    global hooks

    hook = hooks
    for key in keys:
        hook = hook.get(key, {})

    return hook.get("__value", None)


def setHook(keys, value):
    global hooks

    hook = hooks
    for key in keys:
        hook[key] = hook.get(key, {})
        hook = hook[key]

    hook["__value"] = value


def resetHook(keys):
    global hooks

    hook = hooks
    for key in keys:
        if key not in hook:
            return
        if key == keys[-1]:

            def cleanUp(hook):
                value = hook.get("__value", None)
                if isinstance(value, dict) and "cleanUp" in value:
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


setHook(["a", "b", "c"], "e")
setHook(["a", "b", "c", "d", "e"], {"cleanUp": lambda: print("CleanUp")})


resetHook(["a", "b", "c"])


print(getHook(["a", "b", "c"]))
print(getHook(["a", "b", "c", "d", "e"]))
