from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%y %H:%M")
        return data_formatada

    def __str__(self):
        return self.formata_data()

    def tempo_cadasto(self, dias):
        tempo = (datetime.today() + timedelta(days=dias)) - self.momento_cadastro
        return tempo