from code import Bolopuntaje

def p_valido(p):
    while True:
        try:
            value = int(input(p))
            if value < 0 or value > 10:
                raise ValueError("El puntaje debe estar entre 0 y 10")
            return value
        except ValueError as e:
            print(e)

def s_tirada(roll1):
    while True:
        try:
            roll2 = int(input("Puntaje del segundo lanzamiento: "))
            if roll1 + roll2 > 10:
                raise ValueError("La suma de los lanzamientos no puede ser mayor a 10")
            return roll2
        except ValueError as e:
            print(e)

def main():
    game = Bolopuntaje()

    print("Introduzca los puntajes para cada lanzamiento:")
    for frame in range(10):
        print(f"Frame {frame + 1}:")
        roll1 = p_valido("Puntaje del primer lanzamiento: ")
        if roll1 == 10:
            game.roll(roll1)
            continue
        roll2 = s_tirada(roll1)
        game.roll(roll1)
        game.roll(roll2)

    print("\nPuntaje final:", game.score())

if __name__ == "__main__":
    main()










