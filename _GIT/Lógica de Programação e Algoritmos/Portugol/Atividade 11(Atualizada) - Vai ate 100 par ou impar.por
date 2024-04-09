programa{
	inclua biblioteca Util --> u
	funcao inicio(){
	inteiro valor, resultado

		resultado = (valor % 2)

		se(resultado > 0) {
			escreva("Seu número é Ímpar")

		} senao {
		     escreva("Seu número é Par")

		     para(inteiro valor, i = 5, resultado)
		     	escreva(u.sorteia(1,100), "\n")
		     }
		     
			

			
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 264; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */