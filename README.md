# Threat Intelligence Automation using STIX

## Overview

This project is a Python-based threat intelligence automation pipeline that processes STIX (Structured Threat Information eXpression) data to extract Indicators of Compromise (IOCs), analyze the MITRE ATT&CK framework, enrich IPv4 indicators with contextual information, and generate structured reports for threat analysis.

The project demonstrates how threat intelligence data can be automated into a reusable workflow for cybersecurity analysis.

---

## Project Highlights

- Processed STIX 2.x threat intelligence bundles.
- Parsed the MITRE ATT&CK Enterprise STIX dataset.
- Extracted IOCs including IPv4 addresses, domains, and URLs.
- Enriched IPv4 indicators with contextual information.
- Generated structured CSV reports and summary outputs using a modular Python pipeline.

## Features

- Parse STIX 2.x threat intelligence bundles
- Process the MITRE ATT&CK Enterprise STIX dataset
- Extract Indicators of Compromise (IOCs)
  - IPv4 Addresses
  - Domain Names
  - URLs
- Extract MITRE ATT&CK attack patterns
- Extract malware information
- Enrich IPv4 indicators with contextual information
  - Country
  - City
  - Organization
- Export extracted data into CSV reports
- Generate an automated summary report
- Modular Python project structure

---

## Project Structure

```
Threat-Intel-Automation/
│
├── data/
│   ├── sample_stix.json
│   └── enterprise_attack.json
│
├── reports/
│   ├── attack_patterns.csv
│   ├── malware.csv
│   ├── ioc_report.csv
│   └── summary.txt
│
├── scripts/
│   ├── main.py
│   ├── parser.py
│   ├── exporter.py
│   ├── ioc_parser.py
│   ├── enricher.py
│   ├── logger.py
│   ├── summary.py
│   └── download_feed.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Workflow

```
STIX Bundle
     │
     ▼
Load STIX Data
     │
     ▼
Extract Indicators of Compromise
(IPs, Domains, URLs)
     │
     ▼
Extract MITRE ATT&CK Data
     │
     ▼
Enrich IPv4 Indicators
     │
     ▼
Generate CSV Reports
     │
     ▼
Generate Summary Report
```

---

## Technologies Used

- Python 3
- STIX 2.x
- MITRE ATT&CK Framework
- JSON
- Pandas
- Requests

---

## Installation

Clone the repository

```bash
git clone https://github.com/sakshi2070/Threat-Intel-Automation.git
```

Navigate into the project

```bash
cd Threat-Intel-Automation
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate the virtual environment

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## Usage

Run the automation pipeline

```bash
python scripts/main.py
```

---

## Output

The project generates the following reports inside the **reports/** directory:

- **attack_patterns.csv** – Extracted MITRE ATT&CK techniques
- **malware.csv** – Extracted malware information
- **ioc_report.csv** – Extracted and enriched Indicators of Compromise
- **summary.txt** – Summary of the processed threat intelligence data

---

## Skills Demonstrated

- Threat Intelligence
- STIX 2.x
- MITRE ATT&CK
- IOC Extraction
- IOC Enrichment
- Python Automation
- JSON Parsing
- Data Processing
- CSV Report Generation
- Modular Programming

---

## Future Improvements

- Support additional STIX object types
- Process multiple STIX bundles automatically
- Integrate live TAXII threat intelligence feeds
- Scheduled automated threat feed updates
- SIEM integration for automated IOC ingestion

---

## Disclaimer

This project was developed for educational purposes to demonstrate the automation of threat intelligence processing using STIX-formatted data and the MITRE ATT&CK framework.
