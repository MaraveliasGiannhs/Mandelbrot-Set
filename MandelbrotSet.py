import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            c = complex(x[i], y[j])
            img[i, j] = mandelbrot(c, max_iter)
    return img

def plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    mandel_img = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(mandel_img.T, extent=(xmin, xmax, ymin, ymax))
    plt.title("Mandelbrot Set")
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.show()

# Set up the parameters for the plot
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
width, height = 2000, 2000
max_iter = 100

# Plot the Mandelbrot set
plot_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
