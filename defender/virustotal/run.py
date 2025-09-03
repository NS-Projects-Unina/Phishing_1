#!/usr/bin/env python3
import sys
import os
import time
import hashlib
import json
from vt import Client
from vt.error import APIError

API_KEY_ENV = "VT_API_KEY"
POLL_INTERVAL = 15  # seconds

def sha256sum(path):
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def print_report(file_obj, file_hash):
    stats = file_obj.last_analysis_stats
    results = file_obj.last_analysis_results

    print(f"\n=== REPORT for {file_hash} ===")
    print("Detection stats:")
    for category, count in stats.items():
        print(f"  {category.capitalize():<15}: {count}")
    print(f"\nPermalink: https://www.virustotal.com/gui/file/{file_hash}/detection\n")
    print("Engines flags:")
    for engine, detail in results.items():
        if detail["category"] != "undetected":
            print(f"  • {engine}: {detail['category']}")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    if not os.path.isfile(pdf_path):
        print(f"Error: file not found: {pdf_path}")
        sys.exit(1)

    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        print(f"Error: set your API key in environment variable {API_KEY_ENV}")
        sys.exit(1)

    file_hash = sha256sum(pdf_path)
    print(f"SHA256: {file_hash}")

    with Client(api_key) as client:
        try:
            file_obj = client.get_object(f"/files/{file_hash}")
            print("[*] Using existing analysis")
        except APIError as e:
            if e.code == "NotFoundError":
                print("[*] File not known, uploading for scan...")
                analysis = client.scan_file(open(pdf_path, "rb"), wait_for_completion=True)
                print("[*] Analysis completed")
                file_obj = client.get_object(f"/files/{file_hash}")
            else:
                print(f"API error: {e.code} - {e.message}")
                sys.exit(1)

        print_report(file_obj, file_hash)

if __name__ == "__main__":
    main()
