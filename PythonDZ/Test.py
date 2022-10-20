class Worker:
    def __init__(self, workerName, workerSurname, workerPosition, wage, bonus):
        self.name = workerName
        self.surname = workerSurname
        self.__position = workerPosition
        self.__income = {"wage": wage, "bonus": bonus}

    def get_income(self):
        return(self.__income["wage"] + self.__income["bonus"])


class Position(Worker):
    def get_full_name(self):
        return(self.name + " " + self.surname)

    def get_total_income(self):
        return(self.get_income())


worker = Position("Igor", "Ivnovich", "Director Interneta", 15, 5)
worker.get_total_income()
worker.get_full_name()