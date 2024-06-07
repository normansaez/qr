import streamlit as st
from PIL import Image
import qrcode

# Título de la aplicación
st.title("Generador de QR")

# Crear un formulario
with st.form(key='formulario'):
    # Campos del formulario
    nombre = st.text_input(label='Escribe aca tu URL para generar QR')
    # Botón para aceptar el formulario
    submit_button = st.form_submit_button(label='Aceptar')

# Acción al aceptar el formulario
if submit_button:
    
    # Datos que quieres codificar en el QR
    data = nombre
    
    # Crear una instancia de QRCode
    qr = qrcode.QRCode(
        version=1,  # Versión del código QR, controla el tamaño del QR
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
        box_size=10,  # Tamaño de cada cuadro del QR
        border=4,  # Grosor del borde
    )
    
    # Agregar datos al QR
    qr.add_data(data)
    qr.make(fit=True)
    
    # Crear una imagen del QR
    img = qr.make_image(fill='black', back_color='white')
    
    # Guardar la imagen en un archivo
    img.save("qrcode_example.png")
    image = Image.open('qrcode_example.png')
    
    # Mostrar la imagen del QR (opcional)
#    img.show()

    st.success(f"QR {nombre}. Generado con exito")
    st.image(image, caption='RQ Generado', use_column_width=True)

