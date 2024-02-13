#!/usr/bin/python3
""" 12-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)


# """ 11-main """
# from models.square import Square
#
# if __name__ == "__main__":
#
#     s1 = Square(5)
#     print(s1)
#
#     s1.update(10)
#     print(s1)
#
#     s1.update(1, 2)
#     print(s1)
#
#     s1.update(1, 2, 3)
#     print(s1)
#
#     s1.update(1, 2, 3, 4)
#     print(s1)
#
#     s1.update(x=12)
#     print(s1)
#
#     s1.update(size=7, y=1)
#     print(s1)
#
#     s1.update(size=7, id=89, y=1)
#     print(s1)
#


# """ 9-main """
# from models.square import Square
#
# if __name__ == "__main__":
#
#     s1 = Square(5)
#     print(s1)
#     print(s1.area())
#     s1.display()
#
#     print("---")
#
#     s2 = Square(2, 2)
#     print(s2)
#     print(s2.area())
#     s2.display()
#
#     print("---")
#
#     s3 = Square(3, 1, 3)
#     print(s3)
#     print(s3.area())
#     s3.display()


# """ 8-main """
# from models.rectangle import Rectangle
#
# if __name__ == "__main__":
#
#     r1 = Rectangle(10, 10, 10, 10)
#     print(r1)
#
#     r1.update(height=1)
#     print(r1)
#
#     r1.update(width=1, x=2)
#     print(r1)
#
#     r1.update(y=1, width=2, x=3, id=89)
#     print(r1)
#
#     r1.update(x=1, height=2, y=3, width=4)
#     print(r1)
#

# """ Doc """
# from models.rectangle import Rectangle
#
# if __name__ == "__main__":
#
#     r1 = Rectangle(10, 10, 10, 10)
#     print(r1)
#
#     r1.update(89)
#     print(r1)
#
#     r1.update(89, 2)
#     print(r1)
#
#     r1.update(89, 2, 3)
#     print(r1)
#
#     r1.update(89, 2, 3, 4)
#     print(r1)
#
#     r1.update(89, 2, 3, 4, 5)
#     print(r1)
#

# from models.rectangle import Rectangle
#
# if __name__ == "__main__":
#
#     r1 = Rectangle(2, 3, 2, 2)
#     r1.display()
#
#     print("---")
#
#     r2 = Rectangle(3, 2, 1, 0)
#     r2.display()
#

# from models.rectangle import Rectangle
#
# if __name__ == "__main__":
#
#     r1 = Rectangle(4, 6, 2, 1, 12)
#     print(r1)
#
#     r2 = Rectangle(5, 5, 1)
#     print(r2)
#

# from models.rectangle import Rectangle
#
# if __name__ == "__main__":
#
#     r1 = Rectangle(4, 6)
#     r1.display()
#
#     print("---")
#
#     r1 = Rectangle(2, 2)
#     r1.display()
#

# """ 3-main """
# from models.rectangle import Rectangle
#
# if __name__ == "__main__":
#
#     r1 = Rectangle(3, 2)
#     print(r1.area())
#
#     r2 = Rectangle(2, 10)
#     print(r2.area())
#
#     r3 = Rectangle(8, 7, 0, 0, 12)
#     print(r3.area())
#

# """ 1-main """
# from models.rectangle import Rectangle
#
# if __name__ == "__main__":
#
#     r1 = Rectangle(10, 2)
#     print(r1.id)
#
#     r2 = Rectangle(2, 10)
#     print(r2.id)
#
#     r3 = Rectangle(10, 2, 0, 0, 12)
#     print(r3.id)

# """ 2-main """
# from models.rectangle import Rectangle
#
# if __name__ == "__main__":
#     try:
#         Rectangle(10, "2")
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))
#
#     try:
#         r = Rectangle(10, 2)
#         r.width = -10
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))
#
#     try:
#         r = Rectangle(10, 2)
#         r.x = {}
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))
#
#     try:
#         Rectangle(10, 2, 3, -1)
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))
