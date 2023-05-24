class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_dokumen(self):
        pass
    
    def get_hargasewa(self):
        return self.jml_penghuni * 5

    def get_summary(self):
        return "Hunian "+ self.jenis +"\nditempati oleh " + str(self.jml_penghuni) + " orang.\n"+"\nharga sewa gan "+ str(self.get_hargasewa()) + ".000.000.000"