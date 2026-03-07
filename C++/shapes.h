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
#include <numeric>

#ifndef SHAPES_1_SHAPES_H
#define SHAPES_1_SHAPES_H

const double PI = 3.141592;

class Shape
{
public:
    Shape(const double& x, const double& y) {x_ = x; y_ = y;} // : x_(x), y_(y) {}

    virtual double area() const = 0;

    virtual ~Shape() {};

private:
    double x_;
    double y_;
};

class Square : public Shape
{
public:
    Square(const double& x, const double& y, const double& side) : Shape(x, y) {side_ = side;} //, side_(side) {}

    double area() const override {return side_*side_;}

    ~Square() override = default;

private:
    double side_;
};

class Circle : public Shape
{
public:
    Circle(const double& x, const double& y, const double& radius) : Shape(x, y), radius_(radius) {} // {radius_ = radius:}

    double area() const override {return PI*radius_*radius_;}

    ~Circle() override = default;

private:
    double radius_;
};

double calculate_total_area(const std::vector<Shape*>& shapes);

#endif //SHAPES_1_SHAPES_H
