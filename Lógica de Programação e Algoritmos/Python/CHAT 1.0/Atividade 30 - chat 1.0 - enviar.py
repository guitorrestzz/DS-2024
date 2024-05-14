from click import clear
import socket

nome = input("Qual seu nome?")

while True:
    clear()
    mensagem = input("Digite a sua mensagem: \n")
    with open("chat_1.txt", "a") as arquivo:
        arquivo.write(f'{nome} | {mensagem} \n')
