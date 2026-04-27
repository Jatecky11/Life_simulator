from population import Population

class Ecosystem:
    def __init__(self):
        """Инициализация экосистемы (список популяций)."""
        self.populations = []

    def add_population(self, population: Population):
        """Добавляет популяцию в экосистему.
        :param population: экземпляр класса Population
        """
        self.populations.append(population)

    def simulate_day(self):
        """Моделирует один день в экосистеме:
        - организмы теряют энергию;
        - живые организмы могут питаться.
        """
        for population in self.populations:
            population.simulate_day()  # потеря энергии

        # Пример взаимодействия (хищники едят жертв)
        self.hunt()

    def hunt(self):
        """Моделирует охоту (например, лисы едят зайцев)."""
        foxes = self.get_population_by_name("Лиса")
        rabbits = self.get_population_by_name("Заяц")

        if foxes and rabbits:
            for fox in foxes.organisms:
                if fox.is_alive():
                    for rabbit in rabbits.organisms:
                        if rabbit.is_alive():
                            fox.eat(10.0)  # лиса ест зайца, получает 10 энергии
                            rabbit.lose_energy(100.0)  # заяц умирает (теряет всю энергию)
                            break  # лиса ест только одного зайца в день

    def get_population_by_name(self, name: str) -> Population | None:
        """Находит популяцию по названию вида.
        :param name: название вида
        :return: популяция или None, если не найдена
        """
        for pop in self.populations:
            if pop.species_name == name:
                return pop
        return None

    def print_status(self):
        """Выводит текущий статус экосистемы (количество живых организмов в каждой популяции)."""
        print("\n=== СТАТУС ЭКОСИСТЕМЫ ===")
        for pop in self.populations:
            alive = pop.get_alive_count()
            total = len(pop.organisms)
            print(f"{pop.species_name}: {alive}/{total} живы")
