def useEffect(callback, dependencies):
    if not hasattr(useEffect, "effects"):
        useEffect.effects = []
    useEffect.effects.append((callback, dependencies))
    return useEffect.effects[-1][0]()
