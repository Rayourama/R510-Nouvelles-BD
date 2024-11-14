import subprocess
import time

def execute_script_and_analyze_complexity():
    # Mesurer le temps de début
    start_time = time.perf_counter()
    
    # Exécuter le script `script.py`
    process = subprocess.run(["python", "script.py"], capture_output=True, text=True)
    
    # Mesurer le temps de fin
    end_time = time.perf_counter()
    
    # Calculer le temps d'exécution
    execution_time = end_time - start_time
    
    # Analyser la complexité
    # Le script effectue les opérations suivantes :
    # - Lecture des fichiers : suppose que cela prend un temps linéaire O(N)
    # - Insertion des données dans Redis : suppose que cela prend un temps linéaire O(R)
    # La complexité temporelle totale est donc de O(N + R), où :
    # - N est le nombre de lignes dans tous les fichiers d'entrée combinés
    # - R est le nombre de réservations
    
    complexity = "O(N + R)"  # Déclaration de la complexité
    
    # Afficher la sortie du script, le temps d'exécution et la complexité estimée
    print("Sortie du script :", process.stdout)
    print("Temps d'exécution :", execution_time, "secondes")
    print("Complexité estimée :", complexity)
    
    # Retourner le temps d'exécution et la complexité
    return execution_time, complexity

# Exécuter la fonction si le fichier est appelé directement
if __name__ == "__main__":
    execute_script_and_analyze_complexity()