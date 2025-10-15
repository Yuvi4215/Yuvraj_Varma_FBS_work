# ANSI color codes
# Regular colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright colors
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Reset
RESET = "\033[0m"

# List of all colors with their names
colors = [
    ("BLACK", BLACK),
    ("RED", RED),
    ("GREEN", GREEN),
    ("YELLOW", YELLOW),
    ("BLUE", BLUE),
    ("MAGENTA", MAGENTA),
    ("CYAN", CYAN),
    ("WHITE", WHITE),
    ("BRIGHT_BLACK", BRIGHT_BLACK),
    ("BRIGHT_RED", BRIGHT_RED),
    ("BRIGHT_GREEN", BRIGHT_GREEN),
    ("BRIGHT_YELLOW", BRIGHT_YELLOW),
    ("BRIGHT_BLUE", BRIGHT_BLUE),
    ("BRIGHT_MAGENTA", BRIGHT_MAGENTA),
    ("BRIGHT_CYAN", BRIGHT_CYAN),
    ("BRIGHT_WHITE", BRIGHT_WHITE),
]

# Fixed indentation for the box
indent_outer = 50  # spaces from the left for borders
indent_inner = 65  # spaces from the left for text inside

# Horizontal line
line = "-" * 75


# Print top border
print(" " * indent_outer + line)
# Print each color with its name
for name, code in colors:
    print(" " * indent_inner + f"{code}{name}{RESET}")
# Print bottom border
print(" " * indent_outer + line)
