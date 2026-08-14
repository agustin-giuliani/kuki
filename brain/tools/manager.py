from brain.tools.registry import ToolRegistry
from brain.tools.permissions import PermissionManager
from brain.tools.executor import ToolExecutor
from brain.tools.basic import obtener_hora
from brain.tools.catalog import ToolCatalog
from brain.tools.selector import ToolSelector
from brain.tools.authorization import AuthorizationManager
from brain.tools.authorization_planner import AuthorizationPlanner
from brain.tools.authorization_executor import AuthorizationExecutor
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

        self.planificador_autorizacion = AuthorizationPlanner(
            self.selector
        )

        self.autorizacion_executor = AuthorizationExecutor(
            self.autorizacion
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

    def ejecutar_plan(self, plan):

        if not plan.get("necesita_herramienta"):

            return {
                "estado": "sin_herramienta",
                "herramienta": None
            }

        herramienta = plan.get(
            "herramienta"
        )

        datos = plan.get(
            "datos",
            {}
        )

        if herramienta is None:

            return {
                "estado": "herramienta_no_encontrada",
                "herramienta": None
            }

        resultado = self.ejecutar(
            herramienta,
            **datos
        )

        resultado["herramienta"] = herramienta

        return resultado

    def ejecutar_autorizacion(self, resultado_lenguaje):

        plan = self.planificador_autorizacion.planificar(
            resultado_lenguaje
        )

        resultado = self.autorizacion_executor.ejecutar(
            plan
        )

        return {
            "plan": plan,
            "resultado": resultado
        }

    def obtener_permisos(self):

        return self.permissions.listar()

    def obtener_herramientas(self):

        return self.catalogo.listar()
