#include "Catalogue.h"

std::string to_string(const Product& p)
{
    std::ostringstream text;
    text << p.get_name() << " [" << p.get_id() << "] $" <<
    std::fixed << std::setprecision(2) << p.get_price();
    return text.str();
}

std::vector<Product> Catalogue::get_products_with_appropriate_price(std::function<bool(double)> criterion) const
{
    std::vector<Product> products;

    for(const auto& iter : inventory_)
    {
        const auto& product = iter.second; // zamiast const auto& moze byc const Product&

        if(criterion(product.get_price()))
            products.push_back(product);
    }

    return products;
}

std::vector<Product> Catalogue::get_products_by_name_part(std::string substr, bool is_case_sensitive) const
{
      std::vector<Product> products;

    for(const auto& iter : inventory_)
    {
        const Product product = iter.second;
        std::string name = product.get_name();

        if(!is_case_sensitive)
        {
            //przeksztalcanie na male litery za pomoca petli for:
            //      for(char& c : substr)
            //      {
            //          c = std::tolower(c);
            //      }
            //za pomoca std::transform:
            std::transform(substr.begin(), substr.end(), substr.begin(), std::tolower());
            std::transform(name.begin(), name.end(), name.begin(), std::tolower());
        }

        if(name.find(substr) != std::string::npos) // szukamy w name funkcją find napisu substr
            products.push_back(product);               // jezeli funkcja find nie znajduje szukanego podciagu znakow
    }                                                  // to zwraca std::string::npos dlatego w if
}                                                      // daje warunek ze ma byc to rozne od std::string::npos

//std::vector<Product> Catalogue::get_products_by_name_part(std::string substr, bool is_case_sensitive) const {
//    std::vector<Product> products;
//
//    for (const auto& entry : inventory_) {
//        const auto& product = entry.second;
//        std::string name = product.get_name();
//
//        std::string name_transformed = name;
//        std::string chunk_transformed = substr;
//
//        if (!is_case_sensitive) {
//            std::transform(name.begin(), name.end(), name_transformed.begin(), ::tolower);
//            std::transform(substr.begin(), substr.end(), chunk_transformed.begin(), ::tolower);
//        }
//
//        bool contains_substr = (name_transformed.find(chunk_transformed) != std::string::npos);
//        if (contains_substr) {
//            products.push_back(product);
//        }
//    }
//
//    return products;
//}

// MOJA WERSJA FUNKCJII DO SZUKANAI PRODUKTU PO KRYTERIUM CENY:
//std::vector<Product> Catalogue::get_products_with_appropriate_price(const double& price) const
//{
//    std::vector<Product> products;
//
//    for(const auto& iter : inventory_)
//    {
//        const auto& product = iter.second;
//
//        if(product.get_price() == price)
//            products.push_back(product);
//    }
//
//    return products;
//}