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
        "-s",
        "--scan_directory",
        dest= "scan_directory",
        help="Scan a directory with a path provided as an argument. Make sure to put quotes around the path. Defaults to current directory if not provided",
    )
    return parser

def parse_args(argv = None) -> argparse.Namespace:
    parser = setup_argument_parser()
    args = parser.parse_args(args=argv)
    
    args.directory = os.getcwd() if args.scan_directory is None else args.scan_directory
    
    return args