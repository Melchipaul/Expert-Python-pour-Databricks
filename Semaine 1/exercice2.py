tickets = [
    {"id": 1, "title": "Bug login", "status": "active", "priority": 3},
    {"id": 2, "title": "Feature export", "status": "closed", "priority": 1},
    {"id": 3, "title": "Crash homepage", "status": "active", "priority": 5},
    {"id": 4, "title": "UI fix", "status": "resolved", "priority": 2},
    {"id": 5, "title": "Perf issue", "status": "active", "priority": 4},
]

# 1. Crée un dict {id: title} pour tous les tickets
index = {ticket["id"]: ticket["title"] for ticket in tickets}

print(index)

# 2. Crée un dict {id: status} uniquement pour les tickets actifs
actifs_index = {ticket["id"]: ticket["status"] for ticket in tickets if ticket["status"] == "active"}
print(actifs_index)

# 3. Crée un dict {id: priority} mais double la priorité de chaque ticket
priorites_doublees = {ticket["id"]: ticket["priority"] * 2 for ticket in tickets}
print(priorites_doublees)

# Crée un dict {status: [liste de titres]} 
# qui groupe les tickets par statut
# Résultat attendu :
# {
#   "active": ["Bug login", "Crash homepage", "Perf issue"],
#   "closed": ["Feature export"],
#   "resolved": ["UI fix"]
# }

groupes = {status: [ticket["title"] for ticket in tickets if ticket["status"] == status] for status in set(ticket["status"] for ticket in tickets)}
print(groupes)
