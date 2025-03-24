from dataclasses import dataclass


@dataclass
class GOOD:
    EVERYTHING_IS_GOOD = "EIG"


@dataclass
class ERROR:
    INTERSEPTION = "I"
    NOT_FOUND = "NF"
    UNKNOWN_ACTION = "UKA"
    UNKNOWN_TABLE = "UKT"
    NO_RIGHTS = "NRI"
    INCORRECT_AMOUNT_OF_ARGUMENTS = "IAA"  # TODO: it should be "IAoA" or "IAOA"
    INCORRECT_ARGUMENTS = "IA"
    SQL = "SQL"
    RIGHTS_NOT_FOUND = "RINF"
    ROLE_NOT_FOUND = "RONF"


@dataclass
class WARNING:
    DIFFERENT_PLACES = "DP"


@dataclass
class ACTIONS:
    CREATE = "CR"
    ADD = "A"
    CHANGE = "CH"
    DELETE = "DE"
    VEIW = "V"
    DROP = "D"


@dataclass
class TABLES:
    ACTIONS = "A"
    BREAKS = "BR"
    CHANGES = "CH"
    DAYS = "D"
    LESSON_TYPES = "LT"
    PEOPLE = "PE"
    PEOPLE_RIGHTS = "PERI"
    PEOPLE_ROLES = "PERO"
    PEOPLE_ROLES_NAMES = "PERON"
    PEOPLE_STATES = "PES"
    PEOPLE_STATES_NAMES = "PESN"
    PLACES = "PL"
    ROLE_RIGHTS = "RORI"
    SCHEDULE_LOCAL = "SCL"
    SCHEDULE_STATIC = "SCS"
    TABLES = "T"
    TEACHERS = "TC"
    TEACHERS_STATES = "TCS"
    USERNAME_TG = "UNTG"
