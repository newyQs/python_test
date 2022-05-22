

try:
    res = await shield(something())
except CancelledError:
    res = None
