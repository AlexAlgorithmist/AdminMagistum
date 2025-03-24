from typing import Any
import tables_control
from SomeClasses import ERROR, WARNING, ACTIONS, TABLES, GOOD
from datetime import datetime


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

    actions = get.action_abbreviations()
    if (action,) not in actions:
        return [("E"+ERROR.UNKNOWN_ACTION, [])]
    del actions
    tables = get.table_abbreviations()
    if (table,) not in tables:
        return [("E"+ERROR.UNKNOWN_TABLE, [])]
    del tables

    if tg_id == 0:
        person = get.person_data(person_id)
        if type(person) == list:
            return [("E"+ERROR.NOT_FOUND, [])]
        if type(person) != tuple:
            return [("E" + ERROR.SQL, [str(person)])]
    elif person_id == 0:
        person = get.person_data_by_tg_id(tg_id)
        if type(person) == list:
            return [("E"+ERROR.NOT_FOUND, [])]
        elif type(person) != tuple:
            return [("E" + ERROR.SQL, [str(person)])]
        person_id = person[0]
    role = get.role(person_id)
    if type(role) != int:
        return [("E" + ERROR.SQL, [str(role), ERROR.ROLE_NOT_FOUND])]
    rights = get.rights_by_role(role)
    # print(rights)
    if type(rights) != list:
        return [("E" + ERROR.SQL, [str(rights), ERROR.RIGHTS_NOT_FOUND])]
    new_rights = get.person_rights(person_id)
    if type(new_rights) == list:
        rights = rights + new_rights
    while rights:
        act, tab = rights.pop(0)
        if act == 0:
            new_rights = get.rights_by_role(tab)
            if type(new_rights) != list:
                continue
            rights = rights + new_rights
            continue
        act_ab = get.action_abbreviation_by_id(act)
        tab_ab = get.table_abbreviation_by_id(tab)
        if act_ab == action and tab_ab == table:
            break
    else:
        return [("E"+ERROR.NO_RIGHTS, [])]
    if action == ACTIONS.CREATE:
        return preform.create(table, *args)
    elif action == ACTIONS.ADD:
        return preform.add(table, role, person_id, *args)
    elif action == ACTIONS.CHANGE:
        return preform.change(table, *args)
    elif action == ACTIONS.DELETE:
        return preform.delete(table, *args)
    elif action == ACTIONS.VEIW:
        return preform.view(table, *args)
    elif action == ACTIONS.DROP:
        return preform.drop(table, *args)


class preform:
    @staticmethod
    def create(table: str, *args) -> Any:
        """
        Performs some create function.
        :param table: table.
        :param args: any args, needed to create a table.
        :return: nothing or an error.
        """
        pass

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
        if table == TABLES.SCHEDULE_STATIC:
            length = len(args)
            if length != 6:
                return [("E"+ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            return add.lesson_static(*args)
        elif table == TABLES.SCHEDULE_LOCAL:
            length = len(args)
            if length != 6:
                return [("E"+ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            return add.lesson_local(*args)
        elif table == TABLES.LESSON_TYPES:
            length = len(args)
            if length != 1:
                return [("E"+ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            return add.lesson_type(*args)
        elif table == TABLES.BREAKS:
            length = len(args)
            if length != 7:
                return [("E"+ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            return add.break_place(*args)
        elif table == TABLES.CHANGES:
            length = len(args)
            if length != 6:
                return [("E"+ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            return add.change(*args)
        elif table == TABLES.PLACES:
            length = len(args)
            if length != 1:
                return [("E"+ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            return add.place(*args)
        elif table == TABLES.PEOPLE:
            length = len(args)
            if length != 4:
                return [("E"+ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            error = add.person(*args)
            if error[0][0][0] == "E":
                return error
            count = tables_control.get.people()[-1][0]
            # print(count)
            return [add.person_state(count, 2)[0], add.person_role(count, 1)[0]]
        elif table == TABLES.PEOPLE_RIGHTS:
            length = len(args)
            if length != 3:
                return [("E"+ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            rights = get.rights_by_role(role)
            if type(rights) != list:
                return [("E" + ERROR.SQL, [str(rights), ERROR.RIGHTS_NOT_FOUND])]
            new_rights = get.person_rights(person_id)
            if type(new_rights) == list:
                rights = rights + new_rights
            while rights:
                act, tab = rights.pop(0)
                if act == 0:
                    new_rights = get.rights_by_role(tab)
                    if type(new_rights) == list:
                        rights = rights + new_rights
                    continue
                # print(act, tab, args, act_ab == args[1] and tab_ab == args[2])
                # act_ab = get.action_abbreviation_by_id(act)
                # tab_ab = get.table_abbreviation_by_id(tab)
                if act == args[1] and tab == args[2]:
                    break
            else:
                return [("E"+ERROR.NO_RIGHTS, [])]
            return add.person_right(*args)
        elif table == TABLES.ROLE_RIGHTS:
            length = len(args)
            if length != 3:
                return [("E"+ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            rights = get.rights_by_role(role)
            if type(rights) != list:
                return [("E" + ERROR.SQL, [str(rights), ERROR.RIGHTS_NOT_FOUND])]
            new_rights = get.person_rights(person_id)
            if type(new_rights) == list:
                rights = rights + new_rights
            while rights:
                act, tab = rights.pop(0)
                if act == 0:
                    new_rights = get.rights_by_role(tab)
                    if type(new_rights) == list:
                        rights = rights + new_rights
                    continue
                if act == args[1] and tab == args[2]:
                    break
            else:
                return [("E"+ERROR.NO_RIGHTS, [])]
            return add.role_right(*args)
        elif table == TABLES.USERNAME_TG:
            length = len(args)
            if length != 2:
                return [("E"+ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            return add.username_tg(*args)

    @staticmethod
    def change(table: str, *args) -> Any:
        """
        Changing something in a some table.
        :param table: table in wich will be changed.
        :param args: any args, needed to charge in a table.
        :return: nothing or an error.
        """
        pass

    @staticmethod
    def delete(table: str, *args) -> Any:
        """
        Deleting something in a some table.
        :param table: table in wich will be added to.
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
        if table == TABLES.SCHEDULE_STATIC:
            length = len(args)
            if length != 4:
                return [("E" + ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            if args[0] == 1 and args[1] == 0:
                return get.by_day_static(args[2])
            elif args[0] == 0 and args[1] == 1:
                return get.by_person_static(args[3])
            elif args[0] == 1 and args[1] == 1:
                return get.by_day_and_person_static(args[2], args[3])
            return [("E" + ERROR.INCORRECT_ARGUMENTS, [length])]
        elif table == TABLES.SCHEDULE_LOCAL:
            length = len(args)
            if length != 4:
                return [("E" + ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            if args[0] == 1 and args[1] == 0:
                return get.by_day_local(args[2])
            elif args[0] == 0 and args[1] == 1:
                return get.by_person_local(args[3])
            elif args[0] == 1 and args[1] == 1:
                return get.by_day_and_person_local(args[2], args[3])
            return [("E" + ERROR.INCORRECT_ARGUMENTS, [length])]
        elif table == TABLES.LESSON_TYPES:
            length = len(args)
            if length != 1:
                return [("E" + ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            return get.lesson_type(*args)
        elif table == TABLES.BREAKS:
            length = len(args)
            if length != 2:
                return [("E" + ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            if args[0] == 0:
                return get.all_breaks()
            elif args[0] == 1:
                return get.break_by_id(args[1])
            elif args[0] == 0:
                return get.breaks_by_place(args[1])
            return [("E" + ERROR.INCORRECT_ARGUMENTS, [length])]
        elif table == TABLES.CHANGES:
            length = len(args)
            if length != 2:
                return [("E" + ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            if args[0] == 0:
                return get.all_changes()
            elif args[0] == 1:
                return get.change_by_lesson(args[1])
            elif args[0] == 2:
                return get.changes_by_changer(args[1])
            return [("E" + ERROR.INCORRECT_ARGUMENTS, [length])]
        elif table == TABLES.PLACES:
            length = len(args)
            if length != 1:
                return [("E" + ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            return add.place(*args)
        elif table == TABLES.PEOPLE:
            length = len(args)
            if length != 4:
                return [("E" + ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            error = add.person(*args)
            if error[0][0][0] == "E":
                return error
            count = tables_control.get.people()[-1][0]
            # print(count)
            return [add.person_state(count, 2)[0], add.person_role(count, 1)[0]]
        elif table == TABLES.PEOPLE_RIGHTS:
            length = len(args)
            if length != 3:
                return [("E" + ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            rights = get.rights_by_role(role)
            if type(rights) != list:
                return [("E" + ERROR.SQL, [str(rights), ERROR.RIGHTS_NOT_FOUND])]
            new_rights = get.person_rights(person_id)
            if type(new_rights) == list:
                rights = rights + new_rights
            while rights:
                act, tab = rights.pop(0)
                if act == 0:
                    new_rights = get.rights_by_role(tab)
                    if type(new_rights) == list:
                        rights = rights + new_rights
                    continue
                # print(act, tab, args, act_ab == args[1] and tab_ab == args[2])
                # act_ab = get.action_abbreviation_by_id(act)
                # tab_ab = get.table_abbreviation_by_id(tab)
                if act == args[1] and tab == args[2]:
                    break
            else:
                return [("E" + ERROR.NO_RIGHTS, [])]
            return add.person_right(*args)
        elif table == TABLES.ROLE_RIGHTS:
            length = len(args)
            if length != 3:
                return [("E" + ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            rights = get.rights_by_role(role)
            if type(rights) != list:
                return [("E" + ERROR.SQL, [str(rights), ERROR.RIGHTS_NOT_FOUND])]
            new_rights = get.person_rights(person_id)
            if type(new_rights) == list:
                rights = rights + new_rights
            while rights:
                act, tab = rights.pop(0)
                if act == 0:
                    new_rights = get.rights_by_role(tab)
                    if type(new_rights) == list:
                        rights = rights + new_rights
                    continue
                if act == args[1] and tab == args[2]:
                    break
            else:
                return [("E" + ERROR.NO_RIGHTS, [])]
            return add.role_right(*args)
        elif table == TABLES.USERNAME_TG:
            length = len(args)
            if length != 2:
                return [("E" + ERROR.INCORRECT_AMOUNT_OF_ARGUMENTS, [length])]
            return add.username_tg(*args)

    @staticmethod
    def drop(table: str, *args) -> Any:
        """
        Drop some table.
        :param table: table wich will be dropped.
        :param args: any args, needed to drop a table.
        :return: nothing or an error.
        """
        pass


def checkTeacher(timeTable: list[tuple[int, int, int, int]]) -> list[tuple[str, list[Any]]]:
    """
    Check, if the teacher`s timetable correct. Also gives warnings. Do not check the teacher`s absents.
    :param timeTable: [(lesson_id, place, time_begin, time_end), ...]
    :return: [(ErrorCode | WarningCode, [info, info, ...]), ...]
    """
    lessons = len(timeTable)
    res = []
    for i in range(lessons):
        for j in range(i + 1, lessons):
            if timeTable[j][2] < timeTable[i][2] < timeTable[j][3] or timeTable[j][2] < timeTable[i][3] < timeTable[j][3]:
                res.append(("E"+ERROR.INTERSEPTION, [timeTable[i][0], timeTable[j][0]]))
            if timeTable[j][1] != timeTable[i][1]:
                res.append(("W"+WARNING.DIFFERENT_PLACES, [timeTable[i][0], timeTable[j][0]]))
    return res


def construct_day(year: int, month: int, day: int) -> list[tuple[int, int, int, int, int, int, int]]:
    """
    Makes a timetabe to some day in the future, according to known breaks and changes.
    :param year: year, when the day will be constructed.
    :param month: month, when the day will be constructed.
    :param day: day, when the day will be constructed.
    :return: [(lesson_id, place, person, type, time_begin, time_end), ...],
             a timetable, as it would be on that day.
    """
    constructed_day = []
    now = datetime.now()
    then = datetime(year, month, day)
    weekDay = then.weekday() + 1
    breaks = get.all_breaks()
    changes = get.all_changes()
    if 0 <= (then - now).days <= 7:
        then_day = get.by_day_local(weekDay)
    elif (then - now).days > 7:
        then_day = get.by_day_static(weekDay)
    elif True:
        then_day = []
    for lesson in then_day:
        new_lesson = list(lesson)
        place = lesson[1]
        add = True
        for _break in breaks:
            if _break[0] != place:
                continue
            elif datetime(*_break[1:4]) <= then <= datetime(*_break[4:7]):
                add = False
                break
        if not add:
            continue
        # person = lesson[2]
        lesson_id = lesson[0]
        for change in changes:
            if change[0] != lesson_id:
                continue
            # print(change, *change[2:5])
            # print(person, year == change[2], month == change[3], day == change[4])
            if year == change[2] and month == change[3] and day == change[4]:
                # print(new_lesson[2], change[1])
                new_lesson[2] = change[1]
                # print(new_lesson[2], change[1])
                break
        constructed_day.append(tuple(new_lesson))
    return constructed_day


def wrapper(func):
    def handler(*args, **kwargs) -> list[tuple[str, list[Any]]]:
        error = func(*args, **kwargs)
        if error is not None:
            return [("E"+ERROR.SQL, [str(error)])]
        return [("G"+GOOD.EVERYTHING_IS_GOOD, [])]
    return handler


class add:
    @staticmethod
    @wrapper
    def lesson_static(place: int, teacher: int, type_lesson: int, day: int, time_begin: int, time_end: int) -> Any | None:
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
        return tables_control.add.lesson_static(place, teacher, type_lesson, day, time_begin, time_end)

    @staticmethod
    @wrapper
    def lesson_local(place: int, teacher: int, type_lesson: int, day: int, time_begin: int, time_end: int) -> Any | None:
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
        return tables_control.add.lesson_local(place, teacher, type_lesson, day, time_begin, time_end)

    @staticmethod
    @wrapper
    def lesson_type(name: str) -> Any | None:
        """
        Just adds a lesson type.
        :param name: name of type.
        :return: None or an error.
        """
        return tables_control.add.lesson_type(name)

    @staticmethod
    @wrapper
    def place(name: str) -> Any | None:
        """
        Just adds a place.
        :param name: name of a place.
        :return: None or an error.
        """
        return tables_control.add.place(name)

    @staticmethod
    @wrapper
    def break_place(place: int, year_from: int, month_from: int, day_from: int, year_to: int, month_to: int, day_to: int) -> Any | None:
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
        return tables_control.add.break_place(place, year_from, month_from, day_from, year_to, month_to, day_to)

    @staticmethod
    @wrapper
    def change(place: int, changer: int, year: int, month: int, day: int, comment: str) -> Any | None:
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
        return tables_control.add.change(place, changer, year, month, day, comment)

    @staticmethod
    @wrapper
    def person(name: str, surname: str, patronymic: str, tg_id: int) -> Any | None:
        """
        Just adds a person to a database.
        :param name: name of person.
        :param surname: surname  of person.
        :param patronymic: patronymic of person.
        :param tg_id: id in tg of person.
        :return: None or an error.
        """
        return tables_control.add.person(name, surname, patronymic, tg_id)

    @staticmethod
    @wrapper
    def person_state(person_id: int, state: int) -> Any | None:
        """
        Adds a state to a person.
        :param person_id: id of person.
        :param state: state of person.
        :return: None or an error.
        """
        return tables_control.add.person_state(person_id, state)

    @staticmethod
    @wrapper
    def person_role(person_id: int, role: int) -> Any | None:
        """
        Adds a role to a person.
        :param person_id: id of person.
        :param role: role of person.
        :return: None or an error
        """
        return tables_control.add.person_role(person_id, role)

    @staticmethod
    @wrapper
    def username_tg(tg_id: int, username: int) -> Any | None:
        """
        Adds a role to a person.
        :param tg_id: id of person.
        :param username: rusername intg of person.
        :return: None or an error
        """
        return tables_control.add.username_tg(tg_id, username)

    @staticmethod
    @wrapper
    def person_right(person_id: int, action: int, table: int) -> Any | None:
        """
        Adds some right to a person
        :param person_id: id of person.
        :param action:
        :param table:
        :return: None or an error.
        """
        return tables_control.add.person_right(person_id, action, table)

    @staticmethod
    @wrapper
    def role_right(role: int, action: int, table: int) -> Any | None:
        """
        Adds some right to a role
        :param role: id of a role.
        :param action:
        :param table:
        :return: None or an error.
        """
        return tables_control.add.role_right(role, action, table)


class get:
    @staticmethod
    def by_day_static(day: int) -> list[tuple[int, int, int, int, int, int]]:
        return tables_control.get.by_day_static(day)

    @staticmethod
    def by_person_static(person: int) -> list[tuple[int, int, int, int, int, int]]:
        return tables_control.get.by_person_static(person)

    @staticmethod
    def by_day_and_person_static(person: int, day: int) -> list[tuple[int, int, int, int, int]]:
        return tables_control.get.by_day_and_person_static(person, day)

    @staticmethod
    def by_day_local(day: int) -> list[tuple[int, int, int, int, int, int]]:
        return tables_control.get.by_day_local(day)

    @staticmethod
    def by_person_local(person: int) -> list[tuple[int, int, int, int, int, int]]:
        return tables_control.get.by_person_local(person)

    @staticmethod
    def by_day_and_person_local(person: int, day: int) -> list[tuple[int, int, int, int, int]]:
        return tables_control.get.by_day_and_person_local(person, day)

    @staticmethod
    def lesson_type(index: int) -> str:
        return tables_control.get.lesson_type(index)

    @staticmethod
    def break_by_id(index: int) -> tuple[int, int, int, int, int, int, int]:
        return tables_control.get.break_by_id(index)

    @staticmethod
    def breaks_by_place(place: int) -> list[tuple[int, int, int, int, int, int]]:
        return tables_control.get.breaks_by_place(place)

    @staticmethod
    def change_by_lesson(lesson: int) -> tuple[int, int, int, int, str]:
        return tables_control.get.change_by_lesson(lesson)

    @staticmethod
    def changes_by_changer(changer: int) -> list[tuple[int, int, int, int, int, int]]:
        return tables_control.get.breaks_by_place(changer)

    @staticmethod
    def person_data(person_id: int) -> tuple[str, str, str, int]:
        """
        Gives a data of a person by his id.
        :rtype: tuple[str, str, str, int]
        :param person_id: id of a person.
        :return: (surname, name, patronymic, tg_id).
        """
        return tables_control.get.person_by_id(person_id)

    @staticmethod
    def person_data_by_tg_id(person_tg_id: int) -> tuple[int, str, str, str]:
        """
        Gives a data of a person by his tg id.
        :rtype: tuple[int, str, str, str]
        :param person_tg_id: id in tg of a person.
        :return: (surname, name, patronymic, tg_id).
        """
        return tables_control.get.person_by_tg_id(person_tg_id)  # <DONE>: make that function (implicit)

    @staticmethod
    def role(person_id: int) -> int:
        """
        Gives person`s role by his id.
        :param person_id: id of a person.
        :return: person`s role.
        """
        return tables_control.get.role(person_id)

    @staticmethod
    def rights_by_role(role: int) -> list[tuple[int, int]]:
        """
        Get all rights of some role.
        :param role: role, that right will be shown.
        :return: [(action, table), ...], just rights.
        """
        return tables_control.get.rights_by_role(role)

    @staticmethod
    def action_abbreviation_by_id(action_id: int) -> str:
        """
        Gives an action abbreviation by it`s id.
        :param action_id: id of an action.
        :return: abbreviation
        """
        return tables_control.get.action_abbreviation_by_id(action_id)

    @staticmethod
    def table_abbreviation_by_id(table_id: int) -> str:
        """
        Gives a table abbreviation by it`s id.
        :param table_id: id of a table.
        :return: abbreviation
        """
        return tables_control.get.table_abbreviation_by_id(table_id)

    @staticmethod
    def action_abbreviations() -> list[tuple[str]]:
        """
        Gives all action`s abbreviations.
        :return: abbreviations
        """
        return tables_control.get.action_abbreviations()

    @staticmethod
    def table_abbreviations() -> list[tuple[str]]:
        """
        Gives all table`s abbreviations.
        :return: abbreviations
        """
        return tables_control.get.table_abbreviations()

    @staticmethod
    def person_rights(person_id: int) -> list[tuple[int, int]] | None:
        """
        Gives person`s rights (that are special apart from person`s role`s rights).
        :return: rights
        """
        return tables_control.get.person_rights(person_id)

    @staticmethod
    def all_breaks() -> list[tuple[int, int, int, int, int, int, int]] | None:
        """
        Gives all places` breaks.
        :return: breaks.
        """
        return tables_control.get.all_breaks()

    @staticmethod
    def all_changes() -> list[tuple[int, int, int, int, int, str]] | None:
        """
        Gives all changes.
        :return: changes.
        """
        return tables_control.get.all_changes()


class change:
    @staticmethod
    def surname(person_id: int, surname: str) -> None:
        """
        Changes person`s surname.
        :param person_id: id of a person.
        :param surname: new surname for a person.
        :return: no return.
        """
        tables_control.change.surname(person_id, surname)

    @staticmethod
    def name(person_id: int, name: str) -> None:
        """
        Changes person`s name.
        :param person_id: id of a person.
        :param name: new name for a person.
        :return: no return.
        """
        tables_control.change.name(person_id, name)

    @staticmethod
    def patronymic(person_id: int, patronymic: str) -> None:
        """
        Changes person`s patronymic.
        :param person_id: id of a person.
        :param patronymic: new patronymic for a person.
        :return: no return.
        """
        tables_control.change.patronymic(person_id, patronymic)

    @staticmethod
    def tg_id(person_id: int, tg_id: int) -> None:
        """
        Changes person`s tg_id. (I don`t this would ever happen.)
        :param person_id: id of a person.
        :param tg_id: new tg_id for a person.
        :return: no return.
        """
        tables_control.change.tg_id(person_id, tg_id)

    @staticmethod
    def state(person_id: int, state: int) -> None:
        """
        Changes person`s state.
        :param person_id: id of a person.
        :param state: new state for a person.
        :return: no return.
        """
        tables_control.change.state(person_id, state)


if __name__ == "__main__":
    import sys
    # import tables_control
    tables_control.setup(f"{sys.path[0]}\\database.sqlite")
    # tables_control.pprint(construct_day(2025, 9, 11))
    # print(get_teacher_data(14))
    # change_surname(14, "rty")
    # print(get_teacher_data(14))
    # change_name(14, "rty")
    # print(get_teacher_data(14))
    # change_patronymic(14, "rty")
    # print(get_teacher_data(14))
    # change_tg_id(14, 987654321)
    # print(get_teacher_data(14))
    # change_state(14, 0)
    # print(get_teacher_data(14))
    # tables_control.lock()
    print(do_action(ACTIONS.ADD, TABLES.LESSON_TYPES, 0, 27, "WeDo1"))
    print(do_action(ACTIONS.ADD, TABLES.LESSON_TYPES, 987654321, 0, "WeDo2"))
    print(do_action(ACTIONS.ADD, TABLES.LESSON_TYPES, 0, 15, "WeDo3"))
    print(do_action(ACTIONS.ADD, TABLES.BREAKS, 0, 27, 0, 2025, 4, 11, 2025, 5, 11))
    print(do_action(ACTIONS.ADD, TABLES.CHANGES, 0, 27, 0, 1, 2025, 4, 11, "da"))
    print(do_action(ACTIONS.ADD, TABLES.PLACES, 0, 27, "da place"))
    print(do_action(ACTIONS.ADD, TABLES.PEOPLE, 0, 27, "da", "dada", "dadada", 0))
    print(do_action(ACTIONS.ADD, TABLES.PEOPLE_RIGHTS, 0, 27, 26, 5, 1))
    print(do_action(ACTIONS.ADD, TABLES.ROLE_RIGHTS, 0, 27, 3, 5, 1))
    # print(do_action(ACTIONS.ADD, TABLES.LESSON_TYPES, 0, 26, "WeDo1"))
    # tables_control.unlock()
    # exit()

    teachers = tables_control.get.people()
    # print(teachers)

    for i in range(1, 8):
        for _teacher_id in teachers:
            _day = tables_control.get.by_day_and_teacher_static(_teacher_id[0], i)
            if _day is None:
                continue
            # print(day)
            newday = []
            for j in _day:
                newday.append((j[0], j[1], j[3], j[4]))
            res = checkTeacher(newday)
            print(f"{_teacher_id[0]}: ", end="")
            tables_control.pprint(res)
