>>> # Print the inverted dictionary
... observations_sorted = list(observations_to_birds_list.keys())
>>> observations_sorted.sort()
>>> for observations in observations_sorted:
...     print(observations, ':', end=" ")
...     for bird in observations_to_birds_list[observations]:
...         print(' ', bird, end=" ")
...     print()
... 
1 :   northern fulmar   snow goose 
2 :   long-tailed jaeger 
5 :   canada goose 
