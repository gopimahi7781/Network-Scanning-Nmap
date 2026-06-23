# Network Scanning Using Nmap

## Objective
Perform network reconnaissance and identify open ports and services.

## Tools Used
- Kali Linux
- Nmap

## Command Used

```bash
nmap -F scanme.nmap.org
## Findings

- Identified open ports 21 (FTP), 22 (SSH), and 80 (HTTP)
- Detected OpenSSH service version
- Detected Apache HTTP Server version
- Gathered basic operating system information
- Performed network reconnaissance using Nmap

## Additional Commands Used

```bash
nmap -F scanme.nmap.org
nmap -F -sV scanme.nmap.org
