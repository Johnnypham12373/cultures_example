#include <iostream> 
#include <vector>
using namespace std;
extern "C" {
    int sum_array(int* array, int length) {
        int total = 0;
        for (int i = 0; i < length; ++i) {
            total += array[i];
        }
        return total;
    }
}
