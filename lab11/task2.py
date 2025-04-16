from collections import defaultdict
def group_by(f, target_list):
    grouped = defaultdict(list)
    for item in target_list:
        key = f(item)
        grouped[key].append(item)
    return dict(grouped)