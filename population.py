from organism import Organism

class Population:
    def __init__(self, species_name: str, organisms: list):
        """Инициализация популяции.
        :param species_name: название вида
        :param organisms: список организмов этого вида
        """
        self.species_name = species_name
        self.organisms = organisms

    def add_organism(self, organism: Organism):
        """Добавляет организм в популяцию.
        :param organism: экземпляр класса Organism
        """
        self.organisms.append(organism)

    def get_alive_count(self) -> int:
        """Считает количество живых организмов в популяции.
        :return: количество живых организмов
        """
        return sum(1 for org in self.organisms if org.is_alive())

    def simulate_day(self):
        """Моделирует один день из жизни популяции: организмы теряют энергию."""
        for org in self.organisms:
            org.lose_energy(2.0)  # потеря энергии за день
