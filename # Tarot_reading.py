# Tarot_reading
import time

def opening():
    opening_lines = [
        "Welcome to the mystical world of tarot reading...",
        "Here, the cards hold the answers to many of life's questions.",
        "What mysteries will they reveal to you today?",
        "Let's get started! \n"
    ]
    
    for line in opening_lines:
        print(line)
        time.sleep(0.5)  # Wait for 2 seconds before displaying the next line

opening()

def user_info():
    name = input("What is your name? ")
    age = input("How old are you? ")
    gender = input("What is your gemder (f/m/?)? ")

    return name, age, gender
user_info()

positive_tarot_cards = {
    0: ("The Fool", "New beginnings, innocence, adventure."),
    1: ("The Magician", "Manifestation, resourcefulness, power."),
    3: ("The Empress", "Creativity, fertility, abundance."),
    4: ("The Emperor", "Authority, stability, control."),
    5: ("The Hierophant", "Tradition, wisdom, guidance."),
    6: ("The Lovers", "Love, harmony, relationships."),
    7: ("The Chariot", "Success, determination, willpower."),
    8: ("Strength", "Courage, confidence, inner power."),
    17: ("The Star", "Hope, inspiration, serenity."),
    19: ("The Sun", "Joy, success, vitality."),
    21: ("The World", "Completion, fulfillment, achievement.")
}

challenging_tarot_cards = {
    2: ("The High Priestess", "Secrets, hidden agendas, intuition."),
    9: ("The Hermit", "Isolation, solitude, contemplation."),
    10: ("Wheel of Fortune", "Change, cycles, unpredictability."),
    11: ("Justice", "Fairness, truth, cause and effect."),
    12: ("The Hanged Man", "Sacrifice, letting go, restriction."),
    13: ("Death", "Endings, transformation, letting go."),
    14: ("Temperance", "Balance, moderation, patience."),
    15: ("The Devil", "Bondage, materialism, ignorance."),
    16: ("The Tower", "Upheaval, chaos, revelation."),
    18: ("The Moon", "Fear, confusion, misunderstanding."),
    20: ("Judgement", "Reflection, reckoning, awakening.")
}

def draw_tarot_card(card_number):
    if card_number in positive_tarot_cards:
        card_name, card_meaning = positive_tarot_cards[card_number]
        description1 = "It looks like you have a positive result."
        print(f"Your card is {card_name} and the meaning is {card_meaning}" + description1)
    else:
        card_name, card_meaning = challenging_tarot_cards[card_number]
        description2 = "It looks like you have a challenging result."
        print(f"Your card is {card_name} and the meaning is {card_meaning}" + description2)
    
  
def questions_answer():
    questions = [
    "1. If you want to know your current relationship status, please choose a number.",
    "2. If you want to know your future relationship status, please choose a number.",
    "3. If you want to know your current working status, please choose a number.",
    "4. If you want to know your future working status, please choose a number."
    ]
    for question in questions:
        while True: #infinite loop
            response = input(question + "\n" + "number:0~21" + " (or type 'pass'): ").strip().lower()
            if response == "pass":
                print("Move on to the next question.")
                continue  
            else:
                try:
                    card_number = int(response)
                    if card_number in range(0, 22):
                        draw_tarot_card(card_number)
                        break # exit the loop 
                    else:
                        print("Please enter a number between 0 and 21.")
                except ValueError:
                    print("Please enter a valid number or 'pass'. \n")
    print("Anyway, you are special.\nDon't worry, you will be just fine.\n")
questions_answer()

