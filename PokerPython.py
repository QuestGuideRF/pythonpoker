import random
import os
import numpy
import time
dinero =500
dineroCrupier =1200
partida =0
partidasGanadas =0
partidasPerdidas =0
MAX_SUMA =21
MIN_APUESTA =10
MAX_APUESTA =1000
MAX_CARTAS =5
MAX_PARTIDAS =100
DINERO_INICIAL =500
DINERO_CRUPIER_INICIAL =1200
def obtenerCarta ():
	cartas =[2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ]
	return int (numpy .random .choice (cartas ))
def formatearCartas (cartas ):
	if not cartas :
		return "Нет карт"
	cartas_formateadas =[]
	for carta in cartas :
		valor =int (carta )
		if valor ==11 :
			cartas_formateadas .append ("Валет")
		elif valor ==10 :
			cartas_formateadas .append ("10")
		else :
			cartas_formateadas .append (str (valor ))
	return " | ".join (cartas_formateadas )
def mostrarCartasVisual (cartas ,esJugador =True ):
	if not cartas :
		return ""
	resultado =[]
	for carta in cartas :
		valor =int (carta )
		if valor ==11 :
			symbol ="J"
		elif valor ==10 :
			symbol ="10"
		else :
			symbol =str (valor )
		carta_visual =f
		resultado .append (carta_visual )
	return "\n".join (resultado )
def poker ():
	global dinero ,dineroCrupier ,partida ,partidasGanadas ,partidasPerdidas
	if partida >=MAX_PARTIDAS :
		os .system ("cls")
		print ("="*60 )
		print ("ДОСТИГНУТО МАКСИМАЛЬНОЕ КОЛИЧЕСТВО ПАРТИЙ!")
		print (f"Сыграно партий: {partida }/{MAX_PARTIDAS }")
		print ("="*60 )
		mostrarEstadisticas ()
		return
	barajaJugador =[]
	barajaCrupier =[]
	apuestaJugador =0
	apuestaCrupier =0
	jugadorTermino =False
	crupierTermino =False
	barajaJugador .append (obtenerCarta ())
	barajaCrupier .append (obtenerCarta ())
	apuestaJugador =hacerApuesta ()
	if apuestaJugador ==0 :
		return
	apuestaCrupier =min (apuestaJugador ,dineroCrupier )
	dineroCrupier -=apuestaCrupier
	print (f"\n✓ Крупье поставил {apuestaCrupier } монет.")
	time .sleep (1 )
	while True :
		try :
			sumaJugador =sum (int (c )for c in barajaJugador )
			sumaCrupier =sum (int (c )for c in barajaCrupier )
			if sumaJugador >MAX_SUMA and not jugadorTermino :
				os .system ("cls")
				print ("="*60 )
				print ("⚠ ПЕРЕБОР! ⚠")
				print ("="*60 )
				print (f"Ваша сумма карт ({sumaJugador }) превышает максимум ({MAX_SUMA })!")
				print (f"\nВаши карты: {formatearCartas (barajaJugador )}")
				print (f"Сумма: {sumaJugador }")
				print (f"\nКарты крупье: {formatearCartas (barajaCrupier )}")
				print (f"Сумма крупье: {sumaCrupier }")
				print ("\n"+"="*60 )
				print ("❌ КРУПЬЕ ВЫИГРАЛ РУКУ! ❌")
				print ("="*60 )
				time .sleep (3 )
				perderPartida (apuestaJugador ,apuestaCrupier )
				return
			if sumaCrupier >MAX_SUMA and not crupierTermino :
				os .system ("cls")
				print ("="*60 )
				print ("🎉 КРУПЬЕ ПЕРЕБРАЛ! 🎉")
				print ("="*60 )
				print (f"Сумма карт крупье ({sumaCrupier }) превышает максимум ({MAX_SUMA })!")
				print (f"\nКарты крупье: {formatearCartas (barajaCrupier )}")
				print (f"Сумма: {sumaCrupier }")
				print (f"\nВаши карты: {formatearCartas (barajaJugador )}")
				print (f"Ваша сумма: {sumaJugador }")
				print ("\n"+"="*60 )
				print ("✅ ИГРОК ВЫИГРАЛ РУКУ! ✅")
				print ("="*60 )
				time .sleep (3 )
				ganarPartida (apuestaJugador ,apuestaCrupier )
				return
			if jugadorTermino and crupierTermino :
				compararResultados (barajaJugador ,barajaCrupier ,apuestaJugador ,apuestaCrupier )
				return
			os .system ("cls")
			mostrarTablero (barajaJugador ,barajaCrupier ,apuestaJugador ,apuestaCrupier ,jugadorTermino )
			if not jugadorTermino :
				opcion =int (input ("\n➤ Ваш выбор: "))
				if opcion ==1 :
					if len (barajaJugador )>=MAX_CARTAS :
						print (f"\n⚠ Максимум карт ({MAX_CARTAS }) уже достигнут!")
						time .sleep (1 )
						continue
					nuevaCarta =obtenerCarta ()
					barajaJugador .append (nuevaCarta )
					sumaJugador =sum (int (c )for c in barajaJugador )
					print (f"\n✓ Вы получили карту: {nuevaCarta }")
					print (f"📊 Ваша текущая сумма: {sumaJugador }")
					if sumaJugador >MAX_SUMA :
						print (f"\n⚠ ПЕРЕБОР! Сумма {sumaJugador } превышает максимум {MAX_SUMA }!")
						time .sleep (2 )
						continue
					sumaCrupier =sum (int (c )for c in barajaCrupier )
					if sumaCrupier <17 and len (barajaCrupier )<MAX_CARTAS :
						nuevaCartaCrupier =obtenerCarta ()
						barajaCrupier .append (nuevaCartaCrupier )
						sumaCrupier =sum (int (c )for c in barajaCrupier )
						print (f"✓ Крупье взял карту. Его сумма: {sumaCrupier }")
						if sumaCrupier >MAX_SUMA :
							print (f"⚠ Крупье перебрал! Сумма: {sumaCrupier }")
							time .sleep (2 )
							continue
					time .sleep (1.5 )
				elif opcion ==2 :
					jugadorTermino =True
					print ("\n✓ Вы решили остаться.")
					time .sleep (1 )
					sumaCrupier =sum (int (c )for c in barajaCrupier )
					while sumaCrupier <17 and len (barajaCrupier )<MAX_CARTAS :
						nuevaCartaCrupier =obtenerCarta ()
						barajaCrupier .append (nuevaCartaCrupier )
						sumaCrupier =sum (int (c )for c in barajaCrupier )
						print (f"✓ Крупье взял карту. Его сумма: {sumaCrupier }")
						time .sleep (0.8 )
						if sumaCrupier >MAX_SUMA :
							print (f"⚠ Крупье перебрал! Сумма: {sumaCrupier }")
							break
					crupierTermino =True
					time .sleep (1 )
				elif opcion ==3 :
					os .system ("cls")
					print ("="*60 )
					print ("Выход из партии.")
					print ("="*60 )
					print ("СПАСИБО ЗА ИГРУ!")
					print ("="*60 )
					print (f"Выиграно партий: {partidasGanadas }")
					print (f"Проиграно партий: {partidasPerdidas }")
					print ("="*60 )
					time .sleep (3 )
					return
				else :
					print ("⚠ Неверная команда! Выберите 1, 2 или 3.")
					time .sleep (1 )
			else :
				time .sleep (1 )
		except ValueError :
			print ("⚠ Введите число!")
			time .sleep (1 )
		except Exception as e :
			print (f"⚠ Ошибка: {e }")
			time .sleep (1 )
def hacerApuesta ():
	global dinero
	if dinero <MIN_APUESTA :
		os .system ("cls")
		print ("="*60 )
		print ("ИГРА ОКОНЧЕНА")
		print ("="*60 )
		print (f"У вас недостаточно денег для минимальной ставки ({MIN_APUESTA })!")
		print (f"Ваш баланс: {dinero }")
		print ("="*60 )
		mostrarEstadisticas ()
		return 0
	while True :
		try :
			os .system ("cls")
			print ("="*60 )
			print ("💰 РАЗМЕЩЕНИЕ СТАВКИ 💰")
			print ("="*60 )
			print (f"Ваши деньги: {dinero } монет")
			print (f"Минимальная ставка: {MIN_APUESTA } монет")
			print (f"Максимальная ставка: {min (MAX_APUESTA ,dinero )} монет")
			print ("="*60 )
			print ("Введите сумму ставки (0 для выхода):")
			apuesta =int (input ("➤ "))
			if apuesta ==0 :
				return 0
			if apuesta <MIN_APUESTA :
				print (f"\n⚠ Минимальная ставка: {MIN_APUESTA } монет!")
				time .sleep (1.5 )
				continue
			if apuesta >MAX_APUESTA :
				print (f"\n⚠ Максимальная ставка за раз: {MAX_APUESTA } монет!")
				time .sleep (1.5 )
				continue
			if apuesta >dinero :
				print (f"\n⚠ У вас недостаточно денег! Доступно: {dinero } монет")
				time .sleep (1.5 )
				continue
			dinero -=apuesta
			print (f"\n✓ Вы поставили {apuesta } монет.")
			time .sleep (1 )
			return apuesta
		except ValueError :
			print ("\n⚠ Введите число!")
			time .sleep (1 )
		except Exception as e :
			print (f"\n⚠ Ошибка: {e }")
			time .sleep (1 )
def mostrarTablero (barajaJugador ,barajaCrupier ,apuestaJugador ,apuestaCrupier ,jugadorTermino ):
	global dinero ,dineroCrupier ,partida
	sumaJugador =sum (int (c )for c in barajaJugador )
	sumaCrupier =sum (int (c )for c in barajaCrupier )
	banco =apuestaJugador +apuestaCrupier
	print ("╔"+"═"*58 +"╗")
	print ("║"+f"💰 Деньги: {dinero }  │  🎴 Карты: {len (barajaJugador )}/{MAX_CARTAS }  │  🎮 Партия: {partida }/{MAX_PARTIDAS }".center (56 )+"║")
	print ("╚"+"═"*58 +"╝")
	print ("\n"+"─"*60 )
	print ("👔 КРУПЬЕ")
	print ("─"*60 )
	if jugadorTermino :
		print (f"🎴 Карты: {formatearCartas (barajaCrupier )}")
		print (f"📊 Сумма: {sumaCrupier }")
		if sumaCrupier >MAX_SUMA :
			print ("⚠ ПЕРЕБОР!")
	else :
		primera_carta =int (barajaCrupier [0 ])
		print (f"🎴 Карты: {primera_carta } | ?")
		print (f"📊 Сумма: ?")
	print (f"💰 Деньги: {dineroCrupier }")
	print ("─"*60 )
	print (f"\n{'🏆 БАНК: '+str (banco )+' монет 🏆':^60}")
	print ("\n"+"─"*60 )
	print ("👤 ИГРОК")
	print ("─"*60 )
	print (f"🎴 Карты: {formatearCartas (barajaJugador )}")
	print (f"📊 Сумма: {sumaJugador }")
	if sumaJugador >MAX_SUMA :
		print ("❌ ПЕРЕБОР!")
	elif sumaJugador ==MAX_SUMA :
		print ("🎯 БЛЭКДЖЕК! (21)")
	elif sumaJugador >=18 :
		print ("⚠ Осторожно! Близко к перебору!")
	elif sumaJugador >=15 :
		print ("⚡ Средний риск")
	else :
		print ("✅ Безопасно")
	print (f"💰 Деньги: {dinero }")
	print ("─"*60 )
	if not jugadorTermino :
		print ("\n"+"─"*60 )
		print ("📋 ДЕЙСТВИЯ:")
		print ("─"*60 )
		print ("1️⃣  Взять ещё карту")
		print ("2️⃣  Остаться")
		print ("3️⃣  Выйти из партии")
		print ("─"*60 )
	else :
		print ("\n⏳ Ожидание завершения хода крупье...")
def compararResultados (barajaJugador ,barajaCrupier ,apuestaJugador ,apuestaCrupier ):
	global dinero ,dineroCrupier ,partidasGanadas ,partidasPerdidas
	sumaJugador =sum (int (c )for c in barajaJugador )
	sumaCrupier =sum (int (c )for c in barajaCrupier )
	os .system ("cls")
	print ("╔"+"═"*58 +"╗")
	print ("║"+"📊 РЕЗУЛЬТАТЫ ПАРТИИ".center (56 )+"║")
	print ("╚"+"═"*58 +"╝")
	print ("\n"+"─"*60 )
	print ("👤 ВАШИ КАРТЫ")
	print ("─"*60 )
	print (f"🎴 {formatearCartas (barajaJugador )}")
	print (f"📊 Сумма: {sumaJugador }")
	print ("\n"+"─"*60 )
	print ("👔 КАРТЫ КРУПЬЕ")
	print ("─"*60 )
	print (f"🎴 {formatearCartas (barajaCrupier )}")
	print (f"📊 Сумма: {sumaCrupier }")
	print ("─"*60 )
	if sumaJugador >MAX_SUMA :
		print ("\n"+"="*60 )
		print ("❌ КРУПЬЕ ВЫИГРАЛ РУКУ! (Перебор у игрока)")
		print ("="*60 )
		perderPartida (apuestaJugador ,apuestaCrupier )
		return
	elif sumaCrupier >MAX_SUMA :
		print ("\n"+"="*60 )
		print ("✅ ИГРОК ВЫИГРАЛ РУКУ! (Перебор у крупье)")
		print ("="*60 )
		ganarPartida (apuestaJugador ,apuestaCrupier )
		return
	elif sumaJugador >sumaCrupier :
		print ("\n"+"="*60 )
		print ("✅ ИГРОК ВЫИГРАЛ РУКУ!")
		print ("="*60 )
		ganarPartida (apuestaJugador ,apuestaCrupier )
	elif sumaJugador <sumaCrupier :
		print ("\n"+"="*60 )
		print ("❌ КРУПЬЕ ВЫИГРАЛ РУКУ!")
		print ("="*60 )
		perderPartida (apuestaJugador ,apuestaCrupier )
	else :
		print ("\n"+"="*60 )
		print ("🤝 НИЧЬЯ!")
		print ("="*60 )
		print ("Ставки возвращены.")
		dinero +=apuestaJugador
		dineroCrupier +=apuestaCrupier
		partida +=1
		time .sleep (2 )
		poker ()
	time .sleep (3 )
def ganarPartida (apuestaJugador ,apuestaCrupier ):
	global dinero ,dineroCrupier ,partidasGanadas ,partida
	banco =apuestaJugador +apuestaCrupier
	dinero +=banco
	partidasGanadas +=1
	partida +=1
	print (f"\n🎉 Вы выиграли {banco } монет!")
	print (f"💰 Ваш баланс: {dinero }")
	if dineroCrupier <=0 :
		print ("\n"+"="*60 )
		print ("🏆 ПОЗДРАВЛЯЕМ! ВЫ ПОБЕДИЛИ!")
		print ("У крупье закончились деньги!")
		print ("="*60 )
		mostrarEstadisticas ()
		return
	if dinero <=0 :
		print ("\n"+"="*60 )
		print ("💔 ИГРА ОКОНЧЕНА")
		print ("У вас закончились деньги!")
		print ("="*60 )
		mostrarEstadisticas ()
		return
	time .sleep (2 )
	poker ()
def perderPartida (apuestaJugador ,apuestaCrupier ):
	global dinero ,dineroCrupier ,partidasPerdidas ,partida
	banco =apuestaJugador +apuestaCrupier
	dineroCrupier +=banco
	partidasPerdidas +=1
	partida +=1
	print (f"\n💸 Вы проиграли {apuestaJugador } монет.")
	print (f"💰 Ваш баланс: {dinero }")
	if dinero <=0 :
		print ("\n"+"="*60 )
		print ("💔 ИГРА ОКОНЧЕНА")
		print ("У вас закончились деньги!")
		print ("="*60 )
		mostrarEstadisticas ()
		return
	if dineroCrupier <=0 :
		print ("\n"+"="*60 )
		print ("🏆 ПОЗДРАВЛЯЕМ! ВЫ ПОБЕДИЛИ!")
		print ("У крупье закончились деньги!")
		print ("="*60 )
		mostrarEstadisticas ()
		return
	time .sleep (2 )
	poker ()
def mostrarEstadisticas ():
	global partidasGanadas ,partidasPerdidas ,partida ,dinero
	print ("\n"+"╔"+"═"*58 +"╗")
	print ("║"+"📊 СТАТИСТИКА ИГРЫ".center (56 )+"║")
	print ("╚"+"═"*58 +"╝")
	print (f"\n✅ Выиграно партий: {partidasGanadas }")
	print (f"❌ Проиграно партий: {partidasPerdidas }")
	if partidasGanadas +partidasPerdidas >0 :
		porcentaje =(partidasGanadas /(partidasGanadas +partidasPerdidas ))*100
		print (f"📈 Процент побед: {porcentaje :.1f}%")
	print (f"🎮 Всего партий: {partida }")
	print (f"💰 Финальный баланс: {dinero } монет")
	print ("\n"+"="*60 )
	print ("🙏 СПАСИБО ЗА ИГРУ!")
	print ("="*60 )
	time .sleep (5 )
def main ():
	global dinero ,dineroCrupier ,partida ,partidasGanadas ,partidasPerdidas
	while True :
		try :
			os .system ("cls")
			print ("""------------------------
 _____
|A .  |	/БЛЭКДЖЕК 21/
| /.\ |
|(_._)| - 1. НАЧАТЬ
|  |  |	- 2. ВЫХОД
|____V|""")
			print ("------------------------")
			user =int (input ("> "))
			if user ==1 :
				dinero =DINERO_INICIAL
				dineroCrupier =DINERO_CRUPIER_INICIAL
				partida =0
				partidasGanadas =0
				partidasPerdidas =0
				os .system ("cls")
				print ("="*60 )
				print ("🎮 НАЧАЛО НОВОЙ ИГРЫ - БЛЭКДЖЕК 21")
				print ("="*60 )
				print (f"💰 Ваш начальный капитал: {dinero } монет")
				print (f"🎴 Максимальная сумма карт: {MAX_SUMA } (перебор = проигрыш)")
				print (f"📊 Максимум карт в руке: {MAX_CARTAS }")
				print (f"💵 Минимальная ставка: {MIN_APUESTA } монет")
				print (f"💵 Максимальная ставка: {MAX_APUESTA } монет")
				print ("="*60 )
				time .sleep (2 )
				poker ()
				break
			elif user ==2 :
				os .system ("cls")
				print ("👋 До свидания!")
				time .sleep (1 )
				break
			else :
				print ("⚠ Неверная команда! Выберите 1 или 2.")
				time .sleep (1 )
		except ValueError :
			print ("⚠ Введите число!")
			time .sleep (1 )
		except KeyboardInterrupt :
			print ("\n\n👋 Выход из игры...")
			break
if __name__ =="__main__":
	main ()