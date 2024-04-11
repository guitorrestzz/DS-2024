programa{
	
	funcao inicio(){

		          real tx1, tx2	
		          inteiro livro	
		
				escreva("Digite quantos livros você ira comprar: ")
				leia(livro)
			
				escreva("Opções: ")
				escreva("\n[1] - R$ 0,25 por livro + R$ 7,50 fixo")
				escreva("\n[2] - R$ 0,50 por livro + R$ 2,50 fixo")
		
		          tx1 = (livro * 0.25) + 7.50
		          tx2 = (livro * 0.50) + 2.50
				
			
				  se(tx1 > tx2){
			     	escreva("\nA melhor opção é: R$ 0,50 por livro + R$ 2,50 fixo [2]- R$ ", tx2)
			
				} senao se(tx2 > tx1)
					escreva("\nA melhor opção é: R$ 0,25 por livro + R$ 7,50 fixo [1]- R$ ", tx1)
		
			
			} 
	
			      
		     	

     
		}

	
	
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 667; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */