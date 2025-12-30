# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re
import json

class LogParser:
    # Regex for NCSA Common/Combined Log Format
    # 127.0.0.1 - - [29/Dec/2024:12:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024 "http://ref" "Mozilla/5.0..."
    LOG_PATTERN = re.compile(
        r'(?P<host>\S+) '             # IP or Hostname
        r'(?P<identity>\S+) '         # Identity (usually -)
        r'(?P<user>\S+) '             # Remote User (usually -)
        r'\[(?P<time>.*?)\] '         # Date and Time
        r'"(?P<request>.*?)" '        # Request Line
        r'(?P<status>\d{3}) '         # Status Code
        r'(?P<size>\S+) '             # Byte Size (or -)
        r'(?:|"(?P<referer>.*?)" '    # Referer (Optional)
        r'"(?P<agent>.*?)")'          # User Agent (Optional)
    )

    @staticmethod
    def parse_line(line):
        match = LogParser.LOG_PATTERN.match(line)
        if match:
            data = match.groupdict()
            # Convert status/size to int/float if needed? Keep strings for JSON usually safer for logs unless specific need.
            # But let's simple-cast status to int.
            try:
                data['status'] = int(data['status'])
            except (ValueError, TypeError):
                pass
            
            # Handle size "-"
            if data['size'] == '-':
                data['size'] = 0
            else:
                 try:
                    data['size'] = int(data['size'])
                 except: 
                    pass
            
            return data
        return None

    @staticmethod
    def parse_file(filepath):
        results = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    parsed = LogParser.parse_line(line.strip())
                    if parsed:
                        results.append(parsed)
                    else:
                        # Optionally handle or log lines that didn't match
                        if line.strip():
                            # Include raw line if parse failed?
                            results.append({"_error": "parse_failed", "raw": line.strip()})
        except Exception as e:
            return None, str(e)
            
        return results, None

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
