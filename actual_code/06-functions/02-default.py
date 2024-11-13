def greeter(name, greeting="Hello", method="email"):
    print(f"{greeting}, {name}.")


greeter("Meriem", "Hola")
greeter("Harry", "Oi")
greeter("Jena", "Bonjour")
greeter("Zoe")  # create a default argument!
greeter()
