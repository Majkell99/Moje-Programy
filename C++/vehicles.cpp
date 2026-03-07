#include "vehicles.h"

std::string to_string(const Vehicle& v)
{
    std::ostringstream text;
    text << v.get_id() << " : " << v.get_brand();

    return text.str();
}
// t = S/V
double compute_min_travel_duration(double distance, const Vehicle& v)
{
    double t = distance / v.get_max_speed();
    return t;
}

std::string compute_min_travel_duration_as_string(double distance, const Vehicle& v)
{
    std::ostringstream text;
    text << compute_min_travel_duration(distance, v) << std::fixed << std::setprecision(3) << "h";
    return text.str();
}

std::vector<Vehicle*> filter_vehicles(
        std::vector<Vehicle*>::const_iterator vehicles_begin,
        std::vector<Vehicle*>::const_iterator vehicles_end,
        std::function<bool (const Vehicle&)> predicate)
{
    std::vector<Vehicle*> products;
//Moj sposób:
//    for(std::vector<Vehicle*>::const_iterator it = vehicles_begin; it != vehicles_end; ++it)
//    {
//        if(predicate(**it))
//        {
//            products.push_back(*it);
//        }
//    }
//Sposob std::copy_if:
    std::copy_if(vehicles_begin, vehicles_end, std::back_inserter(products),
                 [&predicate](const Vehicle *vehicle) {return predicate(*vehicle);}); // nie do konca rozumiem ta linijke
    return products;
}

//std::function<bool (const Vehicle&)> slower_than_50kph = [](const Vehicle& vehicle) {
//    return vehicle.get_max_speed() < 50;
//};
// przykladowa funkcja jakiegos kryterium ktora mozna wstawic jako funkcje predicate:
bool max_speed_predicate(const Vehicle& vehicle) {return vehicle.get_max_speed() >= 100;}

std::string to_string(std::vector<Vehicle*>::const_iterator vehicles_begin,
                      std::vector<Vehicle*>::const_iterator vehicles_end)
{
// Wersja z zadania:
//    std::string text;
//    for(auto& it = vehicles_begin; it != vehicles_end; ++it)
//    {
//        const auto& vehicle = *(*it);
//        text += to_string(vehicle);
//        text += "\n";
//    }
//    return text;
// Moja wersja (wg mnie lepsza):
    std::ostringstream text;
    for(auto& it = vehicles_begin; it != vehicles_end; ++it)
    {
        text << *it << std::endl;
    }
    return text.str();
}

//Car::~Car() {
//    // Implementacja destruktora
//}
//Bicycle::~Bicycle() {
//    // Implementacja destruktora
//}
///// NAUKA:
//class Car1 : public Vehicle
//{
//public:
//    Car(const std::string& id, const std::string& brand, const double& engine_hp)
//    : Vehicle(id, brand) {engine_hp_ = engine_hp;}
//    Car(const Car& c) = default;
//
//private:
//    double engine_hp_;
//};

//Vehicle(const std::string& id, const std::string& brand) : id_(id), brand_(brand), vin_(next_vin_++) {}

std::string to_string(const Driver& d)
{
    std::ostringstream text;
    if(d.get_vehicle() == nullptr)
        text << d.get_name() << " : [no vehicle]";
    else
        text << d.get_name() << " : [" << to_string(*d.get_vehicle()) << "]";
// SPYTAJ O FUNKCJE to_string z linijki wyzej
    return text.str();
}

void assign_vehicle_to_driver(std::vector<std::unique_ptr<Vehicle>>& vehicles, Driver& owner)
{
    if (vehicles.empty())
        owner.assign_vehicle(nullptr);
    else
        owner.assign_vehicle(std::move(vehicles.back()));
    vehicles.pop_back(); // pop_back() - nwm czy to o to tu chodzilo
}

