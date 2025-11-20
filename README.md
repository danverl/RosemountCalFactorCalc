Tool to calculate new 16 digit cal code for rosemount electromagnetic flow meters based on a reference total.

Warning. i make no claims to the accuracy of the tool. it is just a reference. use the output on your own risk, and double check the calculation and the result

The rosemount cal factor code has the following format:

XXXXX Y ZZ BBBBB KKK

X = Gain at 37.5 HZ

Y = Spacer

Z = Zero offset

B = Gain at 5 hz

K = trailing zeroes

Example: 0958255009448000

Formatted to 09582 5 50 09448 000

This gives a gain at 37.5 hz of 95.82%, a zero offset of 5.0% and a gain at 5hz of 94.48%
