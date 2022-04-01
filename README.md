# Barcode & QR Code Image Generator

This Python 3 script generates PNG images of barcodes and serves them via an HTTP server.

## Install Prerequisites

### System Packages

```bash
## Zbar is in EPEL repository
dnf install zbar libjpeg-devel zlib-devel freetype-devel libpng-devel libpng python3-devel
```

### Pip Modules

```bash
python3 -m pip install -r requirements.txt --upgrade
#python3 -m pip install --compile --install-option=-O1 Pillow
```

## Run the script from a terminal

```bash
python3 main.py
```

## Build the Container Image

```bash
podman build -t barcode_image_generator .
```

## Run the Container Image

```bash
podman run --rm -it -p 8111:8111 barcode_image_generator
```
