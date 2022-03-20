from pathlib import Path
import xmltodict

DB_PATH = Path("C:/Users/Henri/AppData/Roaming/cYo/ComicRack/ComicDb.xml")

def main():
    db_ = xmltodict.parse(DB_PATH.read_text(encoding="latin1"))
    books = db_["ComicDatabase"]["Books"]["Book"]

    existing_books = {}

    for book in books:
        serie = book.get("Series", "").encode("latin1")
        number = book.get("Number")
        alt = book.get("AlternateNumber")
        title = book.get("Title", "").encode("latin1")
        if existing_book := existing_books.get(serie, {}).get(number, {}).get(alt):
            print(f'Existing {serie} - {number}/{alt} - {title} at {existing_book["@File"]}. Duplicate: {book["@File"]} ')
        elif serie:
            existing_books.setdefault(serie, {}).setdefault(number, {})[alt] = book


if __name__ == '__main__':
    main()

