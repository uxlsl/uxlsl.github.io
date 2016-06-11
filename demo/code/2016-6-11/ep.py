
def f(scores):
    total = sum(scores)
    return [i / total for i in scores]

print f(i for i in range(100))


class ReadVisits(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path) as f:
            for line in f:
                yield line
