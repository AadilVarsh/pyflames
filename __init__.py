

class Flames:
    """
    fun python module to automate the classic 90s game Flames

    """

    def __init__(self, name_a, name_b):
        self.name_a = name_a
        self.name_b = name_b

        self.flames = "FLAMES"

        self.tags = {
            'f': 'friends',
            'l': 'lovers',
            'a': 'affection',
            'm': 'marriage',
            'e': 'enemies',
            's': 'siblings',
        }

        _name_a, _name_b = self.name_a, self.name_b

        for char_a in _name_a:
            for char_b in _name_b:
                if char_a == char_b:
                    _name_a.replace(char_a, str())
                    _name_b.replace(char_b, str())

        len_no = len(_name_a) + len(_name_b)

        rem = len_no % 6

        while rem > 6:
            rem = rem % 6

        self.flame = self.flames[rem - 1]

    def find_it(self):

        return self.flame


if __name__ == "__main__":
    pass
