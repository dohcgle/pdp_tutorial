import random

GameOver = ValueError

def random_number():
    return random.randint(1,10)

def chek_number(number, guess):
    message = "Men o'ylagan son "
    if number < guess:
        return f"{message} {guess}dan kichik"
    if number > guess:
        return f"{message} {guess}dan katta"
    raise GameOver

def main():
    number = random_number()
    print(f"Men 1-10 oraligida bir son o'yladim. {number}")
    guess = int(input("Tahminingizni kiriting: "))
    error_answer = 0
    while number != guess:
        if error_answer == 3:
            print("Siz o'yinda yutqazdingiz")
            break
        error_answer += 1
        try:
            message = chek_number(number, guess)
            print(message)
            guess = int(input("Tahminingizni kiriting: "))
        except GameOver:
            print("O'ylangan sonni topdingiz")
            break
if __name__ == '__main__':
    main()