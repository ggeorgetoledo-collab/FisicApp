# FisicApp

Página web y app Android para hacer física con los sensores del teléfono (iPhone y Android). Al entrar aparecen todas las herramientas, agrupadas por sensor:

**Cámara**
- **Ángulos:** visor con cruz que muestra el ángulo de **elevación** y el ángulo **horizontal**, con registro en tablas (punto, ángulos, distancia, nota, foto) y CSV.
- **Movimiento:** con el teléfono fijo, se toca un objeto y la app lo sigue cuadro a cuadro (forma o color). Con escala entrega t, x, y, vx, vy y v; gráficos x–t, y–t, v–t e y–x con ajuste lineal o cuadrático.

**Movimiento del teléfono** (acelerómetro, giroscopio, orientación)
- **Acelerómetro:** aceleración en x, y, z y total, con o sin gravedad.
- **Giroscopio:** velocidad angular en x, y, z (°/s o rad/s).
- **Oscilaciones:** periodo y frecuencia de un péndulo (giroscopio) o un resorte (acelerómetro); calcula g = 4π²L/T² o k = 4π²m/T².
- **Nivel:** inclinación de una superficie (plano inclinado), con burbuja.
- **Brújula:** rumbo respecto del norte magnético.

**Sonido** (micrófono y parlante)
- **Sonómetro:** nivel en dB (aproximado, calibrable), máximo y promedio.
- **Frecuencia:** espectro, frecuencia principal y nota musical; historial para el efecto Doppler.
- **Osciloscopio:** forma de la onda con disparo, base de tiempo y frecuencia.
- **Cronómetro acústico:** tiempo entre dos sonidos o vueltas, con precisión de milisegundos.
- **Generador de tonos:** seno, cuadrada, triangular o diente de sierra; batimientos; muestra T y λ.

**Ubicación**
- **GPS:** rapidez, distancia recorrida, precisión y altitud.

Las herramientas que miden en el tiempo pueden **grabar**; las grabaciones quedan en **Datos**, con gráfico por canal, ajuste lineal o cuadrático, estadísticas, tabla y CSV.

Ábrela en: https://ggeorgetoledo-collab.github.io/FisicApp/

**App Android (APK):** https://github.com/ggeorgetoledo-collab/FisicApp/releases/download/apk/FisicApp.apk

El APK se compila solo con GitHub Actions (`.github/workflows/apk.yml`) usando Capacitor: `apk/preparar.sh` arma el proyecto Android desde `index.html`, con permisos de cámara, micrófono y ubicación, ícono propio y pantalla siempre encendida. `apk/iconos.py` genera los íconos de `apk/res`.

Profesor Gonzalo George Toledo
