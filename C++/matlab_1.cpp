#include "matlab.hpp"
//ZAD 1
void Orchestra::play_music() const
{
    for(const auto& elem : v_)
    {
        elem->get_sound();
    }
}


