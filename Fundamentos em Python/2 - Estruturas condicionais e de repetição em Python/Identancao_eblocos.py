# Papel da Identcação

    # - A estética
        # Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo
        # papel, através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina

    # - Bloco de comando
        # As linguagens de programação costumam utilizar caracteres ou palavras reservadas para determinar o início e fim
        # do bloco. Em Java e C por exemplo, utilizamos chaves

    # Bloco em Java
        # void sacar(double valor) { // início do bloco do método
        #   if(this.saldo >= valor) {// início do bloco do if
        #       this.saldo -= valor;
        #   } //Fim do bloco do if
        #} // Fim do bloco do método

    # Bloco em Java
            # void sacar(double valor) { // início do bloco do método
            # if(this.saldo >= valor) {// início do bloco do if
            # this.saldo -= valor;
            #} //Fim do bloco do if
            #} // Fim do bloco do método

# Utilizando espaços
    # Existe uma ocnvenção em Python, que define as boas práticas oara escrita de código na linguagem. Besse documento é indicado
    # utilizar 4 espaços em branco por nível de identação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco

# Bloco em Python

def sacar(self, valor: float) -> None: #inicio do bloco do método
    if self.saldo >= valor: #Inicio do bloco do If
        self.saldo -= valor

        # Fim do bloco do If

#Fim do bloco do método

#Isso não funciona em Python

  # Bloco em Python

def sacar(self, valor: float) -> None: #inicio do bloco do método
if self.saldo >= valor: #Inicio do bloco do If
self.saldo -= valor
# Fim do bloco do If
#Fim do bloco do método


#O exemplo acima não funciona pous o interpretador simplesmente não entende o que está sendo escrito.
# É possível colocar o exemplo acima na sua IDE e ver que ele apresenta diversos erros e não interpreta o código.

