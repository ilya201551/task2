import functools


@functools.total_ordering
class Version:
    def __init__(self, version: str):
        self.version = version
        self.digit_part = self.getting_digit_part()
        self.letter_part = self.getting_letter_part()

    def to_standard_format(self):
        literal = (('a', '-alpha'), ('b', '-beta'), ('r', '-rc'))
        standard_version = self.version
        if '-' not in standard_version:
            for l in literal:
                standard_version = standard_version.replace(*l)
            return standard_version
        else:
            return standard_version

    def getting_digit_part(self):
        if '-' in self.to_standard_format():
            digit_part = self.to_standard_format().split('-')[0]
        else:
            digit_part = self.to_standard_format()
        return digit_part

    def getting_letter_part(self):
        if '-' in self.to_standard_format():
            letter_part = self.to_standard_format().split('-')[1]
        else:
            letter_part = ''
        return letter_part

    def __eq__(self, other):
        return self.to_standard_format() == other.to_standard_format()

    def __lt__(self, other):
        if self.to_standard_format() != other.to_standard_format():
            if self.digit_part != other.digit_part:
                for i, j in zip(self.digit_part.split('.'), other.digit_part.split('.')):
                    if int(i) < int(j):
                        return True
                    elif int(i) > int(j):
                        return False
            elif self.digit_part == other.digit_part:
                if self.letter_part != '' and other.letter_part == '':
                    return True
                elif self.letter_part == '' and other.letter_part != '':
                    return False
                elif self.letter_part < other.letter_part:
                    return True
                elif self.letter_part > other.letter_part:
                    return False
        else:
            return False


def main():
    to_test = [
        ('1.0.0', '2.0.0'),
        ('1.0.0', '1.42.0'),
        ('1.2.0', '1.2.42'),
        ('1.1.0-alpha', '1.2.0-alpha.1'),
        ('1.0.1b', '1.0.10-alpha.beta'),
        ('1.0.0-rc.1', '1.0.0'),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), 'le failed'
        assert Version(version_2) > Version(version_1), 'ge failed'
        assert Version(version_2) != Version(version_1), 'neq failed'


if __name__ == "__main__":
    main()
