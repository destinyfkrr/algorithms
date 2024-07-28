class Stack:
    def __init__(self):
        self.items = []
        self.max_size = 5

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.max_size

    def push(self, item):
        if self.is_full():
            print("The stack is full. Cannot add more items.")
        else:
            self.items.append(item)
            print(f"'{item}' has been added to the stack.")
        self.display()

    def pop(self):
        if self.is_empty():
            print("The stack is empty. Nothing to pop.")
        else:
            removed_item = self.items.pop()
            print(f"'{removed_item}' has been removed from the stack.")
        self.display()

    def peek(self):
        if self.is_empty():
            return "The stack is empty."
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        max_width = 20
        print("\nStack contents:")
        print("+" + "-" * max_width + "+")
        for _ in range(self.max_size - len(self.items)):
            print("|" + " " * max_width + "|")
            print("|" + "-" * max_width + "|")
        for item in reversed(self.items):
            print("|" + item.center(max_width) + "|")
            print("|" + "-" * max_width + "|")
        print("+" + "-" * max_width + "+")
        print(f"Stack size: {self.size()}\n")

# Function to display the menu and take user input
def menu():
    stack = Stack()
    while True:
        print("Stack Operations Menu:")
        print("1. Push (Add an item)")
        print("2. Pop (Remove the top item)")
        print("3. Peek (View the top item)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            stack.push(item)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            print(f"Top item: {stack.peek()}")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()