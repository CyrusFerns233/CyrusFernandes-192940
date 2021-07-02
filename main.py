import pyttsx3
import PyPDF2

with open('MS_41_kumar.pdf', 'rb') as book:

    full_text = ""


    reader = PyPDF2.PdfFileReader(book)
    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 150)

    for page in range(reader.numPages):

        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_text += content

    audio_reader.save_to_file(content,"MS_41_kumar.mp3")
    audio_reader.runAndWait()
