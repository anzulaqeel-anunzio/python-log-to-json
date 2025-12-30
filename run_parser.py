# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os
import json

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from parser.core import LogParser

def main():
    parser = argparse.ArgumentParser(description="Apache/Nginx Log to JSON Parser")
    parser.add_argument("file", help="Input log file (access.log)")
    parser.add_argument("--output", "-o", help="Output JSON file")
    parser.add_argument("--pretty", "-p", action="store_true", help="Pretty print JSON output")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)

    print(f"Parsing '{args.file}'...")
    data, error = LogParser.parse_file(args.file)

    if error:
        print(f"Error parsing file: {error}")
        sys.exit(1)

    indent = 4 if args.pretty else None
    json_output = json.dumps(data, indent=indent)

    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(json_output)
            print(f"Parsed {len(data)} lines. Output saved to {args.output}")
        except Exception as e:
            print(f"Error writing output: {e}")
            sys.exit(1)
    else:
        print(json_output)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
