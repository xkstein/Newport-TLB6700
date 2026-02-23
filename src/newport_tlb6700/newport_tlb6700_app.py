import argparse

from newport_tlb6700.version import __version__  # noqa


def main():
    parser = argparse.ArgumentParser(
        prog="newport-tlb6700",
        description=(
            "Unofficial Newport Velocity TLB6700 tunable laser python driver\n\n"
            "For more information, visit: "
            "https://github.com/xkstein/newport-tlb6700/"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the program's version number and exit",
    )

    args = parser.parse_args()

    if args.version:
        print(f"newport-tlb6700 {__version__}")
    else:
        # Default behavior when no arguments are given
        parser.print_help()


if __name__ == "__main__":
    main()
