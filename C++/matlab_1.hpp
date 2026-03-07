#ifndef INCLUDE_MATLAB_HPP_
#define INCLUDE_MATLAB_HPP_

// Biblioteka <cstddef> zawiera definicję typu `std::size_t`.
#include <cstdlib>
#include <cstddef>
#include <vector>
#include <iostream>
#include <math.h>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <iomanip>



// NAUKA DO KOLOKWIUM
//
// ZAD 1
class Instrument
{
public:
    Instrument() = default;
    virtual void get_sound() const = 0;
    virtual ~Instrument() = default;
};

class Piano : public Instrument
{
public:
    Piano() = default;
    void get_sound() const override {std::cout << "piano_sound";}
    ~Piano() override = default;
};

class Guitar : public Instrument
{
public:
    Guitar() = default;
    void get_sound() const override {std::cout << "guitar_sound";}
    ~Guitar() override = default;
};

class Orchestra
{
public:
    Orchestra() = default;

    void play_music() const;

private:
    std::vector<Instrument*> v_;
};



//ZAD 2

//class Abs
//{
//public:
//    virtual void foo() = 0;
//    virtual ~Abs() = default;
//};
//
//class Con : public Abs
//{
//public:
//    void foo() override;
//    ~Con() override = default;
//};



//Moj program
class Menu
{
public:
    Menu() = default;

    std::string typeMenu() {return typeMenu_;}

private:
    std::string typeMenu_;
};

class Soup : public Menu
{
public:

};


#endif /* INCLUDE_MATLAB_HPP_ */
