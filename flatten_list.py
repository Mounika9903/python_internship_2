def flatten(lst):
    result = []
    for i in lst:
        print("Instance from 1",isinstance(i, list))
        if isinstance(i, list):
            result.extend(flatten(i))
            print("value of result ",result.extend(flatten(i)))
        else:
            result.append(i)
    return result

print(flatten([[1, 2, [3]], 4, 5]))