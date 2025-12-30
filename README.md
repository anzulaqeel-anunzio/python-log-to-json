# Log File to JSON Parser

A tool to convert standard Apache/Nginx access logs (Common or Combined Log Format) into structured JSON data for easier analysis.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Robust Parsing**: Handles complex log lines including quoted referrers and user agents.
*   **Error Handling**: Preserves unparseable lines as raw data for inspection.
*   **Zero Dependencies**: Optimized regex-based parsing using standard libraries.

## Usage

```bash
python run_parser.py [logfile] [options]
```

### Options

*   `--output`, `-o`: Save the result to a JSON file.
*   `--pretty`, `-p`: Pretty-print the JSON output.

### Example

```bash
python run_parser.py access.log -o logs.json --pretty
```

### Supported Format
Standard Combined Log Format:
`%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"`

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
