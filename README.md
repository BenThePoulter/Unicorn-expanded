# Unicorn expanded
A python 3 module for the <a href="https://shop.pimoroni.com/products/unicorn-hat">pimoroni unicorn hat</a> to add a few extra commands. <br><br>

<b>Note:</b> This requires the unicorn hat library installed to work (install with <code>curl -sS https://get.pimoroni.com/unicornhat | bash</code>)<br><br>

## Command Documentation
To use it simply download the file, place it in the same folder as your unicorn hat script and put <code>from unicornExpanded import *</code> at the top of the file. <br><br>

Fill the whole matrix one colour (but not show):
<code>fill(R, G, B)</code><br>
Fade the brightness from 0 to 0.9:
<code>fadein()</code><br>
Fade the brighness from 0.9 to 0:
<code>fadeout()</code><br>
Pulse the matrix:
<code>pulse(times)</code><br>
instantly clear:
<code>clear()</code><br>

