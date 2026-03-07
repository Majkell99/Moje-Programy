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
#include <memory>
#include <utility>

#ifndef VEHICLES_1_VEHICLES_H
#define VEHICLES_1_VEHICLES_H

class Vehicle
{
public:
    Vehicle(const std::string& id, const std::string& brand) : id_(id), brand_(brand), vin_(next_vin_++) {} //{id_ = id; brand_ = brand;}
    //najpierw przypisujemy next_vin_ do vin_ a potem inkrementujemy o1
    Vehicle(const Vehicle& v) = default; // konstrukotr kopiujacy z default // Vehicle(const Vehicle& v) : v_(v) {}

    // Vehicle() = default;  // konstruktor domyslny (zwykly) z default
    std::string get_id() const {return id_;}
    std::string get_brand() const {return brand_;}

    virtual double get_max_speed() const = 0;

    std::int64_t get_vin() {return vin_;}

    void reset_vin_counter() {next_vin_ = 1;}

    virtual ~Vehicle() = default;

private:
    std::string id_;
    std::string brand_;
    std::int64_t vin_;
    static std::int64_t next_vin_; // pole statyczne wtedy kiedy odnosimy sie do wszystkich obiektow danej klasy
};

std::int64_t Vehicle::next_vin_ = 1;

class Car : public Vehicle
{
public:
    Car(const std::string& id, const std::string& brand, const double& engine_hp) : Vehicle(id, brand),
    engine_hp_(engine_hp) {}
    Car(const Car& c) = default;

    double get_max_speed() const override {return engine_hp_;}

    ~Car() override = default;

private:
    double engine_hp_;
};

class Bicycle : public Vehicle
{
public:
    Bicycle(const std::string& id, const std::string& brand, const int& n_gears) : Vehicle(id, brand),
    n_gears_(n_gears) {}
    Bicycle(const Bicycle& b) = default;

    double get_max_speed() const override {return (3*n_gears_);}

    ~Bicycle() override = default;

private:
    int n_gears_;
};

std::string to_string(const Vehicle& v);

double compute_min_travel_duration(double distance, const Vehicle& v);

std::string compute_min_travel_duration_as_string(double distance, const Vehicle& v);

std::vector<Vehicle*> filter_vehicles(
        std::vector<Vehicle*>::const_iterator vehicles_begin,
        std::vector<Vehicle*>::const_iterator vehicles_end,
        std::function<bool (const Vehicle&)> predicate);

std::string to_string(std::vector<Vehicle*>::const_iterator vehicles_begin,
                      std::vector<Vehicle*>::const_iterator vehicles_end);



class Driver
{
public:
    enum Gender{MALE, FEMALE};

    Driver(const std::string& name, const Gender& gender, std::unique_ptr<Vehicle> vehicle_ptr) : name_(name), gender_(gender), vehicle_ptr_(std::move(vehicle_ptr)) {}
    Driver(const std::string& name, const Gender& gender) : Driver(name, gender, nullptr) {}
    Driver(const Driver&) = delete;
    Driver& operator=(const Driver&) = delete;

    Driver(Driver&& object) noexcept : name_(object.name_), gender_(object.gender_), vehicle_ptr_(std::move(object.vehicle_ptr_)) {}
    Driver& operator=(Driver&& other) noexcept
    {
        name_ = other.name_;
        vehicle_ptr_ = std::move(other.vehicle_ptr_);
        return *this;
    }

    void assign_vehicle(std::unique_ptr<Vehicle> vehicle_ptr) {vehicle_ptr_ = std::move(vehicle_ptr);}

    std::string get_name() const {return name_;}

    Vehicle* get_vehicle() const {return vehicle_ptr_.get();}

    Gender get_gender() const {return gender_;}

private:

    std::string name_;
    Gender gender_;
    std::unique_ptr<Vehicle> vehicle_ptr_;

};

std::string to_string(const Driver& d);

void assign_vehicle_to_driver(std::vector<std::unique_ptr<Vehicle>>& vehicles, Driver& owner);

#endif //VEHICLES_1_VEHICLES_H
