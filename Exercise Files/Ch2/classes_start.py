#
# Example file for working with classes
#

class myClass():
    def method1(self):
        print("myClass method 1")
    def method2(self, someString):
        print("myclass method2" + someString)

def main():
    c = myClass()
    c.method1()
    c.method2("this is a string")

if __name__ == "__main__":
    main()
