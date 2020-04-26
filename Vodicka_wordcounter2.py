import argparse
import requests
import sys

def main():
    muj_parser = argparse.ArgumentParser(description='WordCounter by Hynek Vodička')
    muj_parser.add_argument("stranka", help='název webové stránky')
    muj_parser.add_argument("--radky", help="spočítá řádky", action="store_true")
    muj_parser.add_argument("--slova", help="spočítá slova", action="store_true")
    muj_parser.add_argument("--znaky", help="spočítá znaky", action="store_true")

    argumenty = muj_parser.parse_args()

    try:
        if argumenty.radky and argumenty.slova and argumenty.znaky:
            web = requests.get(argumenty.stranka)
            text = web.text
            pocet_slov = text.lower().count(" ")+1+text.lower().count("\n")
            delka = len(text)
            pocet_radku = text.lower().count("\n")+1
            print(f"Vstupní text má {delka} znaků, {pocet_slov} slov a {pocet_radku} řádků.")
        elif argumenty.radky and argumenty.slova:
            web = requests.get(argumenty.stranka)
            text = web.text
            pocet_slov = text.lower().count(" ")+1+text.lower().count("\n")
            pocet_radku = text.lower().count("\n")+1
            print(f"Vstupní text má {pocet_slov} slov a {pocet_radku} řádků.")
        elif argumenty.radky and argumenty.znaky:
            web = requests.get(argumenty.stranka)
            text = web.text
            delka = len(text)
            pocet_radku = text.lower().count("\n")+1
            print(f"Vstupní text má {delka} znaků a {pocet_radku} řádků.")
        elif argumenty.slova and argumenty.znaky:
            web = requests.get(argumenty.stranka)
            text = web.text
            pocet_slov = text.lower().count(" ")+1+text.lower().count("\n")
            delka = len(text)
            print(f"Vstupní text má {delka} znaků a {pocet_slov} slov.")
        elif argumenty.slova:
            web = requests.get(argumenty.stranka)
            text = web.text
            pocet_slov = text.lower().count(" ")+1+text.lower().count("\n")
            print(f"Vstupní text má {pocet_slov} slov.")
        elif argumenty.radky:
            web = requests.get(argumenty.stranka)
            text = web.text
            pocet_radku = text.lower().count("\n")+1
            print(f"Vstupní text má {pocet_radku} řádků.")
        elif argumenty.znaky:
            web = requests.get(argumenty.stranka)
            text = web.text
            delka = len(text)
            print(f"Vstupní text má {delka} znaků.")
        else:
            web = requests.get(argumenty.stranka)
            text = web.text
            pocet_slov = text.lower().count(" ")+1+text.lower().count("\n")
            delka = len(text)
            pocet_radku = text.lower().count("\n")+1
            print(f"Vstupní text má {delka} znaků, {pocet_slov} slov a {pocet_radku} řádků.")
    except FileNotFoundError:
        print("Soubor neexistuje")
        sys.exit()
    except PermissionError:
        print("nemám práva k souboru")
        sys.exit()

if __name__ == '__main__':
    main()