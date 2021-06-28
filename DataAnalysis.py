from timeit import timeit
from statsmodels.sandbox.stats.runs import runstest_1samp
import matplotlib.pyplot as plt
import numpy as np

def midsq(seed,randoms,num):
    # square the seed values
    seed_sq = seed ** 2
    # append the middle 4 digits of the squared seed value to the list of random numbers
    # zfill is a string method that will add leading zeros needed for padding to make it a 8 digit number
    randoms.append(int(str(seed_sq).zfill(8)[2:6]))
    # set counter variable to 1 since we now have 1st random number in list of randoms
    count = 1
    # loop while counter is less than number of randoms to generate
    while count<num:
        # first square the previous random numbers value in list and add padding zeros to make it 8 digits if needed
        # then slice the middle 4 digits of the squared value with the padding zeros and append to list of random numbers
        randoms.append(int(str(randoms[count-1]**2).zfill(8)[2:6]))
        # increment counter
        count+=1


def linconm(X_0, mod, mult, inc, randoms, num):
    #append seed value to list
    randoms.append(X_0)
    # set counter variable to 1 since seed value is in list
    count = 1
    # loop while counter is less than number of randoms to generate
    while count < num:
        # append next random number generated from LCG algorithm to list
        # to get next random, multiply last generated random by multiplier
        # add product result with increment, then do modulus the mod value
        randoms.append(((mult * randoms[count - 1]) + inc) % mod)
        # increment counter
        count += 1

# this code contributed from Dr. Wooster CSCI U236 class to time functions
def time_function(func,*args,reps=10):
    # passes *args into function func and times it reps times
    # divide by number of reps to get average execution time
    avg_time = timeit(lambda: func(*args), number=reps) / reps
    # return avearge execution time in milliseconds
    return avg_time * 1000

# create 10 lists, 5 for MSM, 5 for LCM, one for each different seed value
# 5 MSM
lst = []
lst1 = []
lst2 = []
lst3 = []
lst4 = []
# 5 LCM
lst5 = []
lst6 = []
lst7 = []
lst8 = []
lst9 = []
# list of seeds to be used
seeds = [3659, 4863, 6983, 7289, 8473]
# create list for execution times of MSM
midsq_times = []
# create list for execution times of LCM
lcm_times = []

# cc65's modulus, multiplier, and increment values (m, a, and c)
m = 2**32
a = 16843009
c = 826366247


# for each different seed value, call the MSM function to generate 50 random numbers,
# and store results from MSM with different seeds in separate lists
# also append the execution time to list for execution times of MSM by calling timing function
midsq_times.append(time_function(midsq, seeds[0], lst, 50,reps=1))
midsq_times.append(time_function(midsq, seeds[1], lst1, 50,reps=1))
midsq_times.append(time_function(midsq, seeds[2], lst2, 50,reps=1))
midsq_times.append(time_function(midsq, seeds[3], lst3, 50,reps=1))
midsq_times.append(time_function(midsq, seeds[4], lst4, 50,reps=1))

# for each different seed value, call the LCM function to generate 50 random numbers,
# and store results from LCM with different seeds in separate lists
# also append the execution time to list for execution times of LCM by calling timing function
lcm_times.append(time_function(linconm, seeds[0], m, a, c, lst5, 50, reps=1))
lcm_times.append(time_function(linconm, seeds[1], m, a, c, lst6, 50, reps=1))
lcm_times.append(time_function(linconm, seeds[2], m, a, c, lst7, 50, reps=1))
lcm_times.append(time_function(linconm, seeds[3], m, a, c, lst8, 50, reps=1))
lcm_times.append(time_function(linconm, seeds[4], m, a, c, lst9, 50, reps=1))









# print each list of random numbers and underneath print out the p-value statistic from the Runs test for randomness for the specific seed and method
# runstest_1samp returns a tuple with first value being z-test statistic and second value is the corresponding p-value for each dataset
print(lst)
print()
print('Runs test for randomness p-value (MSM) (seed = 3659): ' + str( runstest_1samp(lst)[1]))
print()
print(lst1)
print()
print('Runs test for randomness p-value (MSM) (seed = 4863): ' + str( runstest_1samp(lst1)[1]))
print()
print(lst2)
print()
print('Runs test for randomness p-value (MSM) (seed = 6983): ' + str( runstest_1samp(lst2)[1]))
print()
print(lst3)
print()
print('Runs test for randomness p-value (MSM) (seed = 7289): ' + str( runstest_1samp(lst3)[1]))
print()
print(lst4)
print()
print('Runs test for randomness p-value (MSM) (seed = 8473): ' + str( runstest_1samp(lst4)[1]))
print()
print(lst5)
print()
print('Runs test for randomness p-value (LCM) (seed = 3659): ' + str( runstest_1samp(lst5)[1]))
print()
print(lst6)
print()
print('Runs test for randomness p-value (LCM) (seed = 4863): ' + str( runstest_1samp(lst6)[1]))
print()
print(lst7)
print()
print('Runs test for randomness p-value (LCM) (seed = 6983): ' + str( runstest_1samp(lst7)[1]))
print()
print(lst8)
print()
print('Runs test for randomness p-value (LCM) (seed = 7289): ' + str( runstest_1samp(lst8)[1]))
print()
print(lst9)
print()
print('Runs test for randomness p-value (LCM) (seed = 8473): ' + str( runstest_1samp(lst9)[1]))

# create plot to plot execution time of both methods for each seed value

fig, ax = plt.subplots()
index = np.arange(5)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, midsq_times, bar_width, alpha=opacity,color='b',label='MSM')

rects2 = plt.bar(index + bar_width, lcm_times, bar_width,alpha=opacity,color='g',label='LCM')

plt.xlabel('Seed Value')
plt.ylabel('Execution Time (ms)')
plt.title('Execution Times for Different Seed Values')
plt.xticks(index + bar_width, tuple(seeds))
plt.legend()

plt.show()
