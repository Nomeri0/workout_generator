# workout_generator.py

def get_user_input():
    equipment = input("What equipment do you have available (none, dumbbells, bands)? ").lower()
    fitness_level = input("What is your fitness level (beginner, intermediate, advanced)? ").lower()
    duration = int(input("How many minutes do you want to work out? "))

    return equipment, fitness_level, duration

def determine_reps(fitness_level):
    if fitness_level == 'beginner':
        return 10
    elif fitness_level == 'intermediate':
        return 15
    elif fitness_level == 'advanced':
        return 20
    else:
        return 10  # default value if fitness level is not recognized

def generate_workout(equipment, fitness_level, duration):
    # Updated exercises dictionary based on equipment and fitness level
    exercises = {
        'none': {
            'beginner': ['Jumping Jacks', 'Push-ups', 'Squats'],
            'intermediate': ['Burpees', 'Mountain Climbers', 'Lunges'],
            'advanced': ['Pistol Squats', 'Handstand Push-ups', 'One-arm Push-ups']
        },
        'dumbbells': {
            'beginner': ['Dumbbell Curls', 'Dumbbell Press', 'Dumbbell Rows'],
            'intermediate': ['Arnold Press', 'Bent-over Rows', 'Dumbbell Deadlifts'],
            'advanced': ['Dumbbell Snatches', 'Dumbbell Clean and Press', 'Renegade Rows']
        },
        'bands': {
            'beginner': ['Band Pull-aparts', 'Band Rows', 'Band Chest Press'],
            'intermediate': ['Band Squats', 'Band Deadlifts', 'Band Shoulder Press'],
            'advanced': ['Band Thrusters', 'Band Overhead Squats', 'Band Burpees']
        }
    }

    # Choose exercises based on available equipment and fitness level
    chosen_exercises = exercises.get(equipment, {}).get(fitness_level, [])

    if not chosen_exercises:
        return "No suitable exercises found for the selected equipment and fitness level."

    # Determine the number of reps based on fitness level
    reps = determine_reps(fitness_level)

    workout_plan = f"Equipment: {equipment}\n"
    workout_plan += f"Fitness Level: {fitness_level}\n"
    workout_plan += f"Duration: {duration} minutes\n"
    workout_plan += f"Workout Plan:\n"

    for exercise in chosen_exercises:
        workout_plan += f"- {exercise}: {reps} reps\n"

    return workout_plan

def main():
    print("Welcome to the Workout Generator!")
    equipment, fitness_level, duration = get_user_input()
    workout_plan = generate_workout(equipment, fitness_level, duration)
    print(workout_plan)

if __name__ == "__main__":
    main()
