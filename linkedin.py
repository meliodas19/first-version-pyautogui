import pyautogui
import time
import pyperclip
import alttab
import subprocess

def startExtraction():
    buttonUltrasCrapperX, buttonUltrasCrapperY = (921, 113)
    maxDailyExtractionsX, maxDailyExtractionsY = (719, 289)
    buttonChangeDailyExtractionsX, buttonChangeDailyExtractionsY = (808, 327)
    buttonStartStractionX, buttonStartStractionY = (761, 412)
    todayRequestsX, todayRequestsY = (821, 231)
    
    #haciendole click a el boton de ultrascrapper
    pyautogui.moveTo(buttonUltrasCrapperX, buttonUltrasCrapperY, 5)
    pyautogui.click()
    time.sleep(10)
   
    #calculando el valor para daily starctions
    pyautogui.click(todayRequestsX, todayRequestsY, 2)
    pyautogui.hotkey('ctrl', 'c')
    solicitudes = int(pyperclip.paste())
    solicitudes += 25
    pyperclip.copy(solicitudes)
    time.sleep(1)    
 
    #eliminando el valor dentro de el input max daily extractions
    pyautogui.click(maxDailyExtractionsX, maxDailyExtractionsY)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    time.sleep(1)
    
    #pego en el input el nuevo valor de daily extractions
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.click(buttonChangeDailyExtractionsX, buttonChangeDailyExtractionsY, 1)
    time.sleep(10)
    pyautogui.click(buttonStartStractionX, buttonStartStractionY)

navegador = "chromium-browser"
cuentasLinkedin = (  "luisnajarluisnajargmail", "blaydeswillis19outlook", "mariazajarova", "turuteasado3gmail", "blaydeswillisgmail", "turuteasado2gmail", "dennislarson59gmail", "dermottlynnmcgmail")
cuenta = []

for i in cuentasLinkedin:
    cuenta.append('--user-data-dir=/home/ubuntu/profiles/{0}'.format(i))

def iniciarBot():
    chromium = []
    contador = 0
    for i in cuentasLinkedin:
        #cuando contador vale 2 abre otra instancia pero ya no las mata porque no entra al if porque contador es mayor a 1 cuando contador es 3 debo volver a matarlas 
        chromium.append(subprocess.Popen([navegador, cuenta[contador], "linkedin.com"]))
        time.sleep(25)
        startExtraction()
        #cuando contador vale uno es que abrio dos instancias entonces debo esperar que terminen su trabajo y luego matarlas 
        #aqui debo esperar para abrir nuevas instancias
        if contador == 1 or contador == 3 or contador == 5 or contador == 7:
            #aqui deberia esperarlas a que terminen su trabajo
            time.sleep( 60 * 38  )
            #mato las instancias porque usando contador asi se por cual instancia va 
            chromium[contador - 1].kill()
            chromium[contador].kill()

        contador += 1
        time.sleep(35)

while True:
	iniciarBot()
