# 24. Дана строка `S` с повторяющимися буквами. Переставить буквы таким образом, чтобы одинаковые буквы не стояли рядом.
#
#     *Примечание:* строка содержит только строчные латинские буквы и может иметь множество решений. Верните любое из них.


def split_adj(s):
    s = list(s)
    cnt = {}
    for c in s:
        if c not in cnt:
            cnt[c] = 0
        cnt[c] += 1
    res = ''
    while cnt:
        keys = list(cnt.keys())
        if len(keys) == 1 and (cnt[keys[0]] > 1 or res and res[-1] == keys[0]):
            raise ValueError('невозможно')
        for k in keys:
            if not cnt[k]:
                del cnt[k]
            else:
                res += k
                cnt[k] -= 1
    return res

print(split_adj('aabbcc'))
# print(split_adj('aabbbaaa'))