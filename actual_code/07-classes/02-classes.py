# class -> blueprint
class Person:
    """
    Class of person which holds information about them
    name, team, tenure, hourly_rate
    """
    def __init__(self, name, team="BBC", tenure=0, hourly_rate=100):   # double underscore  -> dunder methods -> dunder init
        self.name = name
        self.team = team
        self.tenure = tenure
        self.hourly_rate = hourly_rate

    def __str__(self):
        # return f"{self.name} works in {self.team}"
        return f"Person(name={self.name}, team={self.team})"

    def work_birthday(self):
        print(f"Happy birthday (at work) - you previously were {self.tenure} BBC years old!")
        self.tenure += 1
        print(f"You are now {self.tenure} BBC years old.")

    def calculate_pay(self, hours_worked):
        return self.hourly_rate * hours_worked


# object -> house/person/thing - actual concrete example
bachir = Person(name="Bachir", team="Media Services", tenure=7)
print(bachir)  # where he is in memory!  "Bachir works in Media Services"
bachir.work_birthday()
bachir.work_birthday()
bachir.work_birthday()

jena = Person("Jena", "CDO", 0)
print(jena)  # "Jena works in CDO"   "Person(Jena, CDO)"  "Person, name=Jena, team=CDO"
jena.work_birthday()
jena.work_birthday()


print(f"{jena.tenure} at the end")
print(f"{bachir.tenure} at the end")

print(jena.calculate_pay(12))