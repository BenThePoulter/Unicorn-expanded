# Unicorn expanded
A small but very useful python module for the <a href="https://shop.pimoroni.com/products/unicorn-hat">pimoroni unicorn hat</a> expanding it's capabilities and powers.<br><br>

<b>Note:</b> This requires the unicorn hat library installed to work (install with <code>curl -sS https://get.pimoroni.com/unicornhat | bash</code>)<br><br>

## Documentation
To use it simply download unicorn_expanded.py, place it in the same folder as your unicorn hat script and put <code>from unicorn_expanded import *</code> at the top of the file. <br><br>


### Funtions
Fill the screens buffer one colour (won't display it though): <code>fill(R, G, B)</code><br><br>
Fill the buffer with a rainbow (also wont't display): <code>rainbow()</code><br><br>
Show the buffer immediately on a brightness of 0.9: <code>on()</code><br><br>
Switch off the buffer immediately to a brightness of 0: <code>off()</code><br><br>
Fade in the buffer from 0 to 0.9 in 9 seconds (fixed speed deal with it): <code>fadein()</code><br><br>
Fade out the buffer from 0.9 to 0 in 9 seconds (also fixed speed): <code>fadeout()</code><br><br>
Flash the buffer very fast (strobe): <code>strobe(times)</code><br><br>
pulse the buffer between 0.9 and 60 (start at 0.9 then fade to 0.6 then fade back to 0.9): <code>pulse(times)</code><br><br>
Set brightness to 0 and clear immediately: <code>clear()</code><br><br>
