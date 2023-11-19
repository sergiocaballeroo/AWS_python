import os
import subprocess

def using_os():
    
    print("Para usar el método os y listar los archivos"
    +"en este directorio: ")   
    os.system("ls")
  

using_os()


def using_Subprocess():
    print("Ahora utilizando un método más reciente"
    +"llamado subprocess.run(): ")
    subprocess.run("ls")

    
using_Subprocess()

def using_Subprocess_2():
    print("Ahora usando argumentos en el comando"
    + "para hacerlo es necesario separar las palabras "
    + 'por ejemplo "ls", "-l')
    
    subprocess.run(["ls", "-l"])
using_Subprocess_2()

def bashWith_Subprocess():
    command = "uname"
    commandArgument = "-a"
    print(f'Gathering system infomation with command: {command} {commandArgument}')
    subprocess.run([command,commandArgument])
    
def processRunning():
    command ="ps"
    commandArgument="-x"
    print(f'Gathering active process now with command: {command} {commandArgument}')
    subprocess.run([command, commandArgument])
    
processRunning()
