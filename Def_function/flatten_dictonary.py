def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                items.extend(flatten_dict(item, f"{new_key}_{i}", sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

d={
    "a":1,
    "b":{
            "c":2,
            "d":3,
            "e":{
                    "f":4,
                    "g":5
                },
            "h":6
        },
    "i":7
}

flatten_dict = flatten_dict(d)
print(flatten_dict)
