import setup, Gen_Py_Grid
import Gen_Py_Cylinder_compute

import turtle

if __name__ == "__main__":
    # Setup the window, Hint: Setup module
    # win = 

    # crate a turtle for drawing the grid
    grid_turtle = turtle.Turtle()
    grid_turtle.speed('fastest')

    # Attach to grid module
    Gen_Py_Grid.grid_turtle = grid_turtle

    # Call Part 2 code to create a grid

    # Call part 1 code to draw cylinders

    



    # Run event loop
    win.mainloop()

