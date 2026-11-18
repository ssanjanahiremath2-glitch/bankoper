
def bankoper(initialbal, deposit, withdraw):
    totalbal = initialbal + deposit
    updatedbal = totalbal - withdraw

    return totalbal, updatedbal


if __name__ == "__main__":
    initialbal = int(input("Enter initial balance: "))
    deposit = int(input("Enter amount to deposit: "))
    withdraw = int(input("Enter withdrawal amount: "))

    totalbal, updatedbal = bankoper(initialbal, deposit, withdraw)

    print("Total balance after deposit:", totalbal)
    print("Updated balance after withdrawal:", updatedbal)
