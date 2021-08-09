class Publisher:

    def __init__(self, publisher_name):

        if publisher_name is int:
            self.__name = "N/A"

        elif publisher_name.isspace():
            self.__name = "N/A"
        elif isinstance(publisher_name, str):
            publisher_name = publisher_name.strip()
            self.__name = publisher_name

        # TODO

    @property
    def name(self) -> str:
        return self.__name


    @name.setter
    def name(self, publisher_name):
        # TODO
        if isinstance(publisher_name, str):
            self.__name = publisher_name
        elif publisher_name.isspace():
            self.__name = "N/A"
        self.__name = publisher_name


    def __repr__(self):
        # we use access via the property here
        return f'<Publisher {self.name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.name == self.name

    def __lt__(self, other):
        # TODO
        return True

    def __hash__(self):
        # TODO
        return 2
