#!/usr/bin/env python3
"""Anuncia conclusão via Voice Monkey (variação do script local)."""
import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

API_URL = "https://api-v3.voicemonkey.io/announce"
DEFAULT_TOKEN = "PUT YOUR TOKEN HERE"
DEFAULT_DEVICE = "PUT YOUR DEVICE CODE HERE"
DEFAULT_LANGUAGE = "pt-BR"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("speech", nargs="?", default="A tarefa foi concluída com sucesso.")
    parser.add_argument("--device", default=DEFAULT_DEVICE)
    parser.add_argument("--language", default=DEFAULT_LANGUAGE)
    parser.add_argument("--token", default=DEFAULT_TOKEN)
    args = parser.parse_args()

    payload = {"token": args.token, "device": args.device, "speech": args.speech.strip(), "language": args.language}
    req = urllib.request.Request(API_URL, data=json.dumps(payload).encode("utf-8"),
                                 headers={"Content-Type": "application/json", "Accept": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(resp.read().decode("utf-8", "replace"))
            return 0
    except Exception as exc:
        print(json.dumps({"success": False, "error": str(exc)}, ensure_ascii=False))
        return 1

if __name__ == "__main__":
    sys.exit(main())
