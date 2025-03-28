from typing import Any


def do_ation2(action: str, table: str, tg_id: int, person_id: int, *args) -> Any:
    """
    Doing action to a table using a really strange but easy metod, acording
    to person`s and his role`s rights.
    :param action: action, that will be performed.
    :param table: what table to perform an action.
    :param tg_id: person`s id in tg.
    :param person_id: id in 'people' table
    :param args: any args, that an action need.
    :return: error, nothing or a result of preforming action.
    """


def checkRights(action: str, table: str, person_id: int) -> list[tuple[str, list[str]]]:
    """
    Chack person`s rights.
    :param action: action, performing to a table.
    :param table: table, taht will be performed an action.
    :param person_id: id of a person, who performs an action to a tabele.
    :return: standard error code.
    """


def do_action(action: str, table: str, tg_id: int, person_id: int, *args) -> Any:
    """
    Doing action to a table, acording to person`s and his role`s rights.
    :param action: action, that will be performed.
    :param table: what table to perform an action.
    :param tg_id: person`s id in tg.
    :param person_id: id in 'people' table
    :param args: any args, that an action need.
    :return: error, nothing or a result of preforming action.
    """


def checkTeacher(timeTable: list[tuple[int, int, int, int]]) -> list[tuple[str, list[Any]]]:
    """
    Check, if the teacher`s timetable correct. Also gives warnings. Do not check the teacher`s absents.
    :param timeTable: [(lesson_id, place, time_begin, time_end), ...]
    :return: [(ErrorCode | WarningCode, [info, info, ...]), ...]
    """


def construct_day(year, month, day) -> list[tuple[int, int, int, int, int, int, int]]:
    """
    Makes a timetabe to some day in the future, according to known breaks and changes.
    :param year: year, when the day will be constructed.
    :param month: month, when the day will be constructed.
    :param day: day, when the day will be constructed.
    :return: [(lesson_id, place, person, type, time_begin, time_end), ...],
             a timetable, as it would be on that day.
    """


class preform:
    @staticmethod
    def create(table: str, role: int, person_id: int, *args) -> Any:
        """
        Performs some create function.
        :param table: table.
        :param role: role of a person, performing action.
        :param person_id: id of a person.
        :param args: any args, needed to create a table.
        :return: nothing or an error.
        """

    @staticmethod
    def add(table: str, role: int, person_id: int, *args) -> Any:
        """
        Adds something to a some table.
        :param table: table wich will be added to.
        :param role: role of a person, performing action.
        :param person_id: id of a person.
        :param args: any args added to a table.
        :return: nothing or an error.
        """

    @staticmethod
    def change(table: str, role: int, person_id: int, *args) -> Any:
        """
        Changing something in a some table.
        :param table: table in wich will be changed.
        :param role: role of a person, performing action.
        :param person_id: id of a person.
        :param args: any args, needed to charge in a table.
        :return: nothing or an error.
        """
        pass

    @staticmethod
    def delete(table: str, role: int, person_id: int, *args) -> Any:
        """
        Deleting something in a some table.
        :param table: table in wich will be added to.
        :param role: role of a person, performing action.
        :param person_id: id of a person.
        :param args: any args, needed to delete in a table.
        :return: nothing or an error.
        """
        pass

    @staticmethod
    def view(table: str, role: int, person_id: int, *args) -> Any:
        """
        Gets something from a some table.
        :param table: table from wich be viewed.
        :param role: role of a person, performing action.
        :param person_id: id of a person.
        :param args: any args, needed to veiw in a table.
        :return: nothing or an error.
        """

    @staticmethod
    def drop(table: str, role: int, person_id: int, *args) -> Any:
        """
        Drop some table.
        :param table: table wich will be dropped.
        :param role: role of a person, performing action.
        :param person_id: id of a person.
        :param args: any args, needed to drop a table.
        :return: nothing or an error.
        """


def wrapper(func):
    def handler(*args, **kwargs) -> list[tuple[str, list[Any]]]: ...


class add:
    class schedule_static:
        @staticmethod
        @wrapper
        def all(place: int, teacher: int, type_lesson: int, day: int, time_begin: int, time_end: int) -> Any | None:
            """
            Adds a lesson to a static schedule.
            :param place: where lesson takes place.
            :param teacher: id of teacher, that teachs.
            :param type_lesson: id of lesson type.
            :param day: day of week, when the lesson takes place.
            :param time_begin: time, when lesson starts.
            :param time_end: time, when lesson ends.
            :return: None or an error.
            """

    class schedule_local:
        @staticmethod
        @wrapper
        def all(place: int, teacher: int, type_lesson: int, day: int, time_begin: int, time_end: int) -> Any | None:
            """
            Adds a lesson to a local schedule.
            :param place: where lesson takes place.
            :param teacher: id of teacher, that teachs.
            :param type_lesson: id of lesson type.
            :param day: day of week, when the lesson takes place.
            :param time_begin: time, when lesson starts.
            :param time_end: time, when lesson ends.
            :return: None or an error.
            """

    class lessons_types:
        @staticmethod
        @wrapper
        def all(name: str) -> Any | None:
            """
            Just adds a lesson type.
            :param name: name of type.
            :return: None or an error.
            """

    class places:
        @staticmethod
        @wrapper
        def all(name: str) -> Any | None:
            """
            Just adds a place.
            :param name: name of a place.
            :return: None or an error.
            """

    class breaks:
        @staticmethod
        @wrapper
        def all(place: int, year_from: int, month_from: int, day_from: int, year_to: int, month_to: int, day_to: int) -> Any | None:
            """
            Adds a breake to some place.
            :param place:
            :param year_from:
            :param month_from:
            :param day_from:
            :param year_to:
            :param month_to:
            :param day_to:
            :return: None or an error.
            """

    class changes:
        @staticmethod
        @wrapper
        def all(place: int, changer: int, year: int, month: int, day: int, comment: str) -> Any | None:
            """
            Add a change to some lesson.
            :param place:
            :param changer:
            :param year:
            :param month:
            :param day:
            :param comment:
            :return: None or an error.
            """

    class people:
        @staticmethod
        @wrapper
        def all(name: str, surname: str, patronymic: str, tg_id: int) -> Any | None:
            """
            Just adds a person to a database.
            :param name: name of person.
            :param surname: surname  of person.
            :param patronymic: patronymic of person.
            :param tg_id: id in tg of person.
            :return: None or an error.
            """

    class people_states:
        @staticmethod
        @wrapper
        def all(person_id: int, state: int) -> Any | None:
            """
            Adds a state to a person.
            :param person_id: id of person.
            :param state: state of person.
            :return: None or an error.
            """

    class people_roles:
        @staticmethod
        @wrapper
        def all(person_id: int, role: int) -> Any | None:
            """
            Adds a role to a person.
            :param person_id: id of person.
            :param role: role of person.
            :return: None or an error
            """

    class username_tg:
        @staticmethod
        @wrapper
        def all(tg_id: int, username: int) -> Any | None:
            """
            Adds a role to a person.
            :param tg_id: id of person.
            :param username: rusername intg of person.
            :return: None or an error
            """

    class people_rights:
        @staticmethod
        @wrapper
        def all(person_id: int, action: int, table: int) -> Any | None:
            """
            Adds some right to a person
            :param person_id: id of person.
            :param action:
            :param table:
            :return: None or an error.
            """

    class role_rights:
        @staticmethod
        @wrapper
        def all(role: int, action: int, table: int) -> Any | None:
            """
            Adds some right to a role
            :param role: id of a role.
            :param action:
            :param table:
            :return: None or an error.
            """


class get:
    class schedule_static:
        @staticmethod
        @wrapper
        def by_day(day: int) -> list[tuple[int, int, int, int, int, int]]: ...

        @staticmethod
        @wrapper
        def by_person(person: int) -> list[tuple[int, int, int, int, int, int]]: ...

        @staticmethod
        @wrapper
        def by_day_and_person(person: int, day: int) -> list[tuple[int, int, int, int, int]]: ...

    class schedule_local:
        @staticmethod
        @wrapper
        def by_day(day: int) -> list[tuple[int, int, int, int, int, int]]: ...

        @staticmethod
        @wrapper
        def by_person(person: int) -> list[tuple[int, int, int, int, int, int]]: ...

        @staticmethod
        @wrapper
        def by_day_and_person(person: int, day: int) -> list[tuple[int, int, int, int, int]]: ...

    class lessons_types:
        @staticmethod
        @wrapper
        def by_id(index: int) -> str: ...

    class breaks:
        @staticmethod
        @wrapper
        def by_id(index: int) -> tuple[int, int, int, int, int, int, int]: ...

        @staticmethod
        @wrapper
        def by_place(place: int) -> list[tuple[int, int, int, int, int, int]]:
            """
            Gives all breaks of some place at any time.
            :param place: id of a place, that got breaked.
            :return: [(year_from, month_from, day_from, year_to, month_to, day_to), ...].
            """

        @staticmethod
        @wrapper
        def all() -> list[tuple[int, int, int, int, int, int, int]] | None:
            """
            Gives all places` breaks.
            :return: breaks.
            """

    class changes:
        @staticmethod
        @wrapper
        def by_lesson(lesson: int) -> list[tuple[int, int, int, int, str]]:
            """
            Return all changes of some lesson at any time.
            :param lesson: id of a lesson, that got changed.
            :return: [(changer_id, year, month, day, comment), ...].
            """

        @staticmethod
        @wrapper
        def by_changer(changer: int) -> list[tuple[int, int, int, int, str]]:
            """
            Return all changes that person gives at any time.
            :param changer: id of person, that changes other.
            :return: [(lesson_id, year, month, day, comment), ...].
            """

        @staticmethod
        @wrapper
        def all() -> list[tuple[int, int, int, int, int, str]] | None:
            """
            Gives all changes.
            :return: changes.
            """

    class people:
        @staticmethod
        @wrapper
        def by_id(person_id: int) -> tuple[str, str, str, int]:
            """
            Gives a data of a person by his id.
            :rtype: tuple[str, str, str, int]
            :param person_id: id of a person.
            :return: (surname, name, patronymic, tg_id).
            """

        @staticmethod
        @wrapper
        def by_tg_id(person_tg_id: int) -> tuple[int, str, str, str]:
            """
            Gives a data of a person by his tg id.
            :rtype: tuple[int, str, str, str]
            :param person_tg_id: id in tg of a person.
            :return: (surname, name, patronymic, tg_id).
            """

    class people_roles:
        @staticmethod
        @wrapper
        def by_person_id(person_id: int) -> int:
            """
            Gives person`s role by his id.
            :param person_id: id of a person.
            :return: person`s role.
            """

    class role_rights:
        @staticmethod
        @wrapper
        def by_role(role: int) -> list[tuple[int, int]]:
            """
            Get all rights of some role.
            :param role: role, that right will be shown.
            :return: [(action, table), ...], just rights.
            """

    class actions:
        @staticmethod
        @wrapper
        def by_id_abbreviation(action_id: int) -> str:
            """
            Gives an action abbreviation by it`s id.
            :param action_id: id of an action.
            :return: abbreviation
            """

        @staticmethod
        @wrapper
        def all_abbreviations() -> list[tuple[str]]:
            """
            Gives all action`s abbreviations.
            :return: abbreviations
            """

    class tables:
        @staticmethod
        @wrapper
        def by_id_abbreviation(table_id: int) -> str:
            """
            Gives a table abbreviation by it`s id.
            :param table_id: id of a table.
            :return: abbreviation
            """

        @staticmethod
        @wrapper
        def all_abbreviations() -> list[tuple[str]]:
            """
            Gives all table`s abbreviations.
            :return: abbreviations
            """

    class people_rights:
        @staticmethod
        @wrapper
        def by_person_id(person_id: int) -> list[tuple[int, int]] | None:
            """
            Gives person`s rights (that are special apart from person`s role`s rights).
            :return: rights
            """


class change:
    class people:
        @staticmethod
        @wrapper
        def surname(person_id: int, surname: str) -> None:
            """
            Changes person`s surname.
            :param person_id: id of a person.
            :param surname: new surname for a person.
            :return: no return.
            """

        @staticmethod
        @wrapper
        def name(person_id: int, name: str) -> None:
            """
            Changes person`s name.
            :param person_id: id of a person.
            :param name: new name for a person.
            :return: no return.
            """

        @staticmethod
        @wrapper
        def patronymic(person_id: int, patronymic: str) -> None:
            """
            Changes person`s patronymic.
            :param person_id: id of a person.
            :param patronymic: new patronymic for a person.
            :return: no return.
            """

        @staticmethod
        @wrapper
        def tg_id(person_id: int, tg_id: int) -> None:
            """
            Changes person`s tg_id. (I don`t this would ever happen.)
            :param person_id: id of a person.
            :param tg_id: new tg_id for a person.
            :return: no return.
            """

    class people_states:
        @staticmethod
        @wrapper
        def by_person_id(person_id: int, state: int) -> None:
            """
            Changes person`s state.
            :param person_id: id of a person.
            :param state: new state for a person.
            :return: no return.
            """
