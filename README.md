
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Fractal Geometry</h1>
    <p>This repository contains implementations of various fractals, including the Newton fractal, Julia set, and Koch curve. These visualizations are created using Python with the <code>numpy</code> and <code>matplotlib</code> libraries.</p>
  
  <h2>Contents</h2>
    <ul>
        <li><strong>Newton Fractal</strong>
            <ul>
                <li>Implementation of Newton's method to find roots of the function <code>f(z) = z<sup>4</sup> - 1</code>.</li>
                <li>Visualizes the convergence to different roots in the complex plane.</li>
            </ul>
        </li>
        <li><strong>Julia Set</strong>
            <ul>
                <li>Generates a Julia set based on the function <code>f(z) = z<sup>2</sup> + c</code> where <code>c</code> is a constant complex number.</li>
                <li>Includes an animation showcasing the transformation of the Julia set by varying the real part of <code>c</code>.</li>
            </ul>
        </li>
        <li><strong>Koch Curve</strong>
            <ul>
                <li>A simple implementation of the Koch snowflake fractal using turtle graphics.</li>
            </ul>
        </li>
    </ul>
   
   <h2>Requirements</h2>
    <p>To run the code, you need Python with the following libraries:</p>
    <ul>
        <li><code>numpy</code></li>
        <li><code>matplotlib</code></li>
        <li><code>turtle</code> (for the Koch curve)</li>
    </ul>
    <p>You can install the required libraries using pip:</p>
    <pre><code>pip install numpy matplotlib</code></pre>
    
   <h2>Usage</h2>
    <ol>
        <li><strong>Julia Set Animation:</strong>
            <ul>
                <li>Run <code>julia.py</code> to generate the Julia set and save an animated GIF of the fractal.</li>
            </ul>
        </li>
        <li><strong>Newton Fractal:</strong>
            <ul>
                <li>Run <code>newton_fractal.py</code> to visualize the Newton fractal and observe the convergence to the roots.</li>
            </ul>
        </li>
        <li><strong>Koch Curve:</strong>
            <ul>
                <li>Run <code>koch_curve.py</code> to draw the Koch snowflake fractal using turtle graphics.</li>
            </ul>
        </li>
    </ol>

<h2>Output</h2>
    <ol>
        <li><strong>Julia Set</strong>
            
   ![ani](https://github.com/user-attachments/assets/7ed79bc3-7a6c-47f1-b4a2-a67f848b61d4) </li>
       <li><strong>Newton Fractal</strong>
       
 ![newton](https://github.com/user-attachments/assets/74ec75ec-4751-456d-a2c9-52cfc7ef0636)</li>
        <li><strong>Koch Curve</strong>
        
 ![delete](https://github.com/user-attachments/assets/f7b2e0e0-955b-431e-8d8b-7dac49b8cdb6)</li>

 <ol>
</body>
</html>

