def menu_is_boring_mine(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    meal = ''
    for m in meals:
        if m == meal:
            return True
        meal = m
    return False


def menu_is_boring_theirs(meals):
    # Iterate over all indices of the list, except the last one
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
