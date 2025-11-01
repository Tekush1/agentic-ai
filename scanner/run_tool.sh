#!/usr/bin/env bash
# run_tool.sh <tool> <target> <extra_json_path>
TOOL="$1"
TARGET="$2"
EXTRA="$3"

case "$TOOL" in
  nmap) exec nmap -sV -Pn -T4 -oX - "$TARGET" ;;
  nikto) exec nikto -h "$TARGET" -o /dev/stdout -Format text ;;
  whatweb) exec whatweb --log-verbose=/dev/stdout "$TARGET" ;;
  gobuster) exec gobuster dir -u "$TARGET" -w /usr/share/wordlists/dirb/common.txt ;;
  sqlmap) exec sqlmap -u "$TARGET" --batch --output-dir=/work/sqlmap_out ;;
  *) echo "tool not allowed"; exit 2 ;;
esac
