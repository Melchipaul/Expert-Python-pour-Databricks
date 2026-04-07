# Tu as cette liste de tickets Azure DevOps
tickets = [
    {"id": 1, "title": "Bug login", "status": "active", "priority": 3},
    {"id": 2, "title": "Feature export", "status": "closed", "priority": 1},
    {"id": 3, "title": "Crash homepage", "status": "active", "priority": 5},
    {"id": 4, "title": "UI fix", "status": "resolved", "priority": 2},
    {"id": 5, "title": "Perf issue", "status": "active", "priority": 4},
]

# 1. Extrais uniquement les titres de tous les tickets
titres = [ticket["title"] for ticket in tickets]
print(titres)

# 2. Extrais les tickets dont le status est "active"
actifs = [ticket for ticket in tickets if ticket["status"] == "active"]
print(actifs)

# 3. Extrais les titres des tickets actifs avec priorité > 3
critiques = [ticket["title"] for ticket in actifs if ticket["priority"] > 3]
print(critiques)


# Crée une liste de strings formatées pour un rapport
# Format attendu : "🔴 [id] - title (priorité: X)"
# Uniquement pour les tickets actifs, triés par priorité décroissante

rapport = [f"🔴 [{ticket['id']}] - {ticket['title']} (priorité: {ticket['priority']})" for ticket in sorted(actifs, key=lambda x: x['priority'], reverse=True)]
print(rapport)