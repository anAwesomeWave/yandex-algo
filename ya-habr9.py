def OneEditApart(str1: str, str2: str) -> bool:
    """
    найдем 1 позицию, символы на которой различны

    сравним длины строк
    """

    def comp(ind1, ind2):
        """  возвращает 1 индексы, на которых символы не равны """
        while ind1 < len(str1) and ind2 < len(str2) and str1[ind1] == str2[ind2]:
            ind1 += 1
            ind2 += 1
        return ind1, ind2

    first_ind, sec_ind = comp(0, 0)

    first_len = len(str1) - first_ind - 1
    sec_len = len(str2) - first_ind - 1

    if first_len == -1 or sec_len == -1:
        return abs(len(str1) - len(str2)) < 2

    if first_len > sec_len:
        first_ind += 1
    elif first_len < sec_len:
        sec_ind += 1
    else:
        first_ind += 1
        sec_ind += 1

    first_ind, sec_ind = comp(first_ind, sec_ind)

    return first_ind == len(str1) and sec_ind == len(str2)


assert OneEditApart("cat", "dog") is False
assert OneEditApart("cat", "cats") is True
assert OneEditApart("cat", "catss") is False
assert OneEditApart("cat", "cut") is True
assert OneEditApart("cat", "cast") is True
assert OneEditApart("cat", "at") is True
assert OneEditApart("cat", "acts") is False
assert OneEditApart("", "") is True
