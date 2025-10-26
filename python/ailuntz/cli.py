#!/usr/bin/env python3
"""
Ailuntz Personal CV CLI Tool
"""

import sys


def print_cv():
    """Display personal CV information in a colorful and elegant way."""

    # ANSI color codes
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    RED = "\033[91m"

    # Border characters
    border = "═" * 60

    cv_content = f"""
{CYAN}{BOLD}{border}{RESET}
{CYAN}{BOLD}                    ✨ AILUNTZ - CV ✨{RESET}
{CYAN}{BOLD}{border}{RESET}

{MAGENTA}{BOLD}👤 Name:{RESET}          {YELLOW}Ailuntz{RESET}
{MAGENTA}{BOLD}💼 Title:{RESET}         {YELLOW}Full Stack Developer{RESET}
{MAGENTA}{BOLD}📍 Location:{RESET}      {YELLOW}China{RESET}
{MAGENTA}{BOLD}📧 Email:{RESET}         {YELLOW}ailuntz@icloud.com{RESET}
{MAGENTA}{BOLD}🔗 Website:{RESET}       {YELLOW}https://ailuntz.com{RESET}

{CYAN}{BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}

{GREEN}{BOLD}💻 SKILLS{RESET}
  {BLUE}•{RESET} Languages:     Python, JavaScript, TypeScript, Go
  {BLUE}•{RESET} Frontend:      React, Vue.js, Next.js, Tailwind CSS
  {BLUE}•{RESET} Backend:       Node.js, Django, FastAPI, Express
  {BLUE}•{RESET} Database:      PostgreSQL, MongoDB, Redis
  {BLUE}•{RESET} DevOps:        Docker, Kubernetes, CI/CD, AWS
  {BLUE}•{RESET} Tools:         Git, Linux, Nginx, Vim

{CYAN}{BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}

{GREEN}{BOLD}🎓 EDUCATION{RESET}
  {BLUE}•{RESET} Computer Science & Technology
  {BLUE}•{RESET} Focus on Software Engineering & AI

{CYAN}{BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}

{GREEN}{BOLD}🚀 PROJECTS{RESET}
  {BLUE}•{RESET} CLI Tools:     Personal command-line utilities
  {BLUE}•{RESET} Web Apps:      Full-stack web applications
  {BLUE}•{RESET} Open Source:   Contributing to various projects

{CYAN}{BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}

{RED}{BOLD}💡 INTERESTS{RESET}
  {BLUE}•{RESET} AI & Machine Learning
  {BLUE}•{RESET} System Design & Architecture
  {BLUE}•{RESET} Developer Tools & CLI Applications
  {BLUE}•{RESET} Open Source Community

{CYAN}{BOLD}{border}{RESET}
{CYAN}{BOLD}            💌 Thanks for checking out my CV!{RESET}
{CYAN}{BOLD}{border}{RESET}
"""

    print(cv_content)


def show_help():
    """Display help message."""
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    help_text = f"""
{CYAN}{BOLD}Ailuntz CLI - Personal CV Tool{RESET}

Usage:
  {GREEN}ailuntz cv{RESET}      Display CV
  {GREEN}ailuntz --help{RESET}  Show this help message

Examples:
  {YELLOW}ailuntz cv{RESET}
    """
    print(help_text)


def main():
    """Main entry point for the CLI."""
    try:
        # Get command line arguments
        args = sys.argv[1:]

        if not args or args[0] == 'cv':
            print_cv()
            return 0
        elif args[0] in ['--help', '-h', 'help']:
            show_help()
            return 0
        else:
            print(f"Unknown command: {args[0]}", file=sys.stderr)
            print("Run 'ailuntz --help' for usage information.")
            return 1

    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
