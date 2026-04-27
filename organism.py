class Organism:
    def __init__(self, name: str, energy: float):
        """Инициализация организма.
        :param name: имя организма
        :param energy: уровень энергии (должен быть > 0)
        """
        self.name = name
        self.energy = energy

    def eat(self, food_energy: float):
        """Организм поедает пищу и получает энергию.
        :param food_energy: количество энергии от пищи
        """
        self.energy += food_energy
        print(f"{self.name} съел и получил {food_energy} энергии.")

    def is_alive(self) -> bool:
        """Проверяет, жив ли организм.
        :return: True, если энергия > 0, иначе False
        """
        return self.energy > 0

    def lose_energy(self, loss: float):
        """Организм теряет энергию (например, из-за движения или времени).
        :param loss: количество теряемой энергии
        """
        self.energy -= loss
        if self.energy < 0:
            self.energy = 0
        print(f"{self.name} потерял {loss} энергии. Остаток: {self.energy}.")

