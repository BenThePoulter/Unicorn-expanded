# Unicorn expanded
A python 3 module for the <a href="https://shop.pimoroni.com/products/unicorn-hat">pimoroni unicorn hat</a> to add a few extra commands. <br><br>

<b>Note:</b> This requires the unicorn hat library installed to work (install with <code>curl -sS https://get.pimoroni.com/unicornhat | bash</code>)<br><br>

## Documentation
To use it simply download unicorn-expanded.py, place it in the same folder as your unicorn hat script and put <code>from unicorn-expanded import *</code> at the top of the file. <br><br>

Fill the whole matrix one colour (but not show):
<code>fill(R, G, B)</code><br>
Fill the matrix with a rainbow (but also not show): 
<code>rainbow()</code><br>
Fade the brightness from 0 to 0.9:
<code>fadein()</code><br>
Fade the brighness from 0.9 to 0:
<code>fadeout()</code><br>
Pulse the matrix:
<code>pulse(times)</code><br>
Instantly clear:
<code>clear()</code><br>

