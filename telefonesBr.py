import re


# Criação de Classe:
class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número incorreto!')

    # Validando o telefone recebido:
    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    # Define a representação string do nosso numero formatado:
    def __str__(self):
        return self.formata_num()

    # Máscara:
    def formata_num(self):
        padrao = "([0-9]{3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)

        if resposta.group(1) != None:
            numero_formatado = f"+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"
        else:
            numero_formatado = f"({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"
        return numero_formatado
