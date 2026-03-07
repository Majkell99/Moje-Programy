#include "shapes.h"

double calculate_total_area(const std::vector<Shape*>& shapes)
{
    double sum = std::accumulate(shapes.begin(), shapes.end(), 0.0,
                                 [](double sum1, Shape* shape){return sum1 + shape->area();});
    return sum;
}