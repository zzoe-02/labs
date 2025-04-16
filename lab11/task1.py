def zipmap(key_list, value_list, override=False):
    if len(key_list) > len(value_list):
        value_list += [None] * (len(key_list) - len(value_list))
    result = {}
    for key, value in zip(key_list, value_list):
        if override or key not in result:
            result[key] = value
    return result

