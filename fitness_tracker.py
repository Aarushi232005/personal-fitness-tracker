# Personal Fitness Tracker

class Workout:
    """
    Represents a single workout session.
    """
    def __init__(self, exercise_type, duration, calories_burned):
        self.exercise_type = exercise_type
        self.duration = duration  # in minutes
        self.calories_burned = calories_burned

    def __str__(self):
        """
        Returns a string representation of the workout.
        """
        return f"{self.exercise_type}: {self.duration} minutes, {self.calories_burned} calories burned"


class FitnessTracker:
    """
    Manages a collection of workouts and provides methods to add, view, save, and load data.
    """
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        """
        Adds a workout to the tracker.
        """
        self.workouts.append(workout)
        print("Workout added successfully.")

    def view_progress(self):
        """
        Displays all recorded workouts.
        """
        if not self.workouts:
            print("No workouts recorded yet.")
        else:
            print("\n--- Workout History ---")
            for i, workout in enumerate(self.workouts, 1):
                print(f"Workout {i}: {workout}")

    def save_data(self, filename="workout_data.txt"):
        """
        Saves workout data to a file.
        """
        with open(filename, "w") as file:
            for workout in self.workouts:
                file.write(f"{workout.exercise_type},{workout.duration},{workout.calories_burned}\n")
        print("Data saved successfully.")

    def load_data(self, filename="workout_data.txt"):
        """
        Loads workout data from a file.
        """
        try:
            with open(filename, "r") as file:
                for line in file:
                    exercise_type, duration, calories_burned = line.strip().split(",")
                    workout = Workout(exercise_type, int(duration), int(calories_burned))
                    self.workouts.append(workout)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")


def main():
    """
    Main function to run the fitness tracker program.
    """
    tracker = FitnessTracker()

    while True:
        print("\n--- Fitness Tracker Menu ---")
        print("1. Add Workout")
        print("2. View Progress")
        print("3. Save Data")
        print("4. Load Data")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # Add a new workout
            exercise_type = input("Enter exercise type: ")
            duration = int(input("Enter duration (in minutes): "))
            calories_burned = int(input("Enter calories burned: "))
            workout = Workout(exercise_type, duration, calories_burned)
            tracker.add_workout(workout)

        elif choice == "2":
            # View workout progress
            tracker.view_progress()

        elif choice == "3":
            # Save workout data to a file
            tracker.save_data()

        elif choice == "4":
            # Load workout data from a file
            tracker.load_data()

        elif choice == "5":
            # Exit the program
            print("Exiting the Fitness Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
