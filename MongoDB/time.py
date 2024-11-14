import time
import subprocess

def measure_execution_time(script_name):
    start_time = time.time()  # Démarrer le chronomètre

    # Exécuter le script
    subprocess.run(['python', script_name], check=True)

    end_time = time.time()  # Arrêter le chronomètre
    execution_time = end_time - start_time  # Calculer le temps d'exécution

    return execution_time

def analyze_complexity():
    # Évaluation de la complexité temporelle des opérations
    # 1. Insertion des pilotes - O(n)
    # 2. Insertion des clients - O(m)
    # 3. Insertion des classes - O(k)
    # 4. Insertion des avions - O(p)
    # 5. Insertion des vols - O(q)
    # 6. Insertion des réservations - O(r)

    # En considérant que les nombres de lignes dans les fichiers sont respectivement n, m, k, p, q, et r.
    # Le temps d'exécution est dominé par les opérations d'insertion, donc la complexité globale est:
    # O(n + m + k + p + q + r)

    print("Complexité temporelle des opérations dans script.py : O(n + m + k + p + q + r)")

if __name__ == "__main__":
    script_name = 'script.py'
    execution_time = measure_execution_time(script_name)
    print(f"Temps d'exécution de ",script_name,' : ', execution_time, " secondes")
    analyze_complexity()