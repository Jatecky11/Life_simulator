from ecosystem import Ecosystem
from organism import Organism
from population import Population

def main():
    # Создаём экосистему
    eco = Ecosystem()

    # Создаём популяции
    rabbits = Population("Заяц", [
        Organism("Заяц1", 50),
        Organism("Заяц2", 50),
        Organism("Заяц3", 50)
    ])

    foxes = Population("Лиса", [
        Organism("Лиса1", 30),
        Organism("Лиса2", 30)
    ])

    # Добавляем популяции в экосистему
    eco.add_population(rabbits)
    eco.add_population(foxes)

    # Симулируем несколько дней
    for day in range(5):
        print(f"\nДень {day + 1}:")
        eco.simulate_day()
        eco.print_status()

if __name__ == "__main__":
    main()
