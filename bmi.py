# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def get_bmi(weight: float, height: float) -> float:
    # Compute the bmi
    bmi = weight / (height ** 2)

    return bmi


def interpret_bmi(bmi) -> str:
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'


def main():
    # Get 2 numbers from the user
    weight = float(input('Enter your weight in kilograms (kg): '))
    height = float(input('Enter your height in meters (m): '))

    bmi = get_bmi(weight, height)
    interpret_bmi(bmi)
    print(f'Your BMI score is: {bmi:.2f}')
    print(f'You are: {interpret_bmi(bmi)}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
