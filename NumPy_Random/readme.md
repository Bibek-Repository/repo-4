Random Numbers in NumPy

Random is a number that cannot be predicted logically. It does not mean different number every time. Computers work on programs, and programs are definitive set of instructions. If there is a program to generate a random number it can be predicted, thus it is not truly random. Random numbers generated through a generation algorithm are called pseudo random. In order to generate truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc. The random module in NumPy is used to generate random number. There are three methods in this module:
rand() : It will generate random floats from 0 to 1 
randint() : It takes two parameter one for the range and the other for the size
choice() : It will generate random value from an array. It can also return an array, size parameter will determine the size of array it returns.