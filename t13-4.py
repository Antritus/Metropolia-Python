class Emo:
    nimi = "emoluokka"
    tila = "Toiminnassa"

    def tulosta(self):
        print(self.tila)
        print(f"Minä olen {self.nimi}.")

class Lapsi(Emo):
    nimi = "lapsiluokka"


emo = Emo()
emo.tulosta()
lapsi = Lapsi()
lapsi.tulosta()