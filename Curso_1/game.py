import random

options = ("piedra", "papel", "tijera")
rounds = 1
computer_wins = 0
user_wins = 0
limit = 3

while computer_wins < 3 and user_wins < 3:
  print('***' * 10)
  print('Round', rounds)
  print('***' * 10)

  user_option = input('>>> Piedra, papel o tijera => ').lower()
  rounds += 1
  computer_option = random.choice(options)

  if user_option not in options:
    print("Esa opción no es válida")
    continue

  print(f"Usuario elige: {user_option}, Computadora elige: {computer_option}")

  if user_option == computer_option:
    print("Empate!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("Piedra gana a tijera")
      print("¡Usuario gana!")
      user_wins += 1
    else:
      print("Papel gana a piedra")
      print("¡Computadora gana!")
      computer_wins += 1
  elif user_option == "papel":
    if computer_option == "piedra":
      print("Papel gana a piedra")
      print("¡Usuario gana!")
      user_wins += 1
    else:
      print("Tijera gana a papel")
      print("¡Computadora gana!")
      computer_wins += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("Tijera gana a papel")
      print("¡Usuario gana!")
      user_wins += 1
    else:
      print("Piedra gana a tijera")
      print("¡Computadora gana!")
      computer_wins += 1

win = "computer" if computer_wins > user_wins else "user"
pointsFinally = computer_wins if computer_wins > user_wins else user_wins

print(f'🎖️ El ganador es {win} con {pointsFinally} puntos 🎖️')
