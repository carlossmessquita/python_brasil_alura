from validate_docbr import CPF, CNPJ
'''Package validate_docbr importado do PyPI...
Feito para utilizar as funções de CPF e CNPJ
'''
#Factory:
class Documento:
# Método Estático para realizar Factory no código:
    @staticmethod
    def cria_doc(documento):
        if len(documento) == 11:
            return Cpf(documento)
        if len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError('Documento Inválido!')

# Classes com características próprias para CPF e CNPJ
class Cpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF Inválido!')

    def __str__(self):
        return self.formata()
# Método valida() para realizar a validação do CPF digita com uso do método .validate()
    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
# Formatação padrão de CPF com o método .mask()
    def formata(self):
        mask = CPF()
        return mask.mask(self.cpf)


class Cnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ Inválido!')

    def __str__(self):
        return self.formata()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def formata(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)
