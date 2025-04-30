# src/main.py

from data_ingestion.kafka_producer import run_producer
from data_processing.spark_consumer import run_consumer

def main():
    print("✅ SmartAccess2030 démarré.")
    while True:
        print("\n=== MENU ===")
        print("1. Lancer le producteur Kafka")
        print("2. Lancer le consumer Spark")
        print("3. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            run_producer()
        elif choix == "2":
            run_consumer()
        elif choix == "3":
            print("👋 Au revoir.")
            break
        else:
            print("❌ Choix invalide.")

if __name__ == "__main__":
    main()
