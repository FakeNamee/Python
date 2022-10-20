class Worker:
    def __init__(self, workername, workersurname, workerposition, wage, bonus):
        self.name = workername
        self.surname = workersurname
        self.__position = workerposition
        self.__income = {"wage": wage, "bonus": bonus}

    def get_income(self):
        return(self.__income["wage"] + self.__income["bonus"])


class Position(Worker):
    def __init__(self, name, surname, __position, wage, bonus):
        super().__init__(name, surname, __position, wage, bonus)

    def get_full_name(self):
        return(self.name + " " + self.surname)

    def get_total_income(self):
        return(self.get_income())


job = Position("Igor", "Ivnovich", "Director Interneta", 15, 5)
print(job.get_total_income())
print(job.get_full_name())