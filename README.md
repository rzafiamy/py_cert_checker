# SSL Certificate Expiry Checker

This Python script checks the SSL certificate expiration for a list of domains provided in a text file. It uses `certifi` to handle SSL certificate verification and `tabulate` to print the results in a neatly formatted table. The script helps in monitoring and alerting for certificates that are close to expiry or have already expired.

## Installation

To run this script, you need Python 3 and pip installed. You can then install the required dependencies with pip:

```bash
pip install certifi tabulate
```

## Usage

1. Prepare a plain text file containing the domain names to check, with one domain per line. For example:

```
example.com
expired.badssl.com
```

2. Run the script by passing the path to your file as an argument:

```bash
python ssl_check.py path/to/your/domains.txt
```

Or just use the script `run.sh`, it will generate a file called `report.dat`

```bash
./run.sh
```

The script will output the SSL certificate status for each domain in a table format, indicating whether the certificate is valid, expired, or if the SSL check failed, along with the days remaining or overdue.

## Example Output

```
+----------------------+--------+-----------------------+
| Domain               | Status | Days Remaining/Overdue |
+----------------------+--------+-----------------------+
| example.com          | Valid  | 90                     |
| expired.badssl.com   | Expired| -5                     |
| invalid.domain       | SSL check failed - [Errno ...] |
+----------------------+--------+-----------------------+
```

## Contributing

Feel free to fork the repository and submit pull requests to add features or fix bugs.

## License

MIT License

Copyright (c) 2024 RZL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
