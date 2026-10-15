# Proyecto de Automatización de Urban Routes

## Descripción del proyecto

Este proyecto consiste en automatizar pruebas de interfaz de Urban Routes, una aplicación para configurar rutas y solicitar un taxi.

El objetivo fue practicar la automatización con Python, Selenium y Pytest, comprobando diferentes funcionalidades del proceso de solicitud.

## Mi trabajo

Preparé pruebas para revisar la configuración de la ruta, la selección de la tarifa Comfort, los datos del teléfono y del método de pago, el mensaje para el conductor y algunas opciones adicionales del pedido.

También organicé el código usando el patrón Page Object, separando los elementos y las acciones de la página de los casos de prueba. Utilicé esperas explícitas para interactuar con los elementos y comprobaciones para validar los valores esperados.

## Tecnologías utilizadas

- Python 3.12
- Selenium
- Pytest
- WebDriver Manager
- PyCharm

## Escenarios de prueba

| Escenario | ¿Qué se verifica? |
|---|---|
| Configuración de la ruta | Que los campos de origen y destino tengan los valores esperados. |
| Tarifa Comfort | Que se seleccione la tarifa Comfort. |
| Teléfono y método de pago | La preparación de los datos del pedido y la información del método de pago. |
| Mensaje para el conductor | Que el mensaje ingresado coincida con el esperado. |
| Manta y pañuelos | Que se active la opción correspondiente. |
| Dos helados | Que el contador indique dos helados. |

## Organización de los archivos

- `main.py`: contiene la configuración del navegador y los casos de prueba.
- `pages.py`: reúne los localizadores y las acciones de la interfaz mediante la clase `UrbanRoutesPage`.
- `helpers.py`: busca el código de confirmación del teléfono en los registros del navegador.
- `data.py`: contiene los datos y la URL utilizados durante las pruebas.
- `requirements.py`: archivo de dependencias presente en el proyecto.

## Instalación y configuración

1. Clonar el repositorio.
2. Abrir el proyecto en PyCharm.
3. Configurar el entorno virtual de Python.
4. Instalar Selenium, Pytest y las demás dependencias necesarias.
5. Revisar la URL configurada en `data.py` y comprobar que el servidor de pruebas esté disponible antes de ejecutar los casos.

## Ejecución de las pruebas

Para ejecutar las pruebas del archivo:

```bash
pytest main.py -v
```

Para ejecutar un caso específico:

```bash
pytest main.py::TestUrbanRoutes::test_agregar_tarjeta -v
```

## Evidencias y resultados

Este repositorio permite revisar el código, la organización de las pruebas y los escenarios automatizados.

La ejecución depende de que el servidor de pruebas esté disponible. Los resultados se documentarán cuando sea posible ejecutar las pruebas y comprobar su salida.

## Autora

Elisa Diaz
