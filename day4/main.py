import re


file = open("input.txt", "r")
data = file.read().split(sep="\n\n")


class PassportFields:
    """
    Class to hold fields of a passport.
    """

    def __init__(self):
        self.birth_year = None
        self.issue_year = None
        self.expiration_year = None
        self.height = None
        self.hair_color = None
        self.eye_color = None
        self.passport_id = None
        self.country_id = None

    def is_valid(self):
        """
        Tests to see if the passport is valid.

        :return: True if passport is valid.
        """
        if self.birth_year is not None and \
                self.issue_year is not None and \
                self.expiration_year is not None and \
                self.height is not None and \
                self.hair_color is not None and \
                self.eye_color is not None and \
                self.passport_id is not None:
            return self.__is_valid_part2()
        return False

    def __is_valid_part2(self):
        """
        Private method for additional data validation.

        :return: True if passport's data is valid.
        """

        # Check birth year
        if len(self.birth_year) != 4 or int(self.birth_year) not in range(1920, 2003):
            return False

        # Check issue year
        if len(self.issue_year) != 4 or int(self.issue_year) not in range(2010, 2021):
            return False

        # Check expiration year
        if len(self.expiration_year) != 4 or int(self.expiration_year) not in range(2020, 2031):
            return False

        # Check height
        if self.height[-2:] == "cm":
            if int(self.height[:-2]) not in range(150, 194):
                return False
        elif self.height[-2:] == "in":
            if int(self.height[:-2]) not in range(59, 77):
                return False
        else:
            return False

        # Check hair color
        valid_color = re.compile("#[0-9a-f]{6}$")
        if not valid_color.match(self.hair_color):
            return False

        # Check eye color
        if self.eye_color not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        # Check passport id
        valid_pid = re.compile("[0-9]{9}$")
        if not valid_pid.match(self.passport_id):
            return False

        return True


def parse_passport_fields(in_str: str) -> PassportFields:
    """
    Helper to parse a string of passport fields into a data structure.

    :param in_str: string to parse into fields.
    :return: PassportFields containing the data.
    """
    in_str = in_str.replace("\n", " ")
    split_str = in_str.split(sep=" ")

    result = PassportFields()
    for field in split_str:
        key = field[:3]
        if key == "byr":
            result.birth_year = field[4:]
        elif key == "iyr":
            result.issue_year = field[4:]
        elif key == "eyr":
            result.expiration_year = field[4:]
        elif key == "hgt":
            result.height = field[4:]
        elif key == "hcl":
            result.hair_color = field[4:]
        elif key == "ecl":
            result.eye_color = field[4:]
        elif key == "pid":
            result.passport_id = field[4:]
        elif key == "cid":
            result.country_id = field[4:]

    return result


passports = []
valid_count = 0
for d in data:
    passport = parse_passport_fields(d)
    passports.append(passport)
    if passport.is_valid():
        valid_count += 1

print(f"There are {valid_count} 'valid' passports")
