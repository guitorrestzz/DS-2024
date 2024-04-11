programa{
			
	funcao inicio(){
	real tx, moeda, resultado
	inteiro opcao

     escreva("Qual a cotação do Dolár: ")
     leia(tx)
     
	escreva("\nEscolha: ")
	escreva("[1] - Converter Dólar para Real \n")
	escreva("[2] - Converter Real para Dólar \n")
	escreva("Digite um número para a conversão: ")
	leia(opcao)

     se(opcao == 1){
	  escreva("Qual o valor em Dólar a ser convertido para Real: ")
	  leia(moeda)
	
	resultado = moeda * tx	
	} senao {
       escreva("Qual o valor em Real a ser convertido para Dólar: ")
	  leia(moeda)
	  
	resultado = moeda / tx		
}    escreva("O valor é: ", resultado)
}
}

	

  
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 624; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */