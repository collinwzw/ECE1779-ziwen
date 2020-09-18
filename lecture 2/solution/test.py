# Question 4


# We provide class Rectangle and starter code for class RectangleCollection.

# Complete class RectangleCollection, which has one list instance variable, rectangles,
# that should initially refer to an empty list. Write a method add_rectangle that takes a Rectangle as a parameter and appends it to the rectangles list.
# Write a method get_same_area_rects that takes a number as a parameter and returns a list of all Rectangles from the rectangles list that have that area.


from typing import List


class Rectangle:
    """ A rectangle with a width and height. """

    def __init__(self, w: int, h: int) -> None:
        # """Create a new rectangle of width w and height h.

        # >>> r = Rectangle(1, 2)
        # >>> r.width
        # 1
        # >>> r.height
        # 2
        # """

        self.width = w
        self.height = h

    def get_area(self) -> int:
        # """Return the area of this rectangle.

        # >>> r = Rectangle(10, 20)
        # >>> r.get_area()
        # 200
        # """

        return self.width * self.height


class RectangleCollection:

    def __init__(self) -> None:
        # """
        # >>> rc = RectangleCollection()
        # >>> rc.rectangles
        # []
        # """
        self.rectangles = []
        
    def add_rectangle(self, r:"Rectangle") -> None:
        self.rectangles.append(r)
    
    
    def get_same_area_rects(self, areaNumber) -> List[Rectangle]:
        result = []
        for rectangle in self.rectangles:
            if rectangle.get_area() == areaNumber:
                result.append(rectangle)
                
        
        return result
            
            
            

	
rc = RectangleCollection(); 
r1 = Rectangle(10, 20); 
r2 = Rectangle(15, 20); 
r3 = Rectangle(20, 10); 
rc.rectangles.extend([r1, r2, r3]); 
print(rc.rectangles)
res = rc.get_same_area_rects(200); 
#res == [r1, r3]
print(res)