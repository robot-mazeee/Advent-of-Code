#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
using namespace std;

int main() {
    int count = 0;

    fstream input;
	input.open("input.txt", ios::in);

    string line;
    while (getline(input, line)) {
        stringstream ss(line);
        int a, index = -1;
        vector<int> numbers;

        bool increasing = true, safe = true;
        while (ss >> a) {
            index++;
            numbers.push_back(a);

            if (index > 0) {
                int prev = numbers[index-1];

                if (index == 1 && prev > a) {
                    increasing = false;
                }

                if (abs(prev-a) < 1 || abs(prev-a) > 3) {
                    safe = false;
                    break;
                }
                if (prev > a && increasing) {
                    safe = false;
                    break;
                }
                if (prev < a && !increasing) {
                    safe = false;
                    break;
                }
            }
        }
        if (safe) 
            count++;
    }
    input.close();

    cout << count << '\n';

    return 0;
}