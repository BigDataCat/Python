import random
import datetime

def save_fortune_history(message):
    with open("fortune_history.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}: {message}\n")

def generate_fortune(category):
    fortunes = {
        'general': ['You will have a great day!', 'Today will be tough...but worth it.', 'You will get married this year!'],
        'love': ['Love is just around the corner.', 'A meaningful relationship will blossom.', 'Show love to those who matter.'],
        'career': ['Professional success is imminent.', 'A great opportunity is on its way.', 'Prepare for a career shift.']
    }
    fortune_text = random.choice(fortunes.get(category, ['Good luck is coming your way!']))
    return fortune_text

def calculate_luck_score():
    scores = [random.randint(0, 100) for _ in range(3)]
    return sum(scores) / len(scores)

def get_user_choice():
    while True:
        print("Choose a category for your fortune: general, love, career")
        category = input("Enter your choice: ").lower()
        if category in ['general', 'love', 'career']:
            return category
        else:
            print("Invalid category. Please choose again.")

def main():
    while True:
        user_choice = input("Do you want to receive a fortune? (yes/no): ").lower()
        if user_choice == 'yes':
            category = get_user_choice()
            fortune_text = generate_fortune(category)
            luck_score = calculate_luck_score()
            message = f"{fortune_text} Your luck score is: {luck_score:.2f}"
            print(message)
            save_fortune_history(message)
        elif user_choice == 'no':
            print("Come back anytime for your fortune!")
            break
        else:
            print("Invalid response. Please type 'yes' or 'no'.")
            continue

if __name__ == "__main__":
    main()
