#include <iostream>
#include <cstdlib>

int main()
{
    std::string name;

    while (std::getline(std::cin, name)) {
        std::cout << "Hello, " + name + "!" << std::endl;
    }

    return EXIT_SUCCESS;
}
