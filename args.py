import argparse, os


DESCRIPTION = "Simple Malware Scanner"

def setup_argument_parser() -> argparse.ArgumentParser:
    os.environ.setdefault("COLUMNS", "100")
    
    parser = argparse.ArgumentParser(
        prog="malware_scanner",
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-scd",
        "--scan_current_directory",
        help="Scan the current directory the program is in",
    )
    parser.add_argument(
        "-s",
        "--scan_directory",
        help="Scan a directory with a path provided as an argument",
    )

def parse_args(argv = None) -> argparse.Namespace:
    parser = setup_argument_parser()
    args = parse_args(argv=argv)