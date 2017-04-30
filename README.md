# Unicorn expanded
A small but very useful python 2/3 module for the <a href="https://shop.pimoroni.com/products/unicorn-hat">pimoroni unicorn hat</a> expanding it's capabilities and powers.<br><br>

<b>Note:</b> This requires the unicorn hat library installed to work (install with <code>curl -sS https://get.pimoroni.com/unicornhat | bash</code>)<br><br>

## Documentation
To use it simply download unicorn_expanded.py, place it in the same folder as your unicorn hat script and put <code>from unicorn_expanded import *</code> at the top of the file. <br><br>

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

