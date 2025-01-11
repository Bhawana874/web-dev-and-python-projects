import tkinter as tk
import math

# Parameters
num_circles = 4           # Number of circles
circle_min_radius = 10     # Minimum radius of circles
circle_max_radius = 30     # Maximum radius of circles
animation_speed = 50       # Milliseconds per frame

# Initialize the main tkinter window
root = tk.Tk()
root.title("Voice Assistant Animation")

# Create a Frame to hold the Canvas, and place it using grid layout
frame = tk.Frame(root, width=200, height=200, bg="white")
frame.grid(row=0, column=0, padx=20, pady=20)
frame.grid_propagate(False)  # Prevent the frame from resizing

# Create a Canvas widget inside the frame
canvas = tk.Canvas(frame, width=200, height=200, bg="white")
canvas.pack(fill="both", expand=True)

# Initialize circles centered at (100, 100) on the canvas
circles = []
for i in range(num_circles):
    circle = canvas.create_oval(100 - circle_min_radius, 100 - circle_min_radius,
                                100 + circle_min_radius, 100 + circle_min_radius,
                                outline="blue", width=2)
    circles.append(circle)

# Animation update function
def animate(frame=0):
    for i, circle in enumerate(circles):
        # Calculate current radius with a sine wave to create pulsing effect
        radius = circle_min_radius + (math.sin(frame / 10 + i) + 1) * (circle_max_radius - circle_min_radius) / 2
        # Update each circle's coordinates to create expansion/contraction
        canvas.coords(circle, 100 - radius, 100 - radius, 100 + radius, 100 + radius)
    
    # Schedule the next frame of the animation
    root.after(animation_speed, animate, frame + 1)

# Start the animation
animate()

# Run the tkinter main loop
root.mainloop()



