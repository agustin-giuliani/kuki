from brain.tools.registry import ToolRegistry
from brain.tools.permissions import PermissionManager
from brain.tools.executor import ToolExecutor
from brain.tools.basic import obtener_hora
from brain.tools.catalog import ToolCatalog
from brain.tools.selector import ToolSelector
from brain.tools.authorization import AuthorizationManager
from brain.tools.internet import (
    consultar_internet,
    buscar_internet
)


class ToolManager:

    def __init__(self):

        self.registry = ToolRegistry()
        self.permissions = PermissionManager()

        self.autorizacion = AuthorizationManager(
            self.permissions
        )

        self._registrar_herramientas()

        self.catalogo = ToolCatalog(
            self.registry,
            self.permissions
        )

        self.selector = ToolSelector(
            self.catalogo
        )

        self.executor = ToolExecutor(
            self.registry,
            self.permissions
        )

    def _registrar_herramientas(self):

        self.registry.registrar(
            "hora",
            obtener_hora,
            "Obtiene la hora actual."
        )

        self.permissions.registrar(
            "hora",
            "seguro",
            True
        )
        self.registry.registrar(
            "internet",
            buscar_internet,
            "Permite buscar informacion en Internet."
        )

        self.permissions.registrar(
            "internet",
            "autorizacion",
            False
        )

    def ejecutar(self, nombre, *args, **kwargs):

        return self.executor.ejecutar(
            nombre,
            *args,
            **kwargs
        )

    def listar(self):

        return self.registry.listar()
        
    def obtener_info(self, nombre):

        return self.catalogo.obtener(nombre)

    def listar_detallado(self):

        return self.catalogo.listar()

    def seleccionar(self, texto):

        return self.selector.seleccionar(texto)

    def ejecutar_seleccion(self, texto, *args, **kwargs):

        herramienta = self.seleccionar(texto)

        if herramienta is None:

            return {
                "estado": "herramienta_no_encontrada",
                "herramienta": None
            }

        resultado = self.ejecutar(
            herramienta,
            *args,
            **kwargs
        )

        resultado["herramienta"] = herramienta

        return resultado

    def solicitar_permiso(self, herramienta):

            return self.autorizacion.solicitar(
                herramienta
            )
    
    def aprobar_permiso(self, herramienta):

        return self.autorizacion.aprobar(
            herramienta,
            origen="usuario"
        )


    def rechazar_permiso(self, herramienta):

        return self.autorizacion.rechazar(
            herramienta,
            origen="usuario"
        )

    def listar_solicitudes(self):

        return self.autorizacion.listar_solicitudes()
