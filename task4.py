def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me the command and arguments."
        except KeyError:
            return "This contact does not exist."
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return inner

def parse_input(user_input: str):
    """Parse user input into command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts: dict):
    """Add a new contact."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts: dict):
    """Change an existing contact's phone number."""
    name, phone = args
    existing_phone = contacts.get(name)
    if not existing_phone:
        return f"Contact with name {name} does not exist."
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts: dict):
    """Show a contact's phone number."""
    [name] = args
    existing_phone = contacts.get(name)
    if not existing_phone:
        return f"Contact with name {name} does not exist."
    return existing_phone

@input_error
def show_all(contacts: dict):
    """Show all contacts."""
    if not contacts:
        return "There are no contacts in the list."
    result = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(result)

def main():
    print("Welcome to the assistant bot!")
    print("Type 'hello' to start or 'exit' to quit.")
    contacts = {}

    while True:
        user_input = input("Enter command: ").strip()
        if not user_input:
            continue  

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print("Enter the argument for the command (name and phone):")
            user_input = input("Enter command: ").strip()
            command, *args = parse_input(user_input)
            print(add_contact(args, contacts))
        elif command == 'change':
            print("Enter the argument for the command (name and phone):")
            user_input = input("Enter command: ").strip()
            command, *args = parse_input(user_input)
            print(change_contact(args, contacts))
        elif command == 'phone':
            print("Enter the argument for the command (name):")
            user_input = input("Enter command: ").strip()
            command, *args = parse_input(user_input)
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()