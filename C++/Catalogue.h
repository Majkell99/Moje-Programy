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

#ifndef CLIONPROJECTSMATLAB3CATALOGUE_CATALOGUE_H
#define CLIONPROJECTSMATLAB3CATALOGUE_CATALOGUE_H

class Product
{
public:
    Product(std::string id, std::string name, double price);

    std::string get_id() const {return id_;}
    std::string get_name() const {return name_;}
    double get_price() const {return price_;}

private:
    std::string id_;
    std::string name_;
    double price_;
};

std::string to_string(const Product& p);

class Catalogue
{
public:
    Catalogue(const std::map<std::string, Product>& inventory) : inventory_(inventory) {}

    bool contains(const std::string& id) const
    {return (inventory_.find(id) != inventory_.end());}

    void add_products(const Product& product)
    {inventory_.emplace(product.get_id(), product);}

    std::vector<Product> get_products_with_appropriate_price(std::function<bool(double)> criterion) const;

    std::vector<Product> get_products_by_name_part(std::string substr, bool is_case_sensitive) const;

private:
    std::map<std::string, Product> inventory_;
};

#endif //CLIONPROJECTSMATLAB3CATALOGUE_CATALOGUE_H

