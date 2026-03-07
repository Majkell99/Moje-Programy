#include <stdio.h>
#include <stdlib.h>
#include <tasks.h>

const Task* choose_more_important_task(const Task* t1, const Task* t2)
{
    if(t1 -> priority > t2 -> priority)
    {
        return t1;
    }
    else if(t1 -> priority < t2 -> priority)
    {
        return t2;
    }

    // lub
    // return (t1 -> priority > t2 -> priority) ? t1 : t2;
}

const char* priority_as_str(Priority p)
{
    switch (p)
    {
        case LOW:
            return "LOW";
            break;

        case MEDIUM:
            return "MEDIUM";
            break;

        case HIGH:
            return "HIGH";
            break;

        default:
            return "UNKNOWN";
            break;
    }
}

void increase_priority(Priority* p)
{
    if((*p) < HIGH) // skad program wie ze HIGH jest wyzsze niz MEDIUM i LOW ??? - Juz wiem
    {
        (*p)++;
    }
}

void transform_task(Task* t, void(*f)(Priority*))
{
    // nie wiem o co tu chodzi
}