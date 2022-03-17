
import animales


menu = {
     '1': '1. Búho \U0001F989 ',
     '2': '2. Delfín \U0001F42C',
     '3': '3. Tortuga \U0001F422',
     "0": '0. Salir',
}
print('Bienvenido al juego de animales')


class Animal():
    def __init__(self, animal_type):
        self.animal_type = animal_type
    

    def mostrar_animal(self):
        animal_art = getattr(animales, self.animal_type)
        return animal_art


if __name__== '__main__':
    for option in menu:
      print(menu.get(option))

    while True:
        user_input = input('Ingresa una opción: ')
        if user_input == '0':
            #salir
            print('Hasta pronto \U0001F609')
            break
        elif user_input in menu:
            #imprimir
            menu_value = menu.get(user_input)
            menu_value.split(' ')
            #user_input = Animal()
        
            if user_input == '1':
                print(animales.buho)
            if user_input == '2':
                print(animales.delfin)
            if user_input == '3':
                print(animales.tortuga)
            #animal = Animal(buho.animal_type) 
            #print(buho.mostrar_animal())
            #print('mostrar')
        else:
            #opcion invalida
            print('Lo siento, Opción no válida \U0001F636')
        