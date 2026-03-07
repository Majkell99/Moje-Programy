#include <cstdlib>
#include <cstddef>
#include <vector>
#include <iostream>
#include <math.h>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <map>
#include <iomanip>
#include <functional>
#include <iterator>
#include <cctype>
#include <cstdint>

#ifndef COMPLEX_1_COMPLEX_H
#define COMPLEX_1_COMPLEX_H

class Complex
{
public:
    Complex(const double& re, const double& im) : re_(re), im_(im) {}
    Complex(double data[2]) : Complex(data[0], data[1]) {} // delegowanie konstruktora

    double re() const {return re_;}
    double im() const {return im_;}

private:
    double re_;
    double im_;
};

#endif //COMPLEX_1_COMPLEX_H
