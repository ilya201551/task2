import functools


@functools.total_ordering
class Version:
    def __init__(self, version: str):
        self.version = version
        self.digit_part = self.getting_digit_part_list()
        self.letter_part = self.getting_letter_part_list()

    def to_standard_format(self):
        literals = (('a', '-alpha'), ('b', '-beta'), ('r', '-rc'))
        standard_version = self.version
        if '-' not in standard_version:
            for literal in literals:
                standard_version = standard_version.replace(*literal)
            return standard_version
        else:
            return standard_version

    def getting_digit_part(self):
        if '-' in self.to_standard_format():
            digit_part = self.to_standard_format().split('-')[0]
        else:
            digit_part = self.version
        return digit_part

    def getting_letter_part(self):
        if '-' in self.to_standard_format():
            letter_part = self.to_standard_format().split('-')[1]
        else:
            letter_part = '0'
        return letter_part

    def getting_digit_part_list(self):
        digit_part_list = [int(i) for i in self.getting_digit_part().split('.')]
        return digit_part_list

    def getting_letter_part_list(self):
        literals = (('alpha', '-3'), ('beta', '-2'), ('rc', '-1'))
        letter_part = self.getting_letter_part()
        for literal in literals:
            letter_part = letter_part.replace(*literal)
        letter_part_list = [int(i) for i in letter_part.split('.')]
        return letter_part_list

    def __eq__(self, other):
        return self.to_standard_format() == other.to_standard_format()

    def __lt__(self, other):
        if self.digit_part == other.digit_part:
            return self.letter_part < other.letter_part
        else:
            return self.digit_part < other.digit_part


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
        assert Version(version_1) < Version(version_2), 'le failed' + version_1
        assert Version(version_2) > Version(version_1), 'ge failed' + version_1
        assert Version(version_2) != Version(version_1), 'neq failed' + version_1


if __name__ == "__main__":
    main()
