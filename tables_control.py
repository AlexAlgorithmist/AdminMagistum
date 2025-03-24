import mylibs.DBMS as DBMS
from DBMS_texts import *
from pprint import pprint


connection = ...


def setup(path: str) -> None | DBMS.Error:
    global connection
    connection = DBMS.create_connection(f"{path}")
    if connection is not None:
        return connection


def teachers() -> list[tuple[int]] | DBMS.Error:
    # res = DBMS.execute_read_query(connection, TEACHERS.teachers_id)
    # print(DBMS.error, DBMS.error_text)
    # print(res)
    return DBMS.execute_read_query(connection, TEACHERS.teachers_id)


def lock() -> None | DBMS.Error:
    """
    Do not work.
    :return: no return.
    """
    for text in LOCK:
        error = DBMS.execute_read_query(connection, text)
        if error is not None:
            return error


def unlock() -> None | DBMS.Error:
    """
    Do not work.
    :return: no return.
    """
    for text in UNLOCK:
        error = DBMS.execute_read_query(connection, text)
        if error is not None:
            return error


class add:
    @staticmethod
    def lesson_static(place: int, person: int, type_lesson: int, day: int, time_begin: int, time_end: int) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, SCHEDULE_STATIC.add, (place, person, type_lesson, day, time_begin, time_end))

    @staticmethod
    def lesson_local(place: int, person: int, type_lesson: int, day: int, time_begin: int, time_end: int) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, SCHEDULE_LOCAL.add, (place, person, type_lesson, day, time_begin, time_end))

    @staticmethod
    def place(name: str) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, PLACES.add, (name,))

    @staticmethod
    def lesson_type(name: str) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, LESSONS_TYPES.add, (name,))

    @staticmethod
    def day(name: str) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, DAYS.add, (name,))

    @staticmethod
    def break_place(place: int, year_from: int, month_from: int, day_from: int, year_to: int, month_to: int, day_to: int) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, BREAKS.add, (place, year_from, month_from, day_from, year_to, month_to, day_to))

    @staticmethod
    def change(place: int, changer: int, year: int, month: int, day: int, comment: str) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, CHANGES.add, (place, changer, year, month, day, comment))

    @staticmethod
    def person(name: str, surname: str, patronymic: str, tg_id: int) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, PEOPLE.add, (name, surname, patronymic, tg_id))

    @staticmethod
    def person_state(person_id: int, state: int) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, PEOPLE_STATES.add, (person_id, state))

    @staticmethod
    def person_role(person_id: int, role: int) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, PEOPLE_ROLES.add, (person_id, role))

    @staticmethod
    def username_tg(tg_id: int, username: int) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, USERNAMES_TG.add, (tg_id, username))

    @staticmethod
    def person_right(person_id: int, action: int, table: int) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, PEOPLE_RIGHTS.add, (person_id, action, table))

    @staticmethod
    def role_right(role: int, action: int, table: int) -> None | DBMS.Error:
        return DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (role, action, table))


class change:
    @staticmethod
    def surname(person_id: int, surname: str) -> None | DBMS.Error:
        error = DBMS.execute_query_values(connection, TEACHERS.change_surname, (surname, person_id))
        if error is not None:
            return error

    @staticmethod
    def name(person_id: int, name: str) -> None | DBMS.Error:
        error = DBMS.execute_query_values(connection, TEACHERS.change_name, (name, person_id))
        if error is not None:
            return error

    @staticmethod
    def patronymic(person_id: int, patronymic: str) -> None | DBMS.Error:
        error = DBMS.execute_query_values(connection, TEACHERS.change_patronymic, (patronymic, person_id))
        if error is not None:
            return error

    @staticmethod
    def tg_id(person_id: int, tg_id: int) -> None | DBMS.Error:
        error = DBMS.execute_query_values(connection, TEACHERS.change_tg_id, (tg_id, person_id))
        if error is not None:
            return error

    @staticmethod
    def state(person_id: int, state: int) -> None | DBMS.Error:
        error = DBMS.execute_query_values(connection, TEACHERS.change_state, (state, person_id))
        if error is not None:
            return error


class get:
    @staticmethod
    def person_by_id(person_id: int) -> tuple[str, str, str, int] | DBMS.Error:
        error = DBMS.execute_read_query_values(connection, PEOPLE.select_by_id, (person_id,))
        if type(error) != list:
            return error
        return error[0]

    @staticmethod
    def person_by_tg_id(person_tg_id: int) -> tuple[int, str, str, str] | DBMS.Error:
        error = DBMS.execute_read_query_values(connection, PEOPLE.select_by_tg_id, (person_tg_id,))
        if type(error) != list or not error:
            return error
        return error[0]

    @staticmethod
    def people() -> list[tuple[int]] | DBMS.Error:
        return DBMS.execute_read_query(connection, PEOPLE.people_id)

    @staticmethod
    def by_day_static(day: int) -> list[tuple[int, int, int, int, int, int]] | DBMS.Error:
        return DBMS.execute_read_query_values(connection, SCHEDULE_STATIC.select_by_day, (day,))

    @staticmethod
    def by_person_static(person: int) -> list[tuple[int, int, int, int, int, int]] | DBMS.Error:
        return DBMS.execute_read_query_values(connection, SCHEDULE_STATIC.select_by_person, (person,))

    @staticmethod
    def by_day_and_person_static(person: int, day: int) -> list[tuple[int, int, int, int, int]] | DBMS.Error:
        return DBMS.execute_read_query_values(connection, SCHEDULE_STATIC.select_by_person_and_day, (person, day))


    @staticmethod
    def by_day_local(day: int) -> list[tuple[int, int, int, int, int, int]] | DBMS.Error:
        return DBMS.execute_read_query_values(connection, SCHEDULE_LOCAL.select_by_day, (day,))

    @staticmethod
    def by_person_local(person: int) -> list[tuple[int, int, int, int, int, int]] | DBMS.Error:
        return DBMS.execute_read_query_values(connection, SCHEDULE_LOCAL.select_by_person, (person,))

    @staticmethod
    def by_day_and_person_local(person: int, day: int) -> list[tuple[int, int, int, int, int]] | DBMS.Error:
        return DBMS.execute_read_query_values(connection, SCHEDULE_LOCAL.select_by_person_and_day, (person, day))


    @staticmethod
    def role(person_id: int) -> int | DBMS.Error:
        error = DBMS.execute_read_query_values(connection, PEOPLE_ROLES.get_role, (person_id,))
        if type(error) != list:
            return error
        return error[0][0]

    @staticmethod
    def rights_by_role(role: int) -> list[tuple[int, int]] | DBMS.Error:
        return DBMS.execute_read_query_values(connection, ROLE_RIGHTS.select_by_role, (role,))

    @staticmethod
    def person_rights(person_id: int) -> list[tuple[int, int]] | DBMS.Error:
        return DBMS.execute_query_values(connection, PEOPLE_RIGHTS.select_by_person, (person_id,))

    @staticmethod
    def lesson_type(index: int) -> str | DBMS.Error:
        return DBMS.execute_read_query_values(connection, LESSONS_TYPES.get, (index,))

    @staticmethod
    def all_breaks() -> list[tuple[int, int, int, int, int, int, int]] | DBMS.Error:
        return DBMS.execute_read_query(connection, BREAKS.select_all)

    @staticmethod
    def break_by_id(index: int) -> tuple[int, int, int, int, int, int, int] | DBMS.Error:
        error = DBMS.execute_read_query_values(connection, BREAKS.get_by_id, (index,))
        if type(error) != list:
            return error
        return error[0]

    @staticmethod
    def breaks_by_place(place: int) -> list[tuple[int, int, int, int, int, int]] | DBMS.Error:
        return DBMS.execute_read_query_values(connection, BREAKS.get_by_place, (place,))

    @staticmethod
    def all_changes() -> list[tuple[int, int, int, int, int, str]] | DBMS.Error:
        return DBMS.execute_read_query(connection, CHANGES.select_all)


    @staticmethod
    def action_abbreviation_by_id(action_id: int) -> str | DBMS.Error:
        error = DBMS.execute_read_query_values(connection, ACTIONS.get_abbreviation_by_id, (action_id,))
        if type(error) != list:
            return error
        return error[0][0]

    @staticmethod
    def table_abbreviation_by_id(table_id: int) -> str | DBMS.Error:
        error = DBMS.execute_read_query_values(connection, TABLES.get_abbreviation_by_id, (table_id,))
        if type(error) != list:
            return error
        return error[0][0]

    @staticmethod
    def action_abbreviations() -> list[tuple[str]] | DBMS.Error:
        return DBMS.execute_read_query(connection, ACTIONS.get_abbreviations)

    @staticmethod
    def table_abbreviations() -> list[tuple[str]] | DBMS.Error:
        return DBMS.execute_read_query(connection, TABLES.get_abbreviations)


if __name__ == "__main__":
    from random import randint, choice
    import sys
    connection = DBMS.create_connection(f"{sys.path[0]}\\database.sqlite")
    def recreate():
        print("In 'recreate':")
        DBMS.execute_query(connection, SCHEDULE_STATIC.drop)
        DBMS.execute_query(connection, SCHEDULE_LOCAL.drop)
        DBMS.execute_query(connection, BREAKS.drop)
        DBMS.execute_query(connection, CHANGES.drop)
        DBMS.execute_query(connection, PLACES.drop)
        DBMS.execute_query(connection, TEACHERS.drop)
        DBMS.execute_query(connection, PEOPLE.drop)
        DBMS.execute_query(connection, LESSONS_TYPES.drop)
        DBMS.execute_query(connection, DAYS.drop)
        DBMS.execute_query(connection, TEACHER_STATES.drop)
        DBMS.execute_query(connection, PEOPLE_STATES.drop)
        DBMS.execute_query(connection, PEOPLE_STATES_NAMES.drop)
        DBMS.execute_query(connection, PEOPLE_ROLES.drop)
        DBMS.execute_query(connection, PEOPLE_ROLES_NAMES.drop)
        DBMS.execute_query(connection, PEOPLE_RIGHTS.drop)
        DBMS.execute_query(connection, ROLE_RIGHTS.drop)
        DBMS.execute_query(connection, ACTIONS.drop)
        DBMS.execute_query(connection, TABLES.drop)
        DBMS.execute_query(connection, USERNAMES_TG.drop)
        print("  Tables dropped.")

        # DBMS.execute_query(connection, TEACHER_STATES.make)
        DBMS.execute_query(connection, PEOPLE_STATES_NAMES.make)
        DBMS.execute_query(connection, PEOPLE_STATES.make)
        DBMS.execute_query(connection, PEOPLE_ROLES_NAMES.make)
        DBMS.execute_query(connection, PEOPLE_ROLES.make)
        DBMS.execute_query(connection, PEOPLE_RIGHTS.make)
        DBMS.execute_query(connection, ROLE_RIGHTS.make)
        DBMS.execute_query(connection, ACTIONS.make)
        DBMS.execute_query(connection, TABLES.make)
        DBMS.execute_query(connection, USERNAMES_TG.make)

        DBMS.execute_query(connection, PLACES.make)
        # DBMS.execute_query(connection, TEACHERS.make)
        DBMS.execute_query(connection, PEOPLE.make)
        DBMS.execute_query(connection, LESSONS_TYPES.make)
        DBMS.execute_query(connection, DAYS.make)
        DBMS.execute_query(connection, SCHEDULE_STATIC.make)
        DBMS.execute_query(connection, SCHEDULE_LOCAL.make)
        DBMS.execute_query(connection, BREAKS.make)
        DBMS.execute_query(connection, CHANGES.make)
        print("  Tables made.")

    def makeBasic():
        print("In 'makeBasic':")
        DBMS.execute_query_values(connection, ACTIONS.add, ("Создать", "CR"))
        DBMS.execute_query_values(connection, ACTIONS.add, ("Добавить", "A"))
        DBMS.execute_query_values(connection, ACTIONS.add, ("Изменить", "CH"))
        DBMS.execute_query_values(connection, ACTIONS.add, ("Удалить", "DE"))
        DBMS.execute_query_values(connection, ACTIONS.add, ("Просмотреть", "V"))
        DBMS.execute_query_values(connection, ACTIONS.add, ("Сборосить", "D"))
        print("  Actions added.")
        DBMS.execute_query_values(connection, TABLES.add, ("schedule_static", "SCS"))
        DBMS.execute_query_values(connection, TABLES.add, ("places", "PL"))
        DBMS.execute_query_values(connection, TABLES.add, ("teachers", "TC"))
        DBMS.execute_query_values(connection, TABLES.add, ("people", "PE"))
        DBMS.execute_query_values(connection, TABLES.add, ("lessons_types", "LT"))
        DBMS.execute_query_values(connection, TABLES.add, ("days", "D"))
        DBMS.execute_query_values(connection, TABLES.add, ("teacher_states", "TCS"))
        DBMS.execute_query_values(connection, TABLES.add, ("people_states_names", "PESN"))
        DBMS.execute_query_values(connection, TABLES.add, ("people_states", "PES"))
        DBMS.execute_query_values(connection, TABLES.add, ("people_roles_names", "PERON"))
        DBMS.execute_query_values(connection, TABLES.add, ("people_roles", "PERO"))
        DBMS.execute_query_values(connection, TABLES.add, ("schedule_local", "SCL"))
        DBMS.execute_query_values(connection, TABLES.add, ("breaks", "BR"))
        DBMS.execute_query_values(connection, TABLES.add, ("changes", "CH"))
        DBMS.execute_query_values(connection, TABLES.add, ("people_rights", "PERI"))
        DBMS.execute_query_values(connection, TABLES.add, ("roles_rights", "RORI"))
        DBMS.execute_query_values(connection, TABLES.add, ("actions", "A"))
        DBMS.execute_query_values(connection, TABLES.add, ("tables", "T"))
        DBMS.execute_query_values(connection, TABLES.add, ("usernames_tg", "UNTG"))
        print("  Tables added.")
        DBMS.execute_query_values(connection, PEOPLE_ROLES_NAMES.add, ("Человек",))
        DBMS.execute_query_values(connection, PEOPLE_ROLES_NAMES.add, ("Учитель",))
        DBMS.execute_query_values(connection, PEOPLE_ROLES_NAMES.add, ("Администратор",))
        DBMS.execute_query_values(connection, PEOPLE_ROLES_NAMES.add, ("Руководитель",))
        print("  Poeple` roles names added.")
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 5, 1))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 2, 2))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 3, 2))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 4, 2))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 5, 2))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 2, 4))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 3, 4))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 4, 4))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 5, 4))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 2, 5))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 3, 5))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 4, 5))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 5, 5))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 5, 6))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 3, 9))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 5, 9))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 2, 12))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 3, 12))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 4, 12))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 5, 12))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 2, 13))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 3, 13))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 4, 13))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 5, 13))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 2, 14))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 3, 14))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 4, 14))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 5, 14))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 2, 19))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 3, 19))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 4, 19))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (3, 5, 19))

        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 0, 3))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 2, 1))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 3, 1))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 4, 1))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 5, 1))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 2, 8))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 3, 8))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 4, 8))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 5, 8))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 3, 11))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 5, 11))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 2, 15))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 3, 15))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 4, 15))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 5, 15))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 2, 16))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 3, 16))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 4, 16))
        DBMS.execute_query_values(connection, ROLE_RIGHTS.add, (4, 5, 16))
        print("  Roles` rights added.")
        DBMS.execute_query_values(connection, DAYS.add, ("Понедельник",))
        DBMS.execute_query_values(connection, DAYS.add, ("Вторник",))
        DBMS.execute_query_values(connection, DAYS.add, ("Среда",))
        DBMS.execute_query_values(connection, DAYS.add, ("Четверг",))
        DBMS.execute_query_values(connection, DAYS.add, ("Пятница",))
        DBMS.execute_query_values(connection, DAYS.add, ("Суббота",))
        DBMS.execute_query_values(connection, DAYS.add, ("Воскресенье",))
        print("  Days added.")
        DBMS.execute_query_values(connection, LESSONS_TYPES.add, ("WeDo",))
        DBMS.execute_query_values(connection, LESSONS_TYPES.add, ("Python",))
        DBMS.execute_query_values(connection, LESSONS_TYPES.add, ("3D",))
        DBMS.execute_query_values(connection, LESSONS_TYPES.add, ("Game Dev",))
        DBMS.execute_query_values(connection, LESSONS_TYPES.add, ("Scratch",))
        print("  Lessons` types added.")
        DBMS.execute_query_values(connection, PLACES.add, ("Магиструм",))
        DBMS.execute_query_values(connection, PLACES.add, ("Полщадка 1",))
        DBMS.execute_query_values(connection, PLACES.add, ("Площадка 2",))
        DBMS.execute_query_values(connection, PLACES.add, ("Площадка 3",))
        DBMS.execute_query_values(connection, PLACES.add, ("Площадка 4",))
        print("  Places added.")
        DBMS.execute_query_values(connection, PEOPLE_STATES_NAMES.add, ("Будет",))
        DBMS.execute_query_values(connection, PEOPLE_STATES_NAMES.add, ("Не будет",))
        print("  People` states names added.")
        lastnames = ["Попов", "Васюков", "Петров", "Каверин"]
        names = ["Иван", "Алексий", "Тимовей", "Дмитрий", "Сергей", "Максим", "Михаил"]
        patronymics = ["Михайлович", "Максимович", "Сергеевич", "Дмитриевич", "Алексеевич", "Иванович", "Тимофеевич"]
        for i in range(25):
            DBMS.execute_query_values(connection, PEOPLE.add, (choice(lastnames), choice(names), choice(patronymics), randint(int(1e8), int(1e10)-1)))
            DBMS.execute_query_values(connection, PEOPLE_STATES.add, (i+1, randint(1, 2)))
            DBMS.execute_query_values(connection, PEOPLE_ROLES.add, (i+1, 2))
        # DBMS.execute_query_values(connection, PEOPLE_STATES.add, (20, 1))
        # DBMS.execute_query_values(connection, PEOPLE_STATES.add, (20, 0))
        # DBMS.execute_query_values(connection, PEOPLE_ROLES.add, (20, 2))
        DBMS.execute_query_values(connection, PEOPLE.add, ("Иван", "Иван", "Иван", 123456789))
        DBMS.execute_query_values(connection, PEOPLE_ROLES.add, (26, 3))
        DBMS.execute_query_values(connection, PEOPLE.add, ("Максим", "Максим", "Максим", 987654321))
        DBMS.execute_query_values(connection, PEOPLE_ROLES.add, (27, 4))
        print("  People added.")
        for i in range(1, 8):
            for j in range(20):
                a = randint(36000, 86400-10800)
                b = a + choice((3600, 2400, 5400))
                DBMS.execute_query_values(connection, SCHEDULE_STATIC.add, (randint(1, 5), randint(1, 25), randint(1, 5), i, a, b))
        print("  Lessons added.")
        for i in range(randint(1, 10)):
            a = randint(4, 12)
            b = randint(1, 18)
            DBMS.execute_query_values(connection, BREAKS.add, (randint(1, 5), 2025, a, b, 2025, a, b + 10))
        DBMS.execute_query_values(connection, BREAKS.add, (3, 2025, 4, 1, 2025, 5, 1))
        print("  Breaks added.")
        for i in range(randint(50, 100)):
            a = randint(4, 12)
            b = randint(1, 28)
            DBMS.execute_query_values(connection, CHANGES.add, (randint(1, 140), randint(1, 25), 2025, a, b, "qwe"))
        DBMS.execute_query_values(connection, CHANGES.add, (88, 10, 2025, 4, 11, "qwe"))
        print("  Changes added.")

    recreate()
    makeBasic()
    # teachers()
    print("Successfully (or not) done all work!")
