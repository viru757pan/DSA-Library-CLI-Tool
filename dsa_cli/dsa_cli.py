import argparse
from dsa_cli.services.manager import DSAManager

manager = DSAManager()

parser = argparse.ArgumentParser(description="DSA Library CLI Tool")
subparsers = parser.add_subparsers(dest="command")

# Add command
add = subparsers.add_parser("add", help="Add a new DSA solution")
add.add_argument("--title", required=True)
add.add_argument(
    "--difficulty", choices=["easy", "medium", "hard"], required=True)
add.add_argument("--tags", nargs="+", required=True)
add.add_argument("--file", required=True)

# List command
subparsers.add_parser("list", help="List all stored problems")

# Search command
search = subparsers.add_parser("search", help="Search problems")
search.add_argument("--keyword", required=True)


def main():
    args = parser.parse_args()
    if args.command == "add":
        status, msg = manager.add_problem(
            args.title, args.difficulty, args.tags, args.file)
        print(msg)

    elif args.command == "list":
        problems = manager.list_problems()

        if not problems:
            print(
                "📂 No problems found yet.\n💡 Use: dsa add --title \"...\" to add your first record.\n")
            return

        print("\n📚 Stored DSA Problems:\n")
        for idx, p in enumerate(problems, start=1):
            print(
                f"{idx}. {p['title']}  ({p['difficulty']}) | Tags: {', '.join(p['tags'])}")
        print("\n✨ End of list.\n")

    elif args.command == "search":
        results = manager.search(args.keyword)
        if results:
            for p in results:
                print(
                    f"🔍 {p['title']} - {p['difficulty']} | {', '.join(p['tags'])}")
        else:
            print("⚠ No matching records found.")
    else:
        parser.print_help()
