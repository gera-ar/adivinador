from random import randint
from time import sleep
import os

# Evitar el cartel de bienvenida de la librería pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
mixer.init()
SILVATO = mixer.Sound("sonidos/start.ogg")
WINNER = mixer.Sound("sonidos/winner.ogg")
LOOSER = mixer.Sound("sonidos/looser.ogg")
NEXT = mixer.Sound("sonidos/next.ogg")

class Configuraciones():
	def __init__(self):
		self.colores = ["negro", "azul", "verde", "agua", "rojo", "morado", "amarillo", "blanco", "gris"]
		self.num_max = None
		self.rondas = None
		self.ronda = 1
		self.fondo = None
		self.letras = None
		self.jugador = None
		self.dificultad = None
		self.init()

	def init(self):
		self.jugador = input("Hola. Por favor escribe tu nombre y pulsa intro")
		while True:
			print(f"Bienvenido {self.jugador}!\nEs momento de personalizar un poco el aspecto de el fondo y las letras. Comencemos por el fondo, y luego las letras.\nEscribe el color que quieras y al finalizar pulsa intro. Los colores disponibles son:")
			for color in self.colores:
				print(color)
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
			self.dificultad = input("Ahora es el turno de la dificultad. Ingresa el número de opción y pulsa intro:\n1 Facilona\n2 Solo para valientes\n3 ¡imposible!")
			if self.dificultad == "1":
				self.num_max = 20
				self.rondas = 6
				print("Has seleccionado la opción 1. A ver como te va con la facilona...")
				break
			elif self.dificultad == "2":
				self.num_max = 50
				self.rondas = 7
				print("¡Apa! Aquí tenemos a alguien valiente. Mucha suerte...")
				break
			elif self.dificultad == "3":
				self.num_max = 100
				self.rondas = 8
				print("!Atención! Una personita intrépida que se le anima al imposible. A cruzar los dedos...")
				break
			else:
				print("Has ingresado un valor incorrecto. Vuelve a intentarlo")
		self.rand = randint(1, self.num_max)
		sleep(1.8)
		mixer.music.stop()
		SILVATO.play()
		sleep(1)

class Juego():

	def __init__(self):
		mixer.music.load("sonidos/init.ogg")
		mixer.music.play(-1)
		print("¡Adivinador!")
		sleep(2)
		self.configuraciones = Configuraciones()
		self.start()

	def start(self):
		mixer.music.load("sonidos/background.ogg")
		mixer.music.play(-1)
		mixer.music.set_volume(0.2)
		while self.configuraciones.ronda <= self.configuraciones.rondas:
			self.rondas()
			try:
				usuario = int(input())
			except ValueError:
				print("Valor incorrecto")
				continue
			if usuario < 1 or usuario > self.configuraciones.num_max:
				print("Fuera de rango")
				continue
			if usuario == self.configuraciones.rand:
				self.winner()
				break
			elif usuario > self.configuraciones.rand:
				if self.configuraciones.ronda < self.configuraciones.rondas:
					print("nops..d. 😳. Es un número menor")
			elif usuario < self.configuraciones.rand:
				if self.configuraciones.ronda < self.configuraciones.rondas:
					print("nops... 😳. Es un número mayor...")
			self.configuraciones.ronda+=1
			NEXT.play()
		self.looser()

	def winner(self):
		print("¡Cooooorrecto! 🫂 🥳")
		mixer.music.stop()
		WINNER.play()
		sleep(6)
		print(f"Felicitaciones {self.configuraciones.jugador}. Has ganado en la ronda {self.configuraciones.ronda}")
		sleep(2)
		self.finish("Victoria")

	def looser(self):
		mixer.music.stop()
		LOOSER.play()
		sleep(2.5)
		print(f"😥. El número secreto era el {self.configuraciones.rand}. Has perdido el juego {self.configuraciones.jugador}. Otra vez será!")
		sleep(3)
		self.finish("Derrota")

	def finish(self, estado):
		with open("historial.txt", "a") as file:
			file.write(f"jugador: {self.configuraciones.jugador}- Resultado: {estado}- dificultad: {self.configuraciones.dificultad}- rondas: {self.configuraciones.ronda}\n")
		print("Gracias por jugar")
		sleep(1.5)
		exit()

	def rondas(self):
		if self.configuraciones.ronda == 1:
			print(f"¡Que comience el juego!. El número que debes adivinar está entre 1 y {self.configuraciones.num_max}. Cuál es tu apuesta? Tienes {self.configuraciones.rondas} oportunidades")
		elif self.configuraciones.ronda == self.configuraciones.rondas:
			print("¡última oportunidad! 😨")
		else:
			print(f"ronda {self.configuraciones.ronda}")

Juego()