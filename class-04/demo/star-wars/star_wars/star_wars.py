class ForceUser:

    def attacking(self):
        return f'{self.name} is attacking!'

    def getting_hit(self):
        return f'{self.name} is being attacked!'

    @classmethod
    def get_count(cls):
        return JediMaster.count + SithLord.count


class JediMaster(ForceUser):

    count = 0

    def __init__(self, name='Random Jedi'):
        self.name = name
        JediMaster.count += 1

    def __str__(self):
        return f'{self.name} is in the House!'

    def attacking(self):
        return f'{self.name} is Force attacking!'

    @staticmethod
    def get_code():
        return 'There is no emotion!'

    @classmethod
    def get_count(cls):
        return cls.count


class SithLord(ForceUser):

    count = 0

    def __init__(self, name='Random Sith'):
        self.name = name
        SithLord.count += 1

    @staticmethod
    def get_code():
        return 'Peace is a lie!'

    @classmethod
    def get_count(cls):
        return cls.count


if __name__ == '__main__':
    newJedi = JediMaster('Yoda')
    print(f'{newJedi} is here!')

