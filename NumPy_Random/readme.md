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

Poisson Distribution
Poisson Distribution is a Discrete Distribution. It estimates how many times an event can happen in a specified  time. If for example, Bibek eats twice a day what is the probability that I will eat thrice? It has two parameters: lam: rate or known number of occurrence e.g. bibek eats twice. size: the shape of the array which is returned. Poisson distribution is discrete whereas normal distribution is continuous. For large data points both the poisson and normal distribution are similar.

Uniform Distribution
It is used to describe probability where every event has equal chances of occuring. Example Generation of random numbers. It has three parameters: low: lower bound: default 0.0. high: upper bound: default 1.0. size: The shape of the array which is returned.

Logistic Distribution
It is used to describe growth. It is extensively used in machine learning such as logistic regression, neural networks etc. It has three parameters: loc: mean, where the peak is default = 0, scale: standard deviation, the flatness of distribution: default 1, size: the shape of the returned array. The difference between logistic and normal distribution is that logistic distribution has more area under the tails, meaning it represents more possibility of occurence of an event further away from mean. For higher value of standard deviation, the normal and logistic distributions are near identical apart from the peak

Multinomial distribution
It is a generalization of binomial distribution. It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. Example: Blood type of a population, dice roll outcome. It has three parameters:
n: number of possible outcomes (example: 6 for dice roll)
pvals: list of probabilities of outcomes(example: 1/6,1/6,1/6,1/6,1/6,1/6 for dice roll)
size: the shape of the array it returns
They will produce one value for each pval. As they are generalization of binomial distribution their visual representation and similarity of normal distribution is same as that of multiple binomial distributions.

Exponential Distribution
It is used for describing time till next event. Example: failure/success etc. It has two parameters:
scale: inverse of rate(defalut to 1.0)
size: The shape of the array it returns
Poisson Distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time between these events.

Chi Square Distribution
It is used as a basis to verify the hypothesis. It has two parameters: 
df: degree of freedom
size: the shape of the array it returns

Rayleigh Distribution
It is used in signal processing. It has two parameters:
scale: standard deviation. It decides how flat the distribution will be default 1.0
At unit standard deviation, and 2 degree of freedom rayleigh and chi square represent the same distributions.

Pareto Distribution
pareto's law: 80-20 distribution (20% factors cause 80% outcome). It has two parameter:
a : shape parameter
size: the shape of the returned array

Zipf Distribution
They are used to sample data based on zipf's law. In a collection, the nth common term is 1/n times of the most common term. Example the 5th most common word in English occurs nearly 1/5 times as often as the most common word. It has two parameter:
a : distribution parameter
size : the shape of the returned array
