# Champurrado Jumpscare

App para Windows que corre en segundo plano y, **cada segundo**, evalúa una probabilidad de **0.000001%** de mostrar una imagen de champurrado en pantalla.

## Comportamiento

- Intervalo de chequeo: 1 segundo.
- Probabilidad por chequeo: `0.000001%` (equivale a `0.00000001`).
- Cuando activa, muestra una ventana fullscreen con la imagen.
- Cierra con clic, tecla `Esc` o automáticamente tras unos segundos.

## Imágenes de champurrado

Coloca una o varias imágenes dentro de la carpeta [assets/Champurrado](assets/Champurrado).

Formatos soportados:

- `jpg`
- `jpeg`
- `png`
- `bmp`
- `webp`
- `heic`
- `heif`

En cada aparición, la app elige una imagen aleatoria de esa carpeta.

Si no encuentra imágenes, muestra una imagen placeholder.

## Construir EXE

Requisitos:

- Python 3.11+

Comando recomendado en Windows:

```powershell
./scripts/build.cmd
```

Alternativa:

```powershell
powershell -ExecutionPolicy Bypass -File ./scripts/build.ps1
```

Salida:

- `dist/ChampurradoJumpscare.exe`

## Crear instalador

Requisitos:

- Inno Setup 6 instalado (ruta esperada: `C:\Program Files (x86)\Inno Setup 6\ISCC.exe`)

Comando recomendado en Windows:

```powershell
./scripts/build-installer.cmd
```

Alternativa:

```powershell
powershell -ExecutionPolicy Bypass -File ./scripts/build-installer.ps1
```

Salida:

- `installer/ChampurradoJumpscare-Setup.exe`

El instalador copia también la carpeta `assets/Champurrado` al directorio de instalación.

## Instalar en otra computadora

Requisitos en la computadora destino:

- Windows 10 u 11 de 64 bits.
- No necesita Python.
- No necesita Inno Setup.

Pasos:

1. Ejecutar `ChampurradoJumpscare-Setup.exe`.
2. Elegir carpeta de instalación.
3. Opcional: crear acceso directo en escritorio.
4. Finalizar el asistente.
5. Abrir la app desde el menú Inicio o el acceso directo.

Si quieres agregar o cambiar imágenes después de instalar, colócalas en:

- `assets/Champurrado` dentro de la carpeta donde quedó instalada la app.
