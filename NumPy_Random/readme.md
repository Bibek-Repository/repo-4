Random Numbers in NumPy

Random is a number that cannot be predicted logically. It does not mean different number every time. Computers work on programs, and programs are definitive set of instructions. If there is a program to generate a random number it can be predicted, thus it is not truly random. Random numbers generated through a generation algorithm are called pseudo random. In order to generate truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc. The random module in NumPy is used to generate random number. There are three methods in this module:
rand() : It will generate random floats from 0 to 1 
randint() : It takes two parameter one for the range and the other for the size
choice() : It will generate random value from an array. It can also return an array, size parameter will determine the size of array it returns.

Seaborn is a library that uses Matplotlib to plot graphs. It will be used to visualize random distributions. pip install seaborn is used to install the seaborn library. Distplot stands for distribution plot. It is depreciated in python 3. displot() method can be used instead. It takes an array as input and plots a curve corresponding to the distribution of points in the array. That means how to points in array are distributed is shown in the curve through the plot. hist=False will remove the histogram from the plot.

Normal Distribution
The Normal Distribution is also called the Gaussian Distribution. It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc. random.normal() method is used to get a Normal Data Distribution. It has three parameters: loc - mean where the peak of the bell exists. scale - Standard Deviation, how flat the graph distribution should be. size - The shape of the returned array. The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.

Binomial Distribution
It is a Discrete Distribution. It describes the outcome of binary scenarios, e.g. toss of a coin, it will be either head or tail. It has three parameters: n: number of trials, p: probability of occurence of each trial(e.g. for toss of a coin 0.5 each) and size: the shape of the returned array.
Discrete Distribution: The distribution is defined at separate set of events, eg. a coin toss's result in discrete as it can be only head or tails whereas height of people is continous as it can be 170, 170.1, 170.11 and so on.

The Normal Distribution and the Binomial Distribution are the same if the data points are large in number