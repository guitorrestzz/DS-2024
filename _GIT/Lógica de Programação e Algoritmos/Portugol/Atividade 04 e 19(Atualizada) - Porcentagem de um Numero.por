programa{
	
	funcao inicio() {
	real numero, porcentagem, resultado
	caracter letra = 's'
	enquanto(letra == 's'){
	
	
	escreva("Digite o numero:") 
	leia(numero)
	escreva("\nDigite a porcentagem:")
	leia(porcentagem)

	resultado = numero * (porcentagem / 100)
	

	escreva("\nO resultado é: ", resultado)

	escreva("\nDeseja repetir?: [s/n] ")
		leia(letra)

	
		}
	} 
	
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 363; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */