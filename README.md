# FisicApp

Página web y app Android para hacer física con los sensores del teléfono (iPhone y Android). Al entrar aparecen todas las herramientas, agrupadas por sensor:

**Cámara**
- **Ángulos:** visor con cruz que muestra el ángulo de **elevación** y el ángulo **horizontal**, con registro en tablas (punto, ángulos, distancia, nota, foto) y CSV.
- **Color y luz:** color (RGB, nombre) y brillo relativo del centro de la imagen, con opción de fijar la exposición.
- **Movimiento:** con el teléfono fijo, se toca un objeto y la app lo sigue cuadro a cuadro (forma o color). Calibración con **regla** (2 puntos) o **rectángulo** (4 esquinas, corrige la perspectiva de un plano inclinado), marcando con lupa. El eje vertical se toma de la **gravedad**. En modo Color mide el tamaño aparente del objeto: **avisa si se acerca o se aleja** de la cámara y, con su diámetro real, **corrige la escala en cada cuadro** y estima la distancia z. Entrega t, x, y, (z), vx, vy y v; gráficos con ajuste lineal o cuadrático.
- **Zoom** (real si el teléfono lo permite, o digital) en Ángulos y Movimiento, con botones o pellizcando.
- **Analizar un video** guardado, también grabado en **cámara lenta** (120 o 240 cuadros por segundo): se busca el cuadro inicial con una barra, se calibra y la app procesa cada cuadro; el factor de cámara lenta (×2, ×4, ×8 u otro) convierte el tiempo del video en tiempo real.
- **Seguimiento más robusto**: el objeto se elige tocándolo o **arrastrando un rectángulo** a su alrededor; comparación que tolera cambios de luz, rechazo de saltos a otros objetos parecidos, continuación de la trayectoria si se pierde un momento y fin automático del análisis si el objeto cambia por completo o sale de la imagen. En modo Color, la app avisa (y usa la forma) si el color se parece al fondo.
- **Escala con manillas**: al tocar Escala aparece una regla (o un rectángulo) con círculos que se arrastran hasta la referencia, con lupa; luego ✓ Listo y el largo real.
- **Desplazarse con zoom**: con dos dedos se acerca y se mueve la imagen; un minimapa muestra la parte visible y, al seguir un objeto, la vista lo acompaña sola.
- **Revisión de la escala** en cada resultado: tamaño de la referencia en la imagen, plano de la referencia, perspectiva del objeto, cámara y comprobación con la gravedad (si el objeto se movía libre en el aire, la g obtenida dice cuánto se equivoca la escala). Opción de **usar la gravedad como escala** cuando el video no tiene referencia.
- **Marcar a mano** en videos: se toca el objeto en cada cuadro y la app avanza 1, 2 o 4 cuadros; ◀ deshace.
- **Lente**: elección de la cámara trasera (por ejemplo, gran angular) cuando el teléfono lo permite; cuadros por segundo de la cámara (30, 60 o 120) en Ajustes y valor real en el visor.
- **Incertidumbre de los ajustes**: velocidad o aceleración con ± (dispersión de los puntos, escala, perspectiva no corregida y tamaño del objeto), con un aviso de cuán concluyentes son los datos y el botón **+ Repetidas** para juntar varios lanzamientos.

**Movimiento del teléfono** (acelerómetro, giroscopio, orientación)
- **Acelerómetro:** aceleración en x, y, z y total, con o sin gravedad.
- **Giroscopio:** velocidad angular en x, y, z (°/s o rad/s).
- **Oscilaciones:** periodo y frecuencia de un péndulo (giroscopio) o un resorte (acelerómetro); calcula g = 4π²L/T² o k = 4π²m/T².
- **Aceleración centrípeta:** gráfico a–ω² al girar; la pendiente es el radio.
- **Ascensor:** aceleración, velocidad, altura y peso aparente.
- **Sismógrafo:** vibraciones en x, y, z sin la gravedad.
- **Nivel:** inclinación de una superficie (plano inclinado), con burbuja.
- **Brújula:** rumbo respecto del norte magnético.

**Sonido** (micrófono y parlante)
- **Sonómetro:** nivel en dB (aproximado, calibrable), máximo y promedio.
- **Frecuencia:** espectro, frecuencia principal y nota musical; historial para el efecto Doppler.
- **Espectrograma:** frecuencias en el tiempo (vocales, armónicos).
- **Osciloscopio:** forma de la onda con disparo, base de tiempo y frecuencia.
- **Cronómetro acústico:** tiempo entre dos sonidos o vueltas, con precisión de milisegundos.
- **Velocidad del sonido:** con el eco en un muro o con dos teléfonos (v = 2d/Δt).
- **Reverberación:** tiempo RT60 a partir de un aplauso.
- **Generador de tonos:** seno, cuadrada, triangular o diente de sierra; batimientos; muestra T y λ.

**Ubicación**
- **GPS:** rapidez, distancia recorrida, precisión y altitud.

**Datos e incertidumbre**
- **Mediciones repetidas:** promedio, desviación estándar, error de la media, semirrango, desviación media y resolución; resultado x̄ ± Δx redondeado. Las herramientas con un resultado tienen el botón **+ Repetidas**.
- **Propagación:** fórmula escrita libremente (con ejemplos), valores ± errores, suma de errores o suma cuadrática, y aporte de cada variable al error.
- **Compartir por QR:** cualquier grabación, movimiento, registro de ángulos o conjunto de mediciones se envía a otro teléfono como una secuencia de códigos QR comprimidos, sin internet (`lib/qrcode.js` de Kazuhiko Arase, MIT; `lib/jsQR.js`, Apache 2.0).

**Registro:** una sección propia (botón *Registro* abajo o en el inicio) que reúne tablas de ángulos, grabaciones de sensores, movimientos con la cámara y mediciones repetidas. Permite **buscar por nombre** (sin importar tildes ni mayúsculas, también en puntos y descripciones), **filtrar por fecha** (hoy, 7 días, 30 días, este año o un rango) y **por magnitud medida** (longitud, tiempo, ángulo, velocidad, aceleración, frecuencia, sonido, luz…), además de por tipo, y ordenar. Las grabaciones tienen gráfico por canal, ajuste lineal o cuadrático, estadísticas, tabla y CSV.

Ábrela en: https://ggeorgetoledo-collab.github.io/FisicApp/

**App Android (APK):** https://github.com/ggeorgetoledo-collab/FisicApp/releases/download/apk/FisicApp.apk

El APK se compila solo con GitHub Actions (`.github/workflows/apk.yml`) usando Capacitor: `apk/preparar.sh` arma el proyecto Android desde `index.html`, con permisos de cámara, micrófono y ubicación, ícono propio y pantalla siempre encendida. `apk/iconos.py` genera los íconos de `apk/res`.

Profesor Gonzalo George Toledo
