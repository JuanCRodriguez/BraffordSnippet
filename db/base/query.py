class Query:

    def __init__(self, q):
        self._q = q

    def __getattr__(self, item):
        attr = getattr(self._q, item)

        if not callable(attr):
            return attr

        def wrapper(*args, **kwargs):
            self._q = attr(*args, **kwargs)
            return self
        return wrapper

    def __repr__(self):
        return repr(self._q)