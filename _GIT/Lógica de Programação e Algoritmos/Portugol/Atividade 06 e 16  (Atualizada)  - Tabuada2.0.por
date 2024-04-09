programa{
	
	funcao inicio(){
		inteiro numero, inicio, termino
		escreva("Tabuada de qual número?: ")
		leia(inicio)

		escreva("Começar a tabuada com qual valor?:")
		leia(numero)
		

		escreva("Fazer a tabuada até qual valor?:")
		leia(termino)
		para(inteiro i = inicio; i <= termino; i++){
			escreva(i * numero, "\n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 330; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */