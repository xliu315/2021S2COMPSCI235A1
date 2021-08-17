import pytest
from domainmodel.publisher import Publisher
#from domainmodel.Author import Author

def main():
    publisher1 = Publisher("Avatar Press")
    print(publisher1)
    publisher2 = Publisher("  ")
    print(publisher2)
    publisher3 = Publisher("  DC Comics ")
    print(publisher3)
    publisher4 = Publisher(42)
    print(publisher4)


main()