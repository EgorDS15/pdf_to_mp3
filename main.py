from pathlib import Path
from gtts import gTTS
import pdfplumber

# File path
file: str = r'files\text.pdf'


def pdf_to_mp3(file_path=file, language='ru'):
    """
    Create .mp3 file and .txt from pdf file
    :param file_path: path to pdf file
    :param language: choosen language of file
    """

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        with pdfplumber.PDF(open(file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        # if we have more than two pages we join all of them
        text = ''.join(pages)
        # delete all new lines
        text = text.replace('\n', '')

        # write from pdf to txt
        with open(r'results\text_file.txt', 'w') as txt_file:
            txt_file.write(text)

        # create audio and save file
        my_audio = gTTS(text=text, lang=language)
        my_audio.save(r'results\result_audio.mp3')

        return '[+] result_audio.mp3 successfully saved'
    else:
        print('No such file!')


def main():
    print(pdf_to_mp3(file))


if __name__ == '__main__':
    main()
