from medals_data import medals_table

def sort_key(d: dict, field: str) -> str:
    return d[field]

medals_table.sort(key=lambda x: sort_key(x, 'rank'))

print(medals_table)