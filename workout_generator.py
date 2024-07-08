import random

print("Welcome to the Workout Generator!")

#Collect user input
equipment = input("Enter available equipment (none, dumbbells, bands, kettlebells, etc.): ").lower()
fitness_level = input("Enter your fitness level (beginner, intermediate, advance): ").lower()
duration = int(input("Enter workout duration in minutes: "))

#Define some example exercises for each category
exercises = {
    'none': {
        'beginner': ['Jumping Jacks', 'Push-ups', 'Squats'],
        'intermidiate': ['Burpees', 'Mountain Climbers', 'Lunges'],
        'advanced': ['Pistol Squats', 'Handstand Push-ups', 'One-arm Push-ups']
    },
    'dumbbells':{
    'beginner': ['Dumbbell Curls', 'Dumbbell Press', 'Dumbbell Rows'],
    'intermediate': ['Band Squats', 'Band Deadlifts', 'Dumbbell Deadlifts'],
    'advanced': ['Dumbbell Snatches', 'Dumbbell Clean and Press', 'Renegade Rows']
    },
    'bands': {
        'beginner': ['Band Pull-aparts', 'Band Rows', 'Band Chest Press'],
        'intermediate': ['Band Squats', 'Band Deadlifts', 'Band Shoulder Press'],
        'advanced': ['Band Thursters', 'Band Overhead Squats', 'Band Burpees']
    }
}

# Generate a workout
selected_exercises = exercises.get(equipment, {}).get(fitness_level, [])
workout_plan = random.sample(selected_exercises, min(len(selected_exercises), 3))

# Print the workout plan
print("\nYour workout plan:")
for exercise in workout_plan:
    print(f"- {exercise}")

