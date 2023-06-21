class Local:

    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre","unknown")
        self.localidad = kwargs.get("localidad","unknow")
        self.img = kwargs.get("img","url")

    def returned_string(self):
        return f"""
        ('{self.nombre}','{self.localidad}','{self.img}')
        """