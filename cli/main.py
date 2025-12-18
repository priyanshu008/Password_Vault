import argparse
import getpass
from core.vault import init_vault, add_entry, get_entry

parser = argparse.ArgumentParser(description="Secure Password Vault")
sub = parser.add_subparsers(dest="cmd")

# init command
sub.add_parser("init")

# add command
add = sub.add_parser("add")
add.add_argument("service")
add.add_argument("username")

# get command
get = sub.add_parser("get")
get.add_argument("service")

args = parser.parse_args()

if args.cmd == "init":
    master = getpass.getpass("Master password: ")
    init_vault(master)
    print("Vault initialized")

elif args.cmd == "add":
    master = getpass.getpass("Master password: ")
    password = getpass.getpass("Service password: ")
    add_entry(master, args.service, args.username, password)
    print("Entry added")

elif args.cmd == "get":
    master = getpass.getpass("Master password: ")
    entry = get_entry(master, args.service)
    print(entry if entry else "Not found")

else:
    parser.print_help()
