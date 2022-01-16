from contextlib import ExitStack

# Sometimes you want to run a code block with multiple context managers:

with open('f') as f:
    with open('g') as g:
        with open('h') as h:
            pass

# Since Python 2.7 and 3.1, you can do it with a single with expression:

o = open
with o('f') as f, o('g') as g, o('h') as h:
    pass

# Before that, you could you use the contextlib.nested function:

with nested(o('f'), o('g'), o('h')) as (f, g, h):
    pass

# If you are working with the uknown number of context manager,
# the more advanced tool suits you well. contextlib.ExitStack 
# allows you to enter any number of contexts at the arbitrary time but
# guarantees to exit them at the end:

with ExitStack() as stack:
    f = stack.enter_context(o('f'))
    g = stack.enter_context(o('g'))
    other = [
        stack.enter_context(o(filename))
        for filename in filenames
    ]