import machine                                                                                                                                                
from machine import Pin, I2C
import ssd1306
 
i2c = I2C(0, scl=Pin(27), sda=Pin(14))
led = machine.Pin(5, machine.Pin.OUT)
led2 = machine.Pin(26, machine.Pin.OUT)
botao = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
botao2 = machine.Pin(23, machine.Pin.IN, machine.Pin.PULL_UP)
 
 
 
largura = 128
altura = 64
 
tela = ssd1306.SSD1306_I2C(largura, altura, i2c)
while True:
    blue = botao.value()
    red = botao2.value()
 
    if blue == 0:
        tela.fill(0)
        tela.text("A temperatura do ", 0, 0)
        tela.text("QUARTO e de: ", 0, 10)
        tela.text("23 graus", 0, 20)
        tela.show()
        led.value(1)
        led2.value(0)
       
       
   
    if red == 0:
         tela.fill(0)
         tela.text("A temperatura da", 0, 0)
         tela.text("COZINHA e de :", 0, 10)
         tela.text("28 graus", 0, 20)
         tela.show()
         led2.value(1)
         led.value(0)