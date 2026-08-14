from brain.tools.result import ToolResult


print("--- TOOL RESULT ---")


resultado = ToolResult(
    "ok",
    resultado="10:30",
    herramienta="hora"
)

print(
    resultado.to_dict()
)


resultado_error = ToolResult(
    "permiso_denegado",
    mensaje="No tiene permiso.",
    herramienta="internet"
)

print(
    resultado_error.to_dict()
)
