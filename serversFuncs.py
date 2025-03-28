from typing import Any
import tables_control
from SomeClasses import ERROR, WARNING, ACTIONS, TABLES, GOOD
from datetime import datetime


def do_ation2(action, table, tg_id, person_id, *args):
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
    error = checkRights(action, table, person_id)
    if error[0][0][0] != "G":
        return error



def checkRights(action, table, person_id):
    role = get.role(person_id)
    if type(role) != int:
        return [("E" + ERROR.SQL, [str(role), ERROR.ROLE_NOT_FOUND])]
    rights = get.rights_by_role(role)
    if type(rights) != list:
        return [("E" + ERROR.SQL, [str(rights), ERROR.RIGHTS_NOT_FOUND])]
    new_rights = get.person_rights(person_id)
    print(new_rights)
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
    return [("G"+GOOD.EVERYTHING_IS_GOOD, [])]


def do_action(action, table, tg_id, person_id, *args):
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
    error = checkRights(action, table, person_id)
    if error[0][0][0] != "G":
        return error
    role = get.role(person_id)
    if action == ACTIONS.CREATE:
        return preform.create(table, *args)
    elif action == ACTIONS.ADD:
        return preform.add(table, role, person_id, *args)
    elif action == ACTIONS.CHANGE:
        return preform.change(table, *args)
    elif action == ACTIONS.DELETE:
        return preform.delete(table, *args)
    elif action == ACTIONS.VEIW:
        return preform.view(table, role, person_id, *args)
    elif action == ACTIONS.DROP:
        return preform.drop(table, *args)


class preform:
    @staticmethod
    def create(table, *args):
        pass

    @staticmethod
    def add(table, role, person_id, *args):
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
    def change(table, *args):
        pass

    @staticmethod
    def delete(table, *args):
        pass

    @staticmethod
    def view(table, role, person_id, *args):
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
            elif args[0] == 2:
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
    def drop(table, *args):
        pass


def checkTeacher(timeTable):
    lessons = len(timeTable)
    res = []
    for i in range(lessons):
        for j in range(i + 1, lessons):
            if timeTable[j][2] < timeTable[i][2] < timeTable[j][3] or timeTable[j][2] < timeTable[i][3] < timeTable[j][3]:
                res.append(("E"+ERROR.INTERSEPTION, [timeTable[i][0], timeTable[j][0]]))
            if timeTable[j][1] != timeTable[i][1]:
                res.append(("W"+WARNING.DIFFERENT_PLACES, [timeTable[i][0], timeTable[j][0]]))
    return res


def construct_day(year, month, day):
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
        if type(error) not in [list, tuple, int, str] and error is not None:
            return [("E"+ERROR.SQL, [str(error)])]
        if error is None:
            return [("G"+GOOD.EVERYTHING_IS_GOOD, [])]
        return error
    return handler


class add:
    @staticmethod
    @wrapper
    def lesson_static(place, teacher, type_lesson, day, time_begin, time_end):
        return tables_control.add.lesson_static(place, teacher, type_lesson, day, time_begin, time_end)

    @staticmethod
    @wrapper
    def lesson_local(place, teacher, type_lesson, day, time_begin, time_end):
        return tables_control.add.lesson_local(place, teacher, type_lesson, day, time_begin, time_end)

    @staticmethod
    @wrapper
    def lesson_type(name):
        return tables_control.add.lesson_type(name)

    @staticmethod
    @wrapper
    def place(name):
        return tables_control.add.place(name)

    @staticmethod
    @wrapper
    def break_place(place, year_from, month_from, day_from, year_to, month_to, day_to):
        return tables_control.add.break_place(place, year_from, month_from, day_from, year_to, month_to, day_to)

    @staticmethod
    @wrapper
    def change(place, changer, year, month, day, comment):
        return tables_control.add.change(place, changer, year, month, day, comment)

    @staticmethod
    @wrapper
    def person(name, surname, patronymic, tg_id):
        return tables_control.add.person(name, surname, patronymic, tg_id)

    @staticmethod
    @wrapper
    def person_state(person_id, state):
        return tables_control.add.person_state(person_id, state)

    @staticmethod
    @wrapper
    def person_role(person_id, role):
        return tables_control.add.person_role(person_id, role)

    @staticmethod
    @wrapper
    def username_tg(tg_id, username):
        return tables_control.add.username_tg(tg_id, username)

    @staticmethod
    @wrapper
    def person_right(person_id, action, table):
        return tables_control.add.person_right(person_id, action, table)

    @staticmethod
    @wrapper
    def role_right(role, action, table):
        return tables_control.add.role_right(role, action, table)


class get:
    class schedule_static:
        @staticmethod
        @wrapper
        def by_day(day):
            return tables_control.get.by_day_static(day)

        @staticmethod
        @wrapper
        def by_person(person):
            return tables_control.get.by_person_static(person)

        @staticmethod
        @wrapper
        def by_day_and_person(person, day):
            return tables_control.get.by_day_and_person_static(person, day)

    class schedule_local:
        @staticmethod
        @wrapper
        def by_day(day):
            return tables_control.get.by_day_local(day)

        @staticmethod
        @wrapper
        def by_person(person):
            return tables_control.get.by_person_local(person)

        @staticmethod
        @wrapper
        def by_day_and_person(person, day):
            return tables_control.get.by_day_and_person_local(person, day)

    class lessons_types:
        @staticmethod
        @wrapper
        def by_id(index):
            return tables_control.get.lesson_type(index)

    class breaks:
        @staticmethod
        @wrapper
        def by_id(index):
            return tables_control.get.break_by_id(index)

        @staticmethod
        @wrapper
        def by_place(place):
            return tables_control.get.breaks_by_place(place)

        @staticmethod
        @wrapper
        def all():
            return tables_control.get.all_breaks()

    class changes:
        @staticmethod
        @wrapper
        def by_lesson(lesson):
            return tables_control.get.change_by_lesson(lesson)

        @staticmethod
        @wrapper
        def by_changer(changer):
            return tables_control.get.changes_by_changer(changer)

        @staticmethod
        @wrapper
        def all():
            return tables_control.get.all_changes()

    class people:
        @staticmethod
        @wrapper
        def by_id(person_id):
            return tables_control.get.person_by_id(person_id)

        @staticmethod
        @wrapper
        def by_tg_id(person_tg_id):
            return tables_control.get.person_by_tg_id(person_tg_id)

    class people_roles:
        @staticmethod
        @wrapper
        def by_person_id(person_id):
            return tables_control.get.role(person_id)

    class role_rights:
        @staticmethod
        @wrapper
        def by_role(role):
            return tables_control.get.rights_by_role(role)

    class actions:
        @staticmethod
        @wrapper
        def by_idn_abbreviation(action_id):
            return tables_control.get.action_abbreviation_by_id(action_id)

        @staticmethod
        @wrapper
        def all_abbreviations():
            return tables_control.get.action_abbreviations()

    class tables:
        @staticmethod
        @wrapper
        def by_id_abbreviation(table_id):
            return tables_control.get.table_abbreviation_by_id(table_id)

        @staticmethod
        @wrapper
        def all_abbreviations():
            return tables_control.get.table_abbreviations()

    class people_rights:
        @staticmethod
        @wrapper
        def by_person_id(person_id):
            return tables_control.get.person_rights(person_id)


class change:
    class people:
        @staticmethod
        @wrapper
        def surname(person_id, surname):
            tables_control.change.surname(person_id, surname)

        @staticmethod
        @wrapper
        def name(person_id, name):
            tables_control.change.name(person_id, name)

        @staticmethod
        @wrapper
        def patronymic(person_id, patronymic):
            tables_control.change.patronymic(person_id, patronymic)

        @staticmethod
        @wrapper
        def tg_id(person_id, tg_id):
            tables_control.change.tg_id(person_id, tg_id)

    class people_states:
        @staticmethod
        @wrapper
        def by_person_id(person_id, state):
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

    print("Now 'add':")

    print(do_action(ACTIONS.ADD, TABLES.LESSON_TYPES, 0, 27, "WeDo1"))
    print(do_action(ACTIONS.ADD, TABLES.LESSON_TYPES, 987654321, 0, "WeDo2"))
    print(do_action(ACTIONS.ADD, TABLES.LESSON_TYPES, 0, 15, "WeDo3"))
    print(do_action(ACTIONS.ADD, TABLES.BREAKS, 0, 27, 0, 2025, 4, 11, 2025, 5, 11))
    print(do_action(ACTIONS.ADD, TABLES.CHANGES, 0, 27, 0, 1, 2025, 4, 11, "da"))
    print(do_action(ACTIONS.ADD, TABLES.PLACES, 0, 27, "da place"))
    print(do_action(ACTIONS.ADD, TABLES.PEOPLE, 0, 27, "da", "dada", "dadada", 0))
    print(do_action(ACTIONS.ADD, TABLES.PEOPLE_RIGHTS, 0, 27, 26, 5, 1))
    print(do_action(ACTIONS.ADD, TABLES.ROLE_RIGHTS, 0, 27, 3, 5, 1))

    print("Now 'veiw':")

    print(do_action(ACTIONS.VEIW, TABLES.LESSON_TYPES, 0, 27, 86))
    print(do_action(ACTIONS.VEIW, TABLES.LESSON_TYPES, 987654321, 0, 7))
    print(do_action(ACTIONS.VEIW, TABLES.LESSON_TYPES, 0, 15, 3))
    print(do_action(ACTIONS.VEIW, TABLES.BREAKS, 0, 27, 0, 0))
    print(do_action(ACTIONS.VEIW, TABLES.BREAKS, 0, 27, 1, 3))
    print(do_action(ACTIONS.VEIW, TABLES.BREAKS, 0, 27, 2, 3))
    print(do_action(ACTIONS.VEIW, TABLES.CHANGES, 0, 27, 0, 0))
    print(do_action(ACTIONS.VEIW, TABLES.CHANGES, 0, 27, 1, 60))
    print(do_action(ACTIONS.VEIW, TABLES.CHANGES, 0, 27, 2, 19))
    # print(do_action(ACTIONS.VEIW, TABLES.PLACES, 0, 27, "da place"))
    # print(do_action(ACTIONS.VEIW, TABLES.PEOPLE, 0, 27, "da", "dada", "dadada", 0))
    # print(do_action(ACTIONS.VEIW, TABLES.PEOPLE_RIGHTS, 0, 27, 26, 5, 1))
    # print(do_action(ACTIONS.VEIW, TABLES.ROLE_RIGHTS, 0, 27, 3, 5, 1))
    # tables_control.unlock()
    exit()

    teachers = tables_control.get.people()
    # print(teachers)

    for i in range(1, 8):
        for _teacher_id in teachers:
            _day = tables_control.get.by_day_and_person_static(_teacher_id[0], i)
            if _day is None:
                continue
            # print(day)
            newday = []
            for j in _day:
                newday.append((j[0], j[1], j[3], j[4]))
            res = checkTeacher(newday)
            print(f"{_teacher_id[0]}: ", end="")
            tables_control.pprint(res)
