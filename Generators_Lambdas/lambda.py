tickets = [
    {"id": 1, "title": "Bug login", "status": "active", "priority": 3, "assignee": "Alice"},
    {"id": 2, "title": "Feature export", "status": "closed", "priority": 1, "assignee": "Bob"},
    {"id": 3, "title": "Crash homepage", "status": "active", "priority": 5, "assignee": "Alice"},
    {"id": 4, "title": "UI fix", "status": "resolved", "priority": 2, "assignee": "Carol"},
    {"id": 5, "title": "Perf issue", "status": "active", "priority": 4, "assignee": "Bob"},
]

# 1. Écris une fonction enrich_ticket(*fields)
#    → prend un ticket + une liste de champs à garder
#    → retourne un nouveau dict avec seulement ces champs
#    Exemple : enrich_ticket(tickets[0], "id", "title") 
#    → {"id": 1, "title": "Bug login"}

def enrich_ticket(ticket, *fields):
    return {field: ticket[field] for field in fields}

# 2. Écris une fonction transform(tickets, **transformations)
#    → applique une transformation par champ
#    Exemple : transform(tickets, priority=lambda p: p * 2, status=str.upper)
#    → retourne une nouvelle liste avec les champs transformés

def transform(tickets, **transformations):
    transformed = []
    for ticket in tickets:
        new_ticket = ticket.copy()
        for field, func in transformations.items():
            if field in new_ticket:
                new_ticket[field] = func(new_ticket[field])
        transformed.append(new_ticket)
    return transformed

# 3. Écris une fonction pipeline(*fonctions)
#    → prend une liste de fonctions et les applique en chaîne sur tickets
#    Exemple : pipeline(f1, f2, f3) applique f1, puis f2 sur le résultat, puis f3

def pipeline(*functions):
    def apply_pipeline(data):
        for func in functions:
            data = func(data)
        return data
    return apply_pipeline


if __name__ == "__main__":
    # Test enrich_ticket
    print(enrich_ticket(tickets[0], "id", "title"))

    # Test transform
    transformed = transform(tickets, priority=lambda p: p * 2, status=str.upper)
    print(transformed)

    # Test pipeline
    pipeline_func = pipeline(
        lambda tickets: transform(tickets, priority=lambda p: p * 2),
        lambda tickets: transform(tickets, status=str.upper)
    )
    print(pipeline_func(tickets))