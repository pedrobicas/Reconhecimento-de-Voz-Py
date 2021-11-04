# ---Instalação das bibliotecas---
# Instalar o SpeechRecognition: pip install SpeechRecognition
# Instalar o PyAudio: pip install pyaudio

# ---Erro do PyAudio--
# Ver versão do PYTHON e do AMD 64 ou win 32 
# Instalar o PyAudio manualmente de acordo com sua versão
# Link: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# Instalar o PyAudio novamente: pip install CaminhdoDoArquivoBaixado

# Importando o Speech Recognition
import speech_recognition as sr
# Importando o gtts e o PlaySound
from gtts import gTTS
from playsound import playsound

#Funcao responsavel por falar 
def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br')
    #Salva o arquivo de audio
    tts.save('audio.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('audio.mp3')



# Usando o microfone usuario
# Habilita o microfone do usuario
def ouvir_microfone():
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        #Frase para o usuario dizer algo
        print("Fale alguma coisa:")
        #Armazena o que foi dito numa variavel
        audio = rec.listen(mic)

    try:
        #Passa a variável para o algoritmo reconhecedor de padroes
        texto = rec.recognize_google(audio,language='pt-BR')
        
        #Retorna a frase pronunciada
        print("Você disse: " + texto)
            
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")

    return texto

texto = ouvir_microfone()
cria_audio(texto)

        
        