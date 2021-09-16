'''
google_images_download nie działa

Instalujemy bibliotekę tqdm wykorzystując PyCharm lub wykonując polecenie w terminalu:
pip install tqdm

Klonujemy repozytorium:
git clone https://github.com/ultralytics/google-images-download

Przechodzimy do katalogu google-images-download:
cd google-images-download

Wykonujemy polecenie:
python bing_scraper.py --search "horse" --limit 10 --download --chromedriver D:\Pobrane\chromedriver_win32\chromedriver.exe

Po --search podajemy termin o jaki chcemy zapytać, po --limit limit zdjęć do pobrania oraz po --chrmedriver odpowiednią ścieżkę do chromedriver.exe
chromedriver pobieramy z https://chromedriver.chromium.org/downloads

Pobrane zdjęcia (pobieranie zakończone sukcesem) będą znajdować się w katalogu:
google-images-download\images\horse

'''
