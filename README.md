# Greenpeace Chile - Hazte Socio/a

Landing page para la selección de planes de suscripción de Greenpeace Chile. Los usuarios eligen un plan y son redirigidos a VirtualPOS para completar el proceso de pago.

## URL de producción

```
https://greenpeace-cl.github.io/hazte-socio/
```

## Estructura del proyecto

```
├── index.html          # Página principal
├── styles.css          # Estilos (CSS puro)
├── assets/
│   ├── logo.svg        # Logo de Greenpeace
│   ├── favicon.ico     # Favicon
│   └── qr-hazte-socio.png  # Código QR generado
└── scripts/
    └── generate_qr.py  # Script para generar QR
```

## Desarrollo local

Abrir `index.html` directamente en el navegador o usar un servidor local:

```bash
# Python 3
python3 -m http.server 8000

# Luego abrir http://localhost:8000
```

## Generar código QR

```bash
# Instalar dependencias
pip install -r requirements.txt

# Generar QR con URL por defecto
python3 scripts/generate_qr.py

# Generar QR con URL personalizada
python3 scripts/generate_qr.py --url https://ejemplo.com --out assets/mi-qr.png
```

## Despliegue

El sitio se despliega automáticamente en GitHub Pages desde la rama `main`.

## Configuración de planes

Los planes actualmente usan URLs placeholder. Para configurar los planes reales, edita las URLs en `index.html`:

```html
<a href="https://suscripcion-pat.virtualpos.cl/greenpeace/PLAN_HASH">Elegir plan</a>
```

Reemplaza `PLAN_HASH` con el hash proporcionado por VirtualPOS para cada plan.

## Tecnologías

- HTML5 semántico
- CSS3 (sin frameworks)
- Sin JavaScript
- Diseño responsive (mobile-first)
- Accesible (ARIA, skip links)
