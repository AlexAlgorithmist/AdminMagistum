from dataclasses import dataclass


LOCK = [
    """PRAGMA locking_mode = EXCLUSIVE""",
    """BEGIN EXCLUSIVE""",
]
UNLOCK = [
    """COMMIT""",
    """PRAGMA locking_mode = NORMAL""",
    """SELECT id FROM people LIMIT 1""",
]


@dataclass
class SCHEDULE_STATIC:
    make = """
    CREATE TABLE IF NOT EXISTS schedule_static (
        lesson_id INTEGER PRIMARY KEY AUTOINCREMENT,
        place INTEGER,
        person INTEGER,
        type INTEGER,
        day INTEGER,
        time_begin INTEGER,
        time_end INTEGER,
        FOREIGN KEY (place) REFERENCES places(id),
        FOREIGN KEY (person) REFERENCES people(id),
        FOREIGN KEY (type) REFERENCES lessons_types(id),
        FOREIGN KEY (day) REFERENCES days(id)
    );
    """
    add = """
    INSERT INTO
        schedule_static (place, person, type, day, time_begin, time_end)
    VALUES
        (?, ?, ?, ?, ?, ?)
    """
    drop = """DROP TABLE schedule_static"""
    select_by_person = """
    SELECT
        lesson_id, place, type, day, time_begin, time_end
    FROM
        schedule_static
    WHERE
        person = ?
    """
    select_by_day = """
    SELECT
        lesson_id, place, person, type, time_begin, time_end
    FROM
        schedule_static
    WHERE
        day = ?
    """
    select_by_person_and_day = """
    SELECT
        lesson_id, place, type, time_begin, time_end
    FROM
        schedule_static
    WHERE
        person = ? and day = ?
    """


@dataclass
class PLACES:
    make = """
    CREATE TABLE IF NOT EXISTS places (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    );
    """
    add = """
    INSERT INTO
        places (name)
    VALUES
        (?)
    """
    drop = """DROP TABLE places"""


# got abolished
@dataclass
class TEACHERS:
    make = """
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        surname TEXT,
        name TEXT,
        patronymic TEXT,
        tg_id INTEGER,
        state INTEGER,
        FOREIGN KEY (state) REFERENCES teacher_states(id)
    );
    """
    add = """
    INSERT INTO
        teachers (surname, name, patronymic, tg_id, state)
    VALUES
        (?, ?, ?, ?, ?)
    """
    drop = """DROP TABLE teachers"""

    teachers_id = """
    SELECT
        id
    FROM
        teachers
    """
    select_by_id = """
    SELECT
        surname, name, patronymic, tg_id, state
    FROM
        teachers
    WHERE
        id = ?
    """

    change_surname = """
    UPDATE
        teachers
    SET
        surname = ?
    WHERE
        id = ?
    """
    change_name = """
    UPDATE
        teachers
    SET
        name = ?
    WHERE
        id = ?
    """
    change_patronymic = """
    UPDATE
        teachers
    SET
        patronymic = ?
    WHERE
        id = ?
    """
    change_tg_id = """
    UPDATE
        teachers
    SET
        tg_id = ?
    WHERE
        id = ?
    """
    change_state = """
    UPDATE
        teachers
    SET
        state = ?
    WHERE
        id = ?
    """


@dataclass
class PEOPLE:
    make = """
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        surname TEXT,
        name TEXT,
        patronymic TEXT,
        tg_id INTEGER
    );
    """
    add = """
    INSERT INTO
        people (surname, name, patronymic, tg_id)
    VALUES
        (?, ?, ?, ?)
    """
    drop = """DROP TABLE people"""

    people_id = """
    SELECT
        id
    FROM
        people
    """
    select_by_id = """
    SELECT
        surname, name, patronymic, tg_id
    FROM
        people
    WHERE
        id = ?
    """
    select_by_tg_id = """
    SELECT
        id, surname, name, patronymic
    FROM
        people
    WHERE
        tg_id = ?
    """

    change_surname = """
    UPDATE
        people
    SET
        surname = ?
    WHERE
        id = ?
    """
    change_name = """
    UPDATE
        people
    SET
        name = ?
    WHERE
        id = ?
    """
    change_patronymic = """
    UPDATE
        people
    SET
        patronymic = ?
    WHERE
        id = ?
    """


@dataclass
class LESSONS_TYPES:
    make = """
    CREATE TABLE IF NOT EXISTS lessons_types (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    );
    """
    add = """
    INSERT INTO
        lessons_types (name)
    VALUES
        (?)
    """
    drop = """DROP TABLE lessons_types"""
    get = """
    SELECT
        name
    FROM
        lesson_types
    WHERE
        id = ?
    """


@dataclass
class DAYS:
    make = """
    CREATE TABLE IF NOT EXISTS days (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    );
    """
    add = """
    INSERT INTO
        days (name)
    VALUES
        (?)
    """
    drop = """DROP TABLE days"""


# got abolished
@dataclass
class TEACHER_STATES:
    make = """
    CREATE TABLE IF NOT EXISTS teacher_states (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    );
    """
    add = """
    INSERT INTO
        teacher_states (name)
    VALUES
        (?)
    """
    drop = """DROP TABLE teacher_states"""


@dataclass
class PEOPLE_STATES_NAMES:
    make = """
    CREATE TABLE IF NOT EXISTS people_states_names (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    );
    """
    add = """
    INSERT INTO
        people_states_names (name)
    VALUES
        (?)
    """
    drop = """DROP TABLE people_states_names"""


@dataclass
class PEOPLE_STATES:
    make = """
    CREATE TABLE IF NOT EXISTS people_states (
        person_id INTEGER,
        state_id INTEGER,
        FOREIGN KEY (person_id) REFERENCES people(id),
        FOREIGN KEY (state_id) REFERENCES people_states_names(id)
    );
    """
    add = """
    INSERT INTO
        people_states (person_id, state_id)
    VALUES
        (?, ?)
    """
    drop = """DROP TABLE people_states"""


@dataclass
class PEOPLE_ROLES_NAMES:
    make = """
    CREATE TABLE IF NOT EXISTS people_roles_names (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    );
    """
    add = """
    INSERT INTO
        people_roles_names (name)
    VALUES
        (?)
    """
    drop = """DROP TABLE people_roles_names"""


@dataclass
class PEOPLE_ROLES:
    make = """
    CREATE TABLE IF NOT EXISTS people_roles (
        person_id INTEGER,
        role_id INTEGER,
        FOREIGN KEY (person_id) REFERENCES people(id),
        FOREIGN KEY (role_id) REFERENCES people_roles_names(id)
    );
    """
    add = """
    INSERT INTO
        people_roles (person_id, role_id)
    VALUES
        (?, ?)
    """
    drop = """DROP TABLE people_roles"""
    get_role = """
    SELECT
        role_id
    FROM
        people_roles
    WHERE
        person_id = ?
    """


@dataclass
class SCHEDULE_LOCAL:
    make = """
    CREATE TABLE IF NOT EXISTS schedule_local (
        lesson_id INTEGER PRIMARY KEY AUTOINCREMENT,
        place INTEGER,
        person INTEGER,
        type INTEGER,
        day INTEGER,
        time_begin INTEGER,
        time_end INTEGER,
        FOREIGN KEY (place) REFERENCES places(id),
        FOREIGN KEY (person) REFERENCES people(id),
        FOREIGN KEY (type) REFERENCES lessons_types(id),
        FOREIGN KEY (day) REFERENCES days(id)
    );
    """
    add = """
    INSERT INTO
        schedule_local (place, person, type, day, time_begin, time_end)
    VALUES
        (?, ?, ?, ?, ?, ?)
    """
    drop = """DROP TABLE schedule_local"""
    select_by_person = """
    SELECT
        lesson_id, place, type, day, time_begin, time_end
    FROM
        schedule_local
    WHERE
        person = ?
    """
    select_by_day = """
    SELECT
        lesson_id, place, person, type, time_begin, time_end
    FROM
        schedule_local
    WHERE
        day = ?
    """
    select_by_person_and_day = """
    SELECT
        lesson_id, place, type, time_begin, time_end
    FROM
        schedule_local
    WHERE
        person = ? and day = ?
    """


@dataclass
class BREAKS:
    make = """
    CREATE TABLE IF NOT EXISTS breaks (
        break_id INTEGER PRIMARY KEY AUTOINCREMENT,
        place INTEGER,
        year_from INTEGR,
        month_from INTEGR,
        day_from INTEGR,
        year_to INTEGR,
        month_to INTEGR,
        day_to INTEGR,
        FOREIGN KEY (place) REFERENCES places(id)
    );
    """
    add = """
    INSERT INTO
        breaks (place, year_from, month_from, day_from, year_to, month_to, day_to)
    VALUES
        (?, ?, ?, ?, ?, ?, ?)
    """
    drop = """DROP TABLE breaks"""
    select_all = """
    SELECT
        place, year_from, month_from, day_from, year_to, month_to, day_to
    FROM
        breaks
    """
    get_by_id = """
    SELECT
        place, year_from, month_from, day_from, year_to, month_to, day_to
    FROM
        breaks
    WHERE
        break_id = ?
    """
    get_by_place = """
    SELECT
        year_from, month_from, day_from, year_to, month_to, day_to
    FROM
        breaks
    WHERE
        place = ?
    """


@dataclass
class CHANGES:
    make = """
    CREATE TABLE IF NOT EXISTS changes (
        change_id INTEGER PRIMARY KEY AUTOINCREMENT,
        lesson_id INTEGER,
        change_person INTEGER,
        year INTEGR,
        month INTEGR,
        day INTEGR,
        comment TEXT,
        FOREIGN KEY (lesson_id) REFERENCES schedule_static(lesson_id),
        FOREIGN KEY (change_person) REFERENCES people(id)
    );
    """
    add = """
    INSERT INTO
        changes (lesson_id, change_person, year, month, day, comment)
    VALUES
        (?, ?, ?, ?, ?, ?)
    """
    drop = """DROP TABLE changes"""
    select_all = """
    SELECT
        lesson_id, change_person, year, month, day
    FROM
        changes
    """


@dataclass
class PEOPLE_RIGHTS:
    make = """
    CREATE TABLE IF NOT EXISTS people_rights (
        right_id INTEGER PRIMARY KEY AUTOINCREMENT,
        person INTEGER,
        action INTEGER,
        table_id INTEGER,
        FOREIGN KEY (person) REFERENCES people(id),
        FOREIGN KEY (action) REFERENCES actions(id),
        FOREIGN KEY (table_id) REFERENCES tables(id)
    );
    """
    add = """
    INSERT INTO
        people_rights (person, action, table_id)
    VALUES
        (?, ?, ?)
    """
    drop = """DROP TABLE people_rights"""
    select_all = """
    SELECT
        person, action, table_id
    FROM
        people_rights
    """
    select_by_person = """
    SELECT
        action, table_id
    FROM
        people_rights
    WHERE
        person = ?
    """


@dataclass
class ROLE_RIGHTS:
    make = """
    CREATE TABLE IF NOT EXISTS role_rights (
        right_id INTEGER PRIMARY KEY AUTOINCREMENT,
        role INTEGER,
        action INTEGER,
        table_id INTEGER,
        FOREIGN KEY (role) REFERENCES roles(id),
        FOREIGN KEY (action) REFERENCES actions(id),
        FOREIGN KEY (table_id) REFERENCES tables(id)
    );
    """
    add = """
    INSERT INTO
        role_rights (role, action, table_id)
    VALUES
        (?, ?, ?)
    """
    drop = """DROP TABLE role_rights"""
    select_all = """
    SELECT
        role, action, table_id
    FROM
        role_rights
    """
    select_by_role = """
    SELECT
        action, table_id
    FROM
        role_rights
    WHERE
        role = ?
    """


@dataclass
class ACTIONS:
    make = """
    CREATE TABLE IF NOT EXISTS actions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        abbreviation TEXT
    );
    """
    add = """
    INSERT INTO
        actions (name, abbreviation)
    VALUES
        (?, ?)
    """
    drop = """DROP TABLE actions"""
    get_abbreviation_by_id = """
    SELECT
        abbreviation
    FROM
        actions
    WHERE
        id = ?
    """
    get_abbreviations = """
    SELECT
        abbreviation
    FROM
        actions
    """


@dataclass
class TABLES:
    make = """
    CREATE TABLE IF NOT EXISTS tables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        abbreviation TEXT
    );
    """
    add = """
    INSERT INTO
        tables (name, abbreviation)
    VALUES
        (?, ?)
    """
    drop = """DROP TABLE tables"""
    get_abbreviation_by_id = """
    SELECT
        abbreviation
    FROM
        tables
    WHERE
        id = ?
    """
    get_abbreviations = """
    SELECT
        abbreviation
    FROM
        tables
    """


@dataclass
class USERNAMES_TG:
    make = """
    CREATE TABLE IF NOT EXISTS usernames_tg (
        tg_id INTEGER,
        username TEXT,
        FOREIGN KEY (tg_id) REFERENCES people(tg_id)
    );
    """
    add = """
    INSERT INTO
        usernames_tg (name)
    VALUES
        (?)
    """
    drop = """DROP TABLE usernames_tg"""
