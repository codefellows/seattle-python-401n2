class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician:
    pass

class Guitarist:
    pass

class Bassist:
    pass

class Drummer:
    pass
