# FisicApp

Página web y app Android para hacer física con la cámara del teléfono (iPhone y Android). Al entrar se elige entre dos herramientas: **Ángulos** y **Movimiento**.

Interfaz con estilo de dispositivo de bolsillo retro: carcasa roja, lente que se enciende con la cámara, luces de estado (verde = teléfono nivelado, amarilla = lectura retenida, roja = dato registrado) y botones inferiores para Inicio, Medir y Registro.

- **Medir:** visor con cruz que muestra el ángulo de **elevación** y el ángulo **horizontal** (desde una referencia 0° que fija el usuario), con línea de nivel. Cada ángulo se registra por separado tocando su cuadro, con el nombre del punto actual y una foto del visor.
- **Movimiento:** con el teléfono fijo, se toca un objeto en la imagen y la app lo sigue cuadro a cuadro (por su forma o por su color). Con una escala (arrastrar sobre una regla de largo conocido) entrega t, x, y, vx, vy y v; gráficos x–t, y–t, v–t e y–x con ajuste lineal o cuadrático (velocidad, aceleración y R²); tabla en CSV e imagen con la trayectoria.
- **Registro:** crea o abre registros, agrega mediciones con la cámara o datos a mano (punto, elevación, horizontal, distancia, nota), edítalos y descárgalos como CSV para Excel; las fotos se comparten o descargan aparte.

Ábrela en: https://ggeorgetoledo-collab.github.io/FisicApp/

**App Android (APK):** https://github.com/ggeorgetoledo-collab/FisicApp/releases/download/apk/FisicApp.apk

El APK se compila solo con GitHub Actions (`.github/workflows/apk.yml`) usando Capacitor: `apk/preparar.sh` arma el proyecto Android desde `index.html`, con permiso de cámara, ícono propio y pantalla siempre encendida. `apk/iconos.py` genera los íconos de `apk/res`.

Profesor Gonzalo George Toledo
