class Alquiler:
    def __init__(self, id_alquiler, nombre,descripcion, localidad,img,  precio_noche, link_reservar):
        self.id_alquiler = id_alquiler
        self.nombre = nombre
        self.descripcion = descripcion
        self.localidad = localidad
        self.img = img
        self.precio_noche = precio_noche
        self.link_reservar = link_reservar

class AlquilerManager:
    def __init__(self):
        self.alquileres = []

    def crear_alquiler(self, id_alquiler, nombre, descripcion, localidad, img, precio_noche, link_reservar):
        alquiler = Alquiler(id_alquiler, nombre, descripcion,  localidad, precio_noche, link_reservar)
        self.alquileres.append(alquiler)

    def obtener_alquileres(self):
        return self.alquileres

    def obtener_alquiler_por_id(self, id_alquiler):
        for alquiler in self.alquileres:
            if alquiler.id_alquiler == id_alquiler:
                return alquiler
        return None

    def actualizar_alquiler(self, id_alquiler, nombre,descripcion, localidad,img, precio_noche, link_reservar):
        alquiler = self.obtener_alquiler_por_id(id_alquiler)
        if alquiler:
            alquiler.nombre = nombre
            alquiler.descripcion = descripcion
            alquiler.localidad = localidad
            alquiler.img = img
            alquiler.precio_noche = precio_noche
            alquiler.link_reservar = link_reservar
            return True
        return False

    def eliminar_alquiler(self, id_alquiler):
        alquiler = self.obtener_alquiler_por_id(id_alquiler)
        if alquiler:
            self.alquileres.remove(alquiler)
            return True
        return False


alquiler_manager = AlquilerManager()

# Crear alquileres
alquiler_manager.crear_alquiler(1,"Departamento Vivi", "Apartamento céntrico","Bariloche", "https://cf.bstatic.com/xdata/images/hotel/max1280x900/422916059.jpg?k=a609bc8d48d3df0e53fce7f04581b712869fd2a9f5a58bb934332025fce4ca80&o=&hp=1", 344000,"https://www.booking.com/Share-sRdnqx")
alquiler_manager.crear_alquiler(2, "pepito","Casa en la montaña ", "Bariloche","https://cf.bstatic.com/xdata/images/hotel/max1280x900/422916059.jpg?k=a609bc8d48d3df0e53fce7f04581b712869fd2a9f5a58bb934332025fce4ca80&o=&hp=1",40000,'https://www.booking.com/Share-sRdnqx')
alquiler_manager.crear_alquiler(3, "chalet", "Chalet en la montaña", "Carlos Paz", "https://cf.bstatic.com/xdata/images/hotel/max1280x900/422916059.jpg?k=a609bc8d48d3df0e53fce7f04581b712869fd2a9f5a58bb934332025fce4ca80&o=&hp=1",50000,'https://www.booking.com/Share-sRdnqx')

# Obtener alquileres
alquileres = alquiler_manager.obtener_alquileres()
for alquiler in alquileres:
    print(f"ID: {alquiler.id_alquiler}, Nombre: {alquiler.nombre},Descripcion: {alquiler.descripcion}, Local: {alquiler.local},Foto: {alquiler.img} Precio: {alquiler.precio} Reservar:{alquiler.link_reservar}")

# Actualizar un alquiler
if alquiler_manager.actualizar_alquiler(2, "Apartamento en el centro", "Ciudad de México", 180):
    print("Alquiler actualizado correctamente.")
else:
    print("No se encontró el alquiler con el ID especificado.")

# Eliminar un alquiler
if alquiler_manager.eliminar_alquiler(3):
    print("Alquiler eliminado correctamente.")
else:
    print("No se encontró el alquiler con el ID especificado.")

alquiler_manager = AlquilerManager()
alquileres = alquiler_manager.obtener_alquileres(1)