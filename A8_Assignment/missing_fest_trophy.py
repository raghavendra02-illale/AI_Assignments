
class Player:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to {self.name}'s bag.")

    def check_item(self, item):
        return item in self.items

    def display_items(self):
        print("Collected Items:", self.items)


class Place:
    def __init__(self, name, item=None, locked=False, required_item=None):
        self.name = name
        self.item = item
        self.locked = locked
        self.required_item = required_item

    def enter(self, player):
        if self.locked and not player.check_item(self.required_item):
            print(f"Access denied! {self.required_item} is required.")
            return

        print(f"Welcome to {self.name}.")

        if self.item is not None:
            player.add_item(self.item)
            self.item = None


class Chest:
    def __init__(self, password):
        self.password = password
        self.is_open = False

    def unlock(self, code):
        if code == self.password:
            self.is_open = True
            print("Congratulations! You found the Missing Fest Trophy!")
        else:
            print("Wrong code! The chest remains closed.")


def failed_route():
    print("\n--- FAILED ATTEMPT ---")

    player = Player("Raghu")

    lab = Place("Computer Lab", "secret code 4821", True, "key")
    stage = Place("Main Stage", locked=True, required_item="secret code 4821")
    chest = Chest("4821")

    lab.enter(player)
    stage.enter(player)

    player.display_items()
    chest.unlock("1234")


def winning_route():
    print("\n--- SUCCESSFUL ATTEMPT ---")

    player = Player("Raghu")

    canteen = Place("Canteen", "key")
    lab = Place("Computer Lab", "secret code 4821", True, "key")
    stage = Place("Main Stage", locked=True, required_item="secret code 4821")
    chest = Chest("4821")

    canteen.enter(player)
    lab.enter(player)
    stage.enter(player)

    player.display_items()
    chest.unlock("4821")


if __name__ == "__main__":
    failed_route()
    winning_route()
