
def mean(num_list):
    if len(num_list) > 0:
        if isinstance(num_list[0], complex):
            return NotImplemented
    try:
        return sum(num_list) / len(num_list)
    except ZeroDivisionError:
        return 0
    except TypeError as detail:
        msg = "The mean of a non-numeric list is undefined."
        raise TypeError(detail.__str__() + '\n' + msg)
    except OverflowError as error:
        return 0
