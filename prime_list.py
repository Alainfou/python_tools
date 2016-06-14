#!/usr/bin/python

import math
import sys
import getopt

print "\n\tHey, that's personal! That's my very, very personal tool for listing prime numbers! Please get out of here! =(\n"

dat_prime_list = [2,3]

def its_prime (p):

        s = int(math.sqrt(p))+1

        for i in dat_prime_list :
                if (p%i) == 0:
                        return False
        return True

def yeah (argv):
        try:
                opts, args = getopt.getopt(argv,"n:l:")
        except getopt.GetoptError:
                print 'prim.py -n <number_until_which_primes_shall_be_listed>'
                sys.exit(2)

        until_there = 42
        based_on_prime_limit = False
        list_length = 42
        based_on_list_length = False
        p = 5

        for opt, arg in opts:
                if opt == '-n':
                        based_on_prime_limit = True
                        try:
                                until_there = int(arg)
                        except ValueError:
                                print 'Invalid argument. Limit will be set to 42, which is a totally arbitrary and random number.'
                elif opt == '-l':
                        based_on_list_length = True
                        try:
                                list_length = int(arg)
                        except ValueError:
                                print 'Invalid argument. Length will be set to 42, which is a totally arbitrary and random number.'

        if based_on_prime_limit :
                while (p < until_there):
                        if its_prime (p):
                                dat_prime_list.append(p)
                        p+=2
                print 'Fine... Here are your prime numbers until ',until_there
        elif based_on_list_length :
                while (len(dat_prime_list)<list_length):
                        if its_prime (p):
                                dat_prime_list.append(p)
                        p+=2
                print 'Fine... Here are your ',list_length,' prime numbers.'
        print dat_prime_list

if __name__ == "__main__":
        yeah(sys.argv[1:])

