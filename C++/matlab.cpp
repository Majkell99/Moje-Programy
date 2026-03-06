#include "matlab.hpp"
#include <math.h>
#include <cmath>

// Wersje standardowych bibliotek znanych z języka C, ale zaimplementowanych
// dla C++, mają przedrostek "c". Dołączając je, nie podajemy rozszerzenia ".h".
// Przykładowo: stdlib.h -> cstdlib
#include <cstdlib>

// Biblioteka <iostream> służy do obsługi strumieni wejścia/wyjścia (odpowiednik
// <stdio.h> w języku C).
#include <iostream>

//int* add_vectors(int* v1, int* v2, std::size_t n) {
//    int* v_sum = (int*) std::malloc(n * sizeof(int));
//    if (v_sum == (int*) NULL) {
//        return (int*) NULL;
//    }
//
//    for (std::size_t i = 0; i < n; i++) {
//        v_sum[i] = v1[i] + v2[i];
//    }
//
//    return v_sum;
//}

MatVect add_vectors(MatVect v3, MatVect v4) {
    MatVect v_sum(v3.size());

    for (std::size_t i = 0; i < (std::size_t) v3.size(); i++) {
        v_sum.set_elem(i, v3.get_elem(i) + v4.get_elem(i));
    }

    return v_sum;
}

void print_vector(MatVect v) {
    for (std::size_t i = 0; i < (std::size_t) v.size(); i++) {
        std::cout << v.get_elem(i) << " ";
    }
    std::cout << std::endl;
}


MatVect::MatVect(std::size_t n)
{
    for(std::size_t i = 0; i < n; i++)
    {
        v_.push_back(0);
    }
}

double MatVect::norm()
{
    double sum = 0.0;
    for(std::size_t i = 0; i < v_.size(); i++)
    {
        sum += v_[i] * v_[i];
    }

    return sqrt(sum);
}

//double MatVect::norm() {
//    double sum_of_squares = 0.0;
//    for (std::size_t i = 0; i < v_.size(); i++) {
//        sum_of_squares += v_[i] * v_[i];
//    }
//    return sqrt(sum_of_squares);
//}

//MatVect add_vectors(MatVect v1, MatVect v2) {
//    MatVect v_sum(v1.size());
//
//    for (std::size_t i = 0; i < v1.size(); i++) {
//        v_sum.set_elem(i, v1.get_elem(i) + v2.get_elem(i));
//    }
//
//    return v_sum;
//}
//
//void print_vector(MatVect v) {
//    for (std::size_t i = 0; i < v.size(); i++) {
//        std::cout << v.get_elem(i) << " ";
//    }
//    std::cout << std::endl;
//}