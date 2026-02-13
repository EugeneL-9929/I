#ifndef ARRAY_H
#define ARRAY_H
#include <iostream>
using namespace std;

static int count = 0;

template <typename T, int LENGTH>

struct Array{
    public:
        Array(): length{LENGTH} {
            std::cout << "You have define " << count++ << " arrays." << std::endl;            
        };

        T arr[LENGTH];
        size_t length;

};

#endif