#!/usr/bin/env python3

import subprocess

# Create epub
cmd = 'pandoc -o walk.epub walk.md -s -S --epub-chapter-level=3'
cmd = cmd.split()
results = subprocess.check_output(cmd)
print(str(results, encoding='UTF-8'))

