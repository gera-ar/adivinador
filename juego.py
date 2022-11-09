from random import randint
from time import sleep
import os

# Evitar el cartel de bienvenida de la librería pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
mixer.init()

class Configuraciones():
	def __init__(self):
		self.colores = ["negro", "azul", "verde", "agua", "rojo", "morado", "amarillo", "blanco", "gris"]
		self.num_max = None
		self.rondas = None
		self.ronda = 1
		self.fondo = None
		self.letras = None
		self.jugador = None
		self.init()

	def init(self):
		self.jugador = input("Hola. Por favor escribe tu nombre y pulsa intro")
		while True:
			print(f"Bienvenido {self.jugador}!\nEs momento de personalizar un poco el aspecto de el fondo y las letras. Comencemos por el fondo, y luego las letras.\nEscribe el color que quieras y al finalizar pulsa intro. Los colores disponibles son:")
			for color in self.colores:
				print(color)
				sleep(0.3)
			fondo = input("ingresa el color de fondo")
			if fondo in self.colores:
				caracteres = input("Ahora ingresa el color de los caracteres")
				if caracteres in self.colores:
					os.system(f"color {self.colores.index(fondo)}{self.colores.index(caracteres)}")
					print(f"perfecto. Has seleccionado el fondo {fondo}, y el color {caracteres} para los caracteres")
					break
		self.seleccionar_dificultad()

	def seleccionar_dificultad(self):
		while True:
			dificultad = input("Ahora es el turno de la dificultad. Ingresa el número de opción y pulsa intro:\n1 Facilona\n2 Solo para valientes\n3 ¡imposible!")
			if dificultad == "1":
				self.num_max = 20
				self.rondas = 6
				print("Has seleccionado la opción 1. A ver como te va con la facilona...")
				break
			elif dificultad == "2":
				self.num_max = 50
				self.rondas = 7
				print("¡Apa! Aquí tenemos a alguien valiente. Mucha suerte...")
				break
			elif dificultad == "3":
				self.num_max = 100
				self.rondas = 8
				print("!Atención! Una personita intrépida que se le anima al imposible. A cruzar los dedos...")
				break
			else:
				print("Has ingresado un valor incorrecto. Vuelve a intentarlo")
		self.rand = randint(1, self.num_max)

mixer.music.load("sonidos/background.ogg")
winner = mixer.Sound("sonidos/winner.ogg")
looser = mixer.Sound("sonidos/looser.ogg")
next = mixer.Sound("sonidos/next.ogg")
mixer.music.play(-1)
print("¡Adivinador!")
sleep(2)

configuraciones = Configuraciones()

while configuraciones.ronda <= configuraciones.rondas:
	if configuraciones.ronda == 1:
		print(f"¡Que comience el juego!. El número que debes adivinar está entre 1 y {configuraciones.num_max}. Cuál es tu apuesta? Tienes {configuraciones.rondas} oportunidades")
	elif configuraciones.ronda == configuraciones.rondas:
		print("¡última oportunidad! 😨")
	else:
		print(f"ronda {configuraciones.ronda}")

	try:
		usuario = int(input())
	except ValueError:
		print("Valor incorrecto")
		continue
	if usuario < 1 or usuario > configuraciones.num_max:
		print("Fuera de rango")
		continue
	if usuario == configuraciones.rand:
			print("¡Cooooorrecto! 🫂 🥳")
			mixer.music.stop()
			winner.play()
			sleep(6)
			print(f"Felicitaciones {configuraciones.jugador}. Has ganado en {configuraciones.ronda} oportunidades")
			sleep(3)
			exit()
	elif usuario > configuraciones.rand:
		if configuraciones.ronda < configuraciones.rondas:
			print("nops..d. 😳. Es un número menor")
	elif usuario < configuraciones.rand:
		if configuraciones.ronda < configuraciones.rondas:
			print("nops... 😳. Es un número mayor...")
	configuraciones.ronda+=1
	next.play()
	

mixer.music.stop()
looser.play()
sleep(2.5)
print(f"😥. El número secreto era el {configuraciones.rand}. Has perdido el juego {configuraciones.jugador}. Otra vez será!")
sleep(2)