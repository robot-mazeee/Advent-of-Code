#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
using namespace std;

bool safe(vector<int> numbers, int index) {
    vector<int> copy;

    for (int i = 0; i < numbers.size(); i++) {
        if (i == index) continue;
        copy.push_back(numbers[i]);
    }

    bool increasing = false;
    if (copy[0] < copy[1]) 
        increasing = true;
    else 
        increasing = false;

    for (int i = 0; i < copy.size(); i++) {
        if (i > 0) {
            int prev = copy[i-1], current = copy[i];

            if (prev == current) {
                return false;
            }
            if (abs(prev-current) < 1 || abs(prev-current) > 3) {
                return false;
            }
            if (prev > current && increasing) {
                return false;
            }
            if (prev < current && !increasing) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    int count = 0;

    fstream input;
	input.open("input.txt", ios::in);

    string line;
    while (getline(input, line)) {
        stringstream ss(line);
        int a, changed = 0;
        vector<int> numbers;

        while (ss >> a) numbers.push_back(a);

        for (int i = 0; i < numbers.size(); i++) {
            // if it's safe without that element
            if (safe(numbers, i)) {
                count++;
                break;
            }
        }
    }
    input.close();

    cout << count << '\n';

    return 0;
}