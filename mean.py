from math import sqrt

def mean(num_list):
    if len(num_list) > 0:
        if isinstance(num_list[0], complex):
            return NotImplemented
    try:
        return float(sum(num_list)) / len(num_list)
    except ZeroDivisionError:
        return 0
    except TypeError as detail:
        msg = "The mean of a non-numeric list is undefined."
        raise TypeError(detail.__str__() + '\n' + msg)
    except OverflowError:
        return 0

# Standard deviation

def std(nums):
    try:
        if len(nums) == 0:
            return 0.0
        m = mean(nums)
        return sqrt(sum((x - m) ** 2 for x in nums) / len(nums))
    except TypeError as error:
        msg = "The standard deviation os a non-numeric list is undefined."
        raise TypeError(error.__str__() + '\n' + msg)
    except OverflowError:
        return 0
