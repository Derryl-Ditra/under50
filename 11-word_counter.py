"""Word counting utility for Under 50 triage briefs.

Rules:
- Whitespace-separated tokens.
- Hyphenated compounds (e.g. '14-month') count as one token.
- Markdown markers (bullet dashes, heading hashes, numbered list prefixes, blockquote markers) are excluded.
- Punctuation attached to words (commas, periods, semicolons, parens) is not separated into distinct tokens.
"""

import re
from typing import List


def extract_tokens(text: str) -> List[str]:
    """Extract word tokens from markdown brief text according to Under 50 rules."""
    tokens: List[str] = []
    
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        
        # Remove markdown heading markers at the beginning of the line (e.g., '# ', '## ')
        line = re.sub(r"^(?:#{1,6}\s+)", "", line)
        
        # Remove blockquote markers (e.g., '> ')
        line = re.sub(r"^(?:>\s+)+", "", line)
        
        # Remove bullet markers: '-', '*', '+' followed by whitespace
        line = re.sub(r"^(?:[-*+]\s+)", "", line)
        
        # Remove ordered list markers (e.g., '1. ', '10. ')
        line = re.sub(r"^(?:\d+\.\s+)", "", line)
        
        # Split on whitespace
        line_tokens = [tok for tok in line.split() if tok]
        tokens.extend(line_tokens)
        
    return tokens


def count_words(text: str) -> int:
    """Return the total token count for a markdown brief."""
    return len(extract_tokens(text))
