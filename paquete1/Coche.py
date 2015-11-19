from subprocess import call
import webbrowser
class Coche:
    #Intentando aprender python
    x = int;
    y = int;
    marca = str;

    def __init__(self,x, y):
        self.x = x;
        self.y = y;

    def decirHola(self):
        print("HOLAAAAAAAA")

    def setterX(self, x):
        self.x = x;

    def setterY(self, y):
        self.y = y;

    def setterMarca(self, marca):
        self.marca = marca;

def main():
    miCoche = Coche(3,4)
    miCoche.decirHola()
    print('Variables de mi coche ' , str(miCoche.x) , ' y ' , str(miCoche.y))
    miCoche.setterX(7)
    print('Variables de mi coche ' , str(miCoche.x) , ' y ' , str(miCoche.y))
    miCoche.setterMarca('Audi')
    print('La marca de mi coche es ' , miCoche.marca)
    webbrowser.open("http://tumblr.com", new=0, autoraise=True)



if __name__ == '__main__':
    main()






