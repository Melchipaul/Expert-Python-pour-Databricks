from medals_data import medals_table


def sort_key(d: dict, field: str) -> str:
    return d[field]

options = {
    'C': ('country',),
    'G': ('gold medals',),
    'S': ('silver medals',),
    'B': ('bronze medals',),
    'R': ('rank',),
}

while True:
    for option, (description, *_) in options.items():
        print(f'{option}: Sort by {description}')
    print('Invalid choices will exit.')

    choice = input('Please select an option: ').upper()

    if choice == 'C':
        medals_table.sort(key=lambda x: sort_key(x, 'country'))
    elif choice == 'G':
        medals_table.sort(key=lambda x: sort_key(x, 'gold'), reverse=True)
    elif choice == 'S':
        medals_table.sort(key=lambda x: sort_key(x, 'silver'), reverse=True)
    elif choice == 'B':
        medals_table.sort(key=lambda x: sort_key(x, 'bronze'), reverse=True)
    elif choice == 'R':
        medals_table.sort(key=lambda x: sort_key(x, 'rank'))
    else:
        break

    print(f'Sorted by {options[choice][0]}')
    for row in range(10):
        print(medals_table[row])