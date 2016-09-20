I implemented the Diceware password generation method in C++ and Python. 
More information about this method can be found here: http://world.std.com/~reinhold/diceware.html

Using a computer to generate random numbers for use in the Diceware method is technically not as secure
as with physical dice. However, since these programs use /dev/urandom, it is in practice random enough for most purposes.

I've also implemented a non-legitmate version of the Diceware method that stores the words in an array instead of a map. 
Random numbers are combined to form an array position from which a word is selected. 

There are also two small programs here to convert the original list of words into the map declaration format in python
and C++.
