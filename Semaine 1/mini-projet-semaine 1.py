tickets = [
    {"id": 1, "title": "Bug login", "status": "active", "priority": 3},
    {"id": 2, "title": "Feature export", "status": "closed", "priority": 1},
    {"id": 3, "title": "Crash homepage", "status": "active", "priority": 5},
    {"id": 4, "title": "UI fix", "status": "resolved", "priority": 2},
    {"id": 5, "title": "Perf issue", "status": "active", "priority": 4},
]

# 1. Écris une fonction get_index(tickets) 
#    → retourne {id: title} pour tous les tickets

# 2. Écris une fonction filter_by_status(tickets, status)
#    → retourne la liste des tickets filtrés par statut

# 3. Écris une fonction group_by_status(tickets)
#    → retourne {status: [titres]}

# 4. Écris une fonction summarize(tickets)
#    → retourne un dict avec :
#       - "total": nombre de tickets
#       - "par_statut": {status: count}
#       - "priorite_max": le titre du ticket avec la priorité la plus haute

def get_index(tickets):
    return {ticket["id"]: ticket["title"] for ticket in tickets}

def filter_by_status(tickets, status):
    return [ticket for ticket in tickets if ticket["status"] == status]

def group_by_status(tickets):
    return {status: [ticket["title"] for ticket in tickets if ticket["status"] == status] for status in set(ticket["status"] for ticket in tickets)}

def summarize(tickets):
    total = len(tickets)
    par_statut = {status: sum(1 for ticket in tickets if ticket["status"] == status) for status in set(ticket["status"] for ticket in tickets)}
    priorite_max = max(tickets, key=lambda x: x["priority"])["title"]
    return {
        "total": total,
        "par_statut": par_statut,
        "priorite_max": priorite_max
    }

print(get_index(tickets))
print(filter_by_status(tickets, "active"))
print(group_by_status(tickets))
print(summarize(tickets))


from collections import defaultdict

def group_by_status_v2(tickets):
    groupes = defaultdict(list)
    for ticket in tickets:
        groupes[ticket["status"]].append(ticket["title"])
    return dict(groupes)
print(group_by_status_v2(tickets))