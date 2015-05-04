# AlgorithmsGreatestHits

Python 3 implementations of various algorithms and data structures for studying.

## Installing the dependencies

Quick sort requires numpy, which you can install with pip, or for users on Ubuntu-based linux distros, by installing the python3-numpy package from aptitude.

## Running the Tests

To run the tests for one class:

    python3 -m unittest path.to.class

For example, to run the binary search tress tests:

    python3 -m unittest data_structures.test_binarysearchtree

To run all unit tests:

    python3 -m unittest discover

There are also a couple of performance tests that can't be run at the same time as other tests:

    python3 -m unittest data_structures.perf_test_trie

## TODO

### Refactor
* data_structures
** Implement heaps for yourself

### Unit test
* data_structures
** graph
* graph_algorithms
** all of them
* other_algorithms
** all of them
* search_algorithms
** rselect

To run all unit tests:

    python3 -m unittest discover

## TODO

### Refactor
* data_structures
** split heaps into 3 files

### Unit test
* data_structures
  * graph
* graph_algorithms
  * all of them (FOR SHAME)
* other_algorithms
  * all of them (SLACKER)


## Contributing

I'm... not sure why you would?
