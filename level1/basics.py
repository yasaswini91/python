
#matchcase statements

def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return True
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
print(is_weekend("sunday"))