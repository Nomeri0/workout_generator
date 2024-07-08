print("Welcome to the Workout Generator!")

equipment = input("Enter available equipment (none, dumbbells, bands, kettlebells, etc.): ").lower()
fitness_level = input("Enter your fitness level (beginner, intermediate, advance): ").lower()
duration = int(input("Enter workout duration in minutes: "))

print(f"\nEquipment: {equipment}")
print(f"Fitness Level: {fitness_level}")
print(f"Duration: {duration} minutes")