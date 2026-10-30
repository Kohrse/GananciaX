# GananciaX (APK para Android)

App de ventas, gastos, productos, clientes y fiados. Los datos se guardan en el propio teléfono.

## Cómo obtener el APK
1. Crea un repositorio en GitHub y sube **todo el contenido** de esta carpeta (incluida la carpeta oculta `.github`).
2. Entra en la pestaña **Actions**. El flujo "Construir APK" arranca solo al subir los archivos (o pulsa **Run workflow**). Tarda unos 5 a 10 minutos.
3. Cuando termine, descarga `GananciaX.apk` desde **Releases** (columna derecha del repositorio) o desde el apartado *Artifacts* de la ejecución.
4. En el Android, abre el APK y permite "instalar apps de orígenes desconocidos" si lo pide.

## Notas
- El APK es de depuración: se instala sin problema, pero no sirve para Google Play (ahí haría falta un APK/AAB firmado con tu llave).
- Los datos son locales: no se sincronizan entre dispositivos. Usa Datos > Exportar copia para respaldarlos.
- Si cambias el icono, reemplaza `assets/icon.png` (cuadrado, con esquinas transparentes).
- La app web está en `www/index.html`.
