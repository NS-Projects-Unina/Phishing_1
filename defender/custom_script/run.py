#!/usr/bin/env python3
import sys
import os
import re

SUSPICIOUS_KEYWORDS = [
    "/JavaScript",
    "/JS",
    "/OpenAction",
    "/AA",            # Additional Actions
    "/Annot",         # Annotations
    "/Launch",        # Launch action
    "/EmbeddedFile",
    "/RichMedia",
    "/XFA",
]

def scan_pdf(path):
    """
    Apre il PDF in binario e conta le occorrenze delle parole chiave sospette.
    Restituisce un dict {keyword: count}.
    """
    counts = {}
    try:
        data = open(path, "rb").read()
    except Exception as e:
        print(f"Errore aprendo {path}: {e}")
        sys.exit(1)

    for kw in SUSPICIOUS_KEYWORDS:
        cnt = len(re.findall(re.escape(kw).encode(), data))
        if cnt:
            counts[kw] = cnt
    return counts

def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <path_al_tuo_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    if not os.path.isfile(pdf_path):
        print(f"File non trovato: {pdf_path}")
        sys.exit(1)

    print(f"\n[*] Scansione PDF sospetto: {pdf_path}\n")
    results = scan_pdf(pdf_path)
    if not results:
        print("Nessuna keyword sospetta trovata.")
    else:
        print("Keyword sospette rilevate:")
        for kw, cnt in results.items():
            print(f"  {kw:<15} → {cnt} occorrenze")
    print()

if __name__ == "__main__":
    main()
