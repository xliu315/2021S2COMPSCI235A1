class Author:
    def __init__(self, authorId, author_name):
        self.coauthor_list = []
        if isinstance(authorId, int) and authorId >= 0 and authorId is not None:
            self.author_id = authorId
        else:
            raise ValueError
        if isinstance(author_name, str) and len(author_name.strip()) > 0 and author_name is not None:
            self.author_full_name = author_name
        else:
            raise ValueError

    @property
    def full_name(self):
        return self.author_full_name

    @full_name.setter
    def full_name(self, author_name):
        if isinstance(author_name, str) and len(author_name.strip()) > 0 and author_name is not None:
            self.author_full_name = author_name
        else:
            raise ValueError

    @property
    def unique_id(self):
        return self.author_id

    def __repr__(self):
        return f'<Author {self.author_full_name}, author id = {self.author_id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.author_id == self.author_id

    def __lt__(self, other):
        return self.author_id < other.author_id

    def __hash__(self):
        return hash(self.author_id)

    def add_coauthor(self, coauthor):
        if coauthor not in self.coauthor_list:
            self.coauthor_list.append(coauthor)
            coauthor.coauthor_list.append(self)

    def check_if_this_author_coauthored_with(self, name):
        return name in self.coauthor_list

