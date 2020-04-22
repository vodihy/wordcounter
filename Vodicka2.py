import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Word Counter')
    parser.add_argument("nazev", help="Napište název souboru")
    parser.add_argument("--chars", help="Vypsání znaků", action="store_true")
    parser.add_argument("--words", help="Vypsání slov", action="store_true")
    parser.add_argument("--lines", help="Vypsání řádků", action="store_true")
    args = parser.parse_args()

    try:

        if args.chars and args.words and args.lines: 
            soubor = open(args.nazev)
            text = soubor.read()
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(
                f"\n{text} \n\nPočet znaků v textu: [{znaky}] \nPočet slov v textu: [{slova}] \nPočet řádků v textu: [{radky}] \n")
            soubor.close()

        elif args.chars and args.words:
            soubor = open(args.nazev)
            text = soubor.read()
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text} \n\nPočet znaků v textu: [{znaky}] \nPočet slov v textu: [{slova}] \n")
            soubor.close()

        elif args.chars and args.lines:
            soubor = open(args.nazev)
            text = soubor.read()
            znaky = len(text)
            radky = len(text.split("\n"))
            print(f"\n{text} \n\nPočet znaků v textu: [{znaky}] \nPočet řádků v textu: [{radky}] \n")
            soubor.close()

        elif args.words and args.lines:
            soubor = open(args.nazev)
            text = soubor.read()
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text} \n\nPočet slov v textu: [{slova}] \nPočet řádků v textu: [{radky}] \n")
            soubor.close()

        elif args.chars:
            soubor = open(args.nazev)
            text = soubor.read()
            znaky = len(text)
            print(f"\n{text} \n\nPočet znaků v textu: [{znaky}]\n")
            soubor.close()

        elif args.words:
            soubor = open(args.nazev)
            text = soubor.read()
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\n\nPočet slov v textu: [{slova}] \n")
            soubor.close()

        elif args.lines:
            soubor = open(args.nazev)
            text = soubor.read()
            radky = len(text.split("\n"))
            print(f"\n{text}\n\nPočet řádků v textu: [{radky}] \n")
            soubor.close()

        else:
            soubor = open(args.nazev)
            text = soubor.read()
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(
                f"\n{text} \n\nPočet znaků v textu: [{znaky}] \nPočet slov v textu: [{slova}] \nPočet řádků v textu: [{radky}] \n")
            soubor.close()

    except PermissionError:
        print("Nemáte oprávnění k zadanému souboru")
    except:
        print("chybný soubor")

if __name__ == "__main__":
    main()