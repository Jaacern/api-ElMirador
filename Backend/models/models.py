from bson import ObjectId
from config.config import mongo

class Departamento:
    @staticmethod
    def to_json(departamento):
        return {
            "_id": str(departamento.get("_id", "")),
            "CodDepto": departamento.get("CodDepto"),
            "codEdificio": departamento.get("codEdificio"),
            "Piso": departamento.get("Piso"),
            "Numero": departamento.get("Numero"),
            "Arrendado": departamento.get("Arrendado"),
            "RutProp": departamento.get("RutProp"),
            "Estado": departamento.get("Estado"),
            "RutArre": departamento.get("RutArre"),
            "FechaIniC": departamento.get("FechaIniC"),
            "FechaFinC": departamento.get("FechaFinC"),
            "Observacion": departamento.get("Observacion"),
            "NumHab": departamento.get("NumHab"),
            "NumBaños": departamento.get("NumBaños")
        }


    class Acceso:
        @staticmethod
        def to_json(acceso):
            return {
                "username": acceso.get("username"),
                "password": acceso.get("password"),
                "fechaCreacion": acceso.get("fechaCreacion"),
                "fechaultimoacceso": acceso.get("fechaultimoacceso"),
                "Rut": acceso.get("Rut"),
                "Tipo": acceso.get("Tipo")
            }

class CuotaGC:
    @staticmethod
    def to_json(cuota):
        return {
            "IdCuotaGC": cuota.get("IdCuotaGC"),
            "Mes": cuota.get("Mes"),
            "Año": cuota.get("Año"),
            "ValorPagado": cuota.get("ValorPagado"),
            "FechaPago": cuota.get("FechaPago"),
            "Atrazado": cuota.get("Atrazado"),
            "CodDepto": cuota.get("CodDepto"),
            "Rut": cuota.get("Rut"),
            "Nombre": cuota.get("Nombre"),
            "Telefono": cuota.get("Telefono")
        }


# Clase Residente
class Residente:
    @staticmethod
    def to_json(residente):
        return {
            "_id": str(residente.get("_id", "")),  # Si tienes un _id, lo transformas en string
            "RutArre": residente.get("RutArre"),
            "Nombre": residente.get("Nombre"),
            "ApePat": residente.get("ApePat"),
            "ApeMat": residente.get("ApeMat"),
            "Email": residente.get("Email"),
            "Fono1": residente.get("Fono1"),
            "Fono2": residente.get("Fono2"),
            "nro_departamento": residente.get("nro_departamento")
        }
     


# Clase Personal
class Personal:
    @staticmethod
    def to_json(personal):
        return {
            "_id": str(personal.get("_id", "")),
            "RutPersonal": personal.get("RutPersonal"),
            "Nombre": personal.get("Nombre"),
            "ApePat": personal.get("ApePat"),
            "ApeMat": personal.get("ApeMat"),
            "Email": personal.get("Email"),
            "Fono1": personal.get("Fono1"),
            "Fono2": personal.get("Fono2"),
            "Estado": personal.get("Estado"),
            "Cargo": personal.get("Cargo"),
            "HoraInicioJ": personal.get("HoraInicioJ"),
            "HoraFinJ": personal.get("HoraFinJ"),
        }



# Clase GastoComun
class GastoComun:
    @staticmethod
    def to_json(gasto):
        return {
            "_id": str(gasto.get("_id", "")),
            "mes": gasto.get("mes"),
            "anio": gasto.get("anio"),
            "valor": gasto.get("valor"),
            "nro_departamento": gasto.get("nro_departamento"),
            "estado_pago": gasto.get("estado_pago", False)
        }
  


class Reclamo:
    @staticmethod
    def to_json(reclamo):
        return {
            "_id": str(reclamo.get("_id", "")),
            "titulo": reclamo.get("titulo"),
            "categoria": reclamo.get("categoria"),
            "descripcion": reclamo.get("descripcion"),
            "ubicacion": reclamo.get("ubicacion"),
            "archivos": reclamo.get("archivos", []),
            "nombre": reclamo.get("nombre"),
            "correo": reclamo.get("correo"),
            "telefono": reclamo.get("telefono"),
            "fecha": reclamo.get("fecha"),
            "urgencia": reclamo.get("urgencia"),
            "estado": reclamo.get("estado", "Activo")
        }