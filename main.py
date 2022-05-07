from pathlib import Path
from gtts import gTTS
import pdfplumber

file: str = r'files\text.pdf'


def pdf_to_mp3(file_path=file, language='ru'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        with pdfplumber.PDF(open(file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        with open(r'results\text_file.txt', 'w') as txt_file:
            txt_file.write(text)

        my_audio = gTTS(text=text, lang=language)
        # file_name = Path(file_path).stem
        my_audio.save(r'results\result_audio.mp3')

        return '[+] result_audio.mp3 successfully saved'
    else:
        print('No such file!')


def main():
    print(pdf_to_mp3(file))


if __name__ == '__main__':
    main()
