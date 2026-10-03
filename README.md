# Isla Brava

Juego de aventuras de bloques para navegador, hecho con HTML, CSS y JavaScript. Explorá dos islas de 500 × 500 metros, completá misiones y mejorá tu equipo. Reuní 300 puntos en el nivel 1 para enfrentar al gólem y 350 en la selva del nivel 2 para llegar al basilisco.

**Jugar:** https://roque27.github.io/IslaBrava/

La lógica del juego está íntegramente en [`isla-brava.html`](isla-brava.html). Los demás archivos permiten instalarlo como aplicación web y mostrar una imagen al compartir el enlace.

## Jugar sin conexión

Abrí el enlace una vez con conexión. Después podés instalar Isla Brava desde la opción **Instalar aplicación** o **Agregar a pantalla de inicio** del navegador compatible. El service worker guarda los archivos necesarios para que la partida pueda abrirse sin conexión.

## Desarrollo local

Desde la carpeta del proyecto, serví los archivos con cualquier servidor HTTP estático y abrí `isla-brava.html`. Para ejecutar las pruebas:

```sh
node tests/isla-brava.cjs
```

Los PNG de icono y vista previa se generan con `tools/generate_assets.py` usando Pillow.
