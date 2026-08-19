# Variables and Data Types



def generate_profile(name: str, age: int, height: float, is_student: bool) -> dict:
    """Constructs a structured profile dictionary and validates input types."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string.")

    if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
        raise ValueError("Age must be a positive integer.")

    if not isinstance(height, (int, float)) or height <= 0:
        raise ValueError("Height must be a positive number.")

    if not isinstance(is_student, bool):
        raise ValueError("is_student must be a boolean.")

    return {
        "name": name.strip(),
        "age": age,
        "height_m": float(height),
        "is_student": is_student,
    }

def print_profile_summary(profile: dict) -> None:
   
    print("--- Profile Overview ---")
    for key, value in profile.items():
        print(f"{key.capitalize().replace('_', ' ')}: {value} (Type: {type(value).__name__})")

if __name__ == "__main__":
    user_profile = generate_profile(
        name="Yaswanth Putla",
        age=17,
        height=5.7,
        is_student=True
    )
    print_profile_summary(user_profile)