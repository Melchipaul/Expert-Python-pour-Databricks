import time

# Version liste
debut = time.time()
total = sum([i for i in range(100)])
print(f"Liste : {time.time() - debut:.3f}s")  # → ~0.8s

# Version générateur
debut = time.time()
total = sum(i for i in range(100))
print(f"Générateur : {time.time() - debut:.3f}s")  # → ~0.4s