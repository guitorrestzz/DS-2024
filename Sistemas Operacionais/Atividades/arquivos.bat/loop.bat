@echo off

chcp 65001 >nul 

:inicio
cls
echo Escolha uma opção
echo 1 - abrir calculadora
echo 2 - abrir bloco de notas
echo 3 - abrir paint

SET /p opcao= "Digite sua opção:"

echo %opcao%

if "%opcao%"=="1" (
	start calc.exe
)
	if "%opcao%"=="2" (
	start notepad.exe
 )
 
 if "%opcao%"=="3" (
	start mspaint.exe
)
goto inicio
pause
cls
