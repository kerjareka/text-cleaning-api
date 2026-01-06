import re
import emoji
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Download NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Stopword Bahasa Indonesia
stop_words = set(stopwords.words('indonesian'))

# Stemmer Bahasa Indonesia
factory = StemmerFactory()
stemmer = factory.create_stemmer()


def clean_text(text: str) -> str:
    """
    Membersihkan teks mentah Bahasa Indonesia
    agar siap digunakan untuk model NLP.
    """
    # 1. Lowercase
    text = text.lower()

    # 2. Hapus URL
    text = re.sub(r'http\S+|www\S+', '', text)

    # 3. Hapus emoji
    text = emoji.replace_emoji(text, replace='')

    # 4. Hapus karakter selain huruf
    text = re.sub(r'[^a-z\s]', '', text)

    # 5. Tokenisasi
    tokens = word_tokenize(text)

    # 6. Hapus stopword
    tokens = [word for word in tokens if word not in stop_words]

    # 7. Stemming
    tokens = [stemmer.stem(word) for word in tokens]

    # 8. Gabung kembali token
    cleaned_text = ' '.join(tokens)

    return cleaned_text


if __name__ == "__main__":
    print(clean_text("SELAMAT!!! Anda MENANG 50JT 🎉"))
