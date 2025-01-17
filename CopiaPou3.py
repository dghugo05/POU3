from Dependencias.importaciones import *

ruta_actual = Path(sys.argv[0]).resolve().parent
dependencia = "Dependencias"
r_multimedia = r"Dependencias\multimedia"
script = "copy.ps1"
dir_list = "Lista.txt"
dir_listn = "Lista_negra.txt"


ruta_dependencia = os.path.join(ruta_actual,dependencia)
directorio_imagen = os.path.join(ruta_actual,r_multimedia)
lista_multimedia = os.listdir(directorio_imagen)
script_path = os.path.join(ruta_dependencia,script)
ruta_lista = os.path.join(ruta_dependencia, dir_list)
ruta_lista_negra = os.path.join(ruta_dependencia, dir_listn)

with open (ruta_lista_negra, "r") as file:
    list_items = file.read()
    lista_negra = list_items.splitlines()
with open(ruta_lista, "r") as file:
    list_items = file.read()
    lista = list_items.splitlines()

def num_atleatorio():
    num_atleatorio = randint(1, 30)


def temporizador():
    tiempo_espera = 15
    temporizador = threading.Timer(tiempo_espera, abrir)
    temporizador.start()

def copiar():
    try:
        subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-file", script_path], check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script: {e}")


def abrir():
    temporizador()
    archivos_de_imagenes = [archivo for archivo in lista_multimedia if archivo.endswith('.jpg') or archivo.endswith('.png') or archivo.endswith(".mp4")]
    multimedia = random.choice(archivos_de_imagenes)
    ruta_imagen_atleatoria = os.path.abspath(os.path.join(directorio_imagen, multimedia))
    if multimedia.endswith(".jpg") or multimedia.endswith(".png"):
        imagen = cv2.imread(ruta_imagen_atleatoria)
        cv2.imshow('Imagen Abierta', imagen)
        hwnd = ctypes.windll.user32.FindWindowW(None, 'Imagen Abierta')
        ctypes.windll.user32.SetForegroundWindow(hwnd)
        ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)
        cv2.waitKey(0)  
        cv2.destroyAllWindows()  
    else:

        video_clip = VideoFileClip(ruta_imagen_atleatoria)
        audio_clip = video_clip.audio

        audio_clip_file = f"temp_audio_{int(time.time())}.mp3"

        if os.path.exists(audio_clip_file):
            os.remove(audio_clip_file)

        audio_clip.write_audiofile(audio_clip_file)
        pygame.mixer.init()
        pygame.mixer.music.load(audio_clip_file)
        pygame.mixer.music.play()  

        cap = cv2.VideoCapture(ruta_imagen_atleatoria)

        video_terminado = False

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video Abierto', frame)
            if not pygame.mixer.music.get_busy():
                video_terminado = True
            hwnd = ctypes.windll.user32.FindWindowW(None, 'Imagen Abierta')
            ctypes.windll.user32.SetForegroundWindow(hwnd)
            ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)
            cv2.waitKey(int(1000 / video_clip.fps))
        pygame.mixer.music.stop()
        cap.release()
        audio_clip.close()

        pygame.mixer.quit()
        try:
            os.remove(audio_clip_file)
        except OSError as e:
            print(f"Error al intentar eliminar el archivo: {e}")
    cv2.destroyAllWindows()


def resultado():
    clave = int(input("Debes introducir la clave, la cuál es un número comprendido del 1 al 30: "))
    cont = 13
    if clave > 30 or clave <= 0:
        print("Debe introducir un número del 1 al 30")
        cont -= 1
        resultado()
    else:
        while True:
            if clave == num_atleatorio:
                break
            else: 
                cont -= 1
                if cont != 0 and cont > 0 :
                    abrir()
                    print("Números de intentos restantes hasta que te empiece a joder", cont)
                    clave = int(input("Vuelve a intentar: "))
                else:
                    if clave > 30 or clave <= 0:
                        print("El número introducido debe ser un número del 1 al 30")
                    else:
                        for item in lista_negra:
                            abrir()
                            clave = int(input("Vuelve a intentar: "))
                

temporizador()
copiar()
resultado()