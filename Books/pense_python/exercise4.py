import turtle
import math
bob = turtle.Turtle()
#1
#Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle. Ela deve usar o turtle para desenhar um quadrado. Escreva uma chamada de função que passe bob como um argumento para o square e então execute o programa novamente

#2
#Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para que o comprimento dos lados seja length e então altere a chamada da função para fornecer um segundo argumento. Execute o programa novamente. Teste o seu programa com uma variedade de valores para length. 

def square(bob, lenght):
    for x in range(0,4):
        bob.fd(lenght)
        bob.lt(90)
    turtle.mainloop()


#square(bob, 20)

#2
#Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro chamado n e altere o corpo para que desenhe um polígono regular de n lados.

def polygon(bob, lenght, n, r):
    angle = 360/n
    for x in range(n):
        bob.fd(lenght)
        bob.lt(angle)
    r = lenght / (2 * math.sin(math.pi / n))
    circle(bob, lenght, r )

#polygon(bob, 25, 10, 15)

#3
#Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros e desenhe um círculo aproximado ao chamar polygon com um comprimento e número de lados adequados. Teste a sua função com uma série de valores de r.

def circle(bob, lenght, r):
    circumference = 2 * math.pi * r
    segments = 100
    segments_lenght = circumference / segments
    angle = 360/ segments
    bob.pu
    bob.fd(lenght/2) #centering
    bob.pd
    for x in range(segments):
        bob.fd(segments_lenght)
        bob.lt(angle)
    turtle.mainloop()

#polygon(bob, 100, 8, 35)

#4
#Faça uma versão mais geral do circle chamada arc, que receba um parâmetro adicional de angle, para determinar qual fração do círculo deve ser desenhada. angle está em unidades de graus, então quando angle=360, o arc deve desenhar um círculo completo.

def arc(bob, r,  angle):
    circumference = 2 * math.pi * r
    arc_length = circumference * (angle / 360)
    segments = 100 #segments to draw the circle 
    segment_length = arc_length / segments
    turn_angle = angle / segments
    for x in range(segments):
        bob.fd(segment_length)
        bob.lt(turn_angle)
    turtle.mainloop()

#arc(bob, 15, 180)


#1 (Desenhos):
#Flores:
