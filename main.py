from my_modules import area
'''
    1)It is a one of the way to import modules
    
    2)import my_modules.area as a
        print(a.area_circle(3))
        This will also work.
        You can put any variable in place of "a".
        
    3)import sys
      sys.path.append("C:\\....")
      
      import area as a
      print(a.area_circle(3))
      Use this when the module is in seperate directory
'''

print("Area of Circle is ", area.area_circle(3))
print(f"Area of Square is {area.area_square(3)}")