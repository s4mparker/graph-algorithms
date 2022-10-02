
def supercall(func):
    """ When used as a decorator, the superclass' respective method 
    will be called prior to the subclass' respective method being called.

    An optional keyword argument is available (skip_supercall) which can
    be used to skip the calling of the superclass' method.

    The values returned by the subclass' method call will be returned.
    """

    def inner(*args, **kwargs):
        args = list(args)
        obj  = args.pop(0)
        args = tuple(args)

        skip_supercall = kwargs.pop('skip_supercall', False)
        superfunc = getattr(super(type(obj), obj), func.__name__, None)

        if not skip_supercall and superfunc:
            superfunc(*args, **kwargs)
        return func(obj, *args, **kwargs)
    return inner