#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
using namespace std;

int main() {
    int result1 = 0, result2 = 0, size = 0;
    vector<int> list1, list2;

    // open file
    fstream input;
	input.open("input.txt", ios::in);

    string line;
    while (getline(input, line)) {
        istringstream iss(line);
        int a, b;
        if (iss >> a >> b) { // Parse the integers from the line
            list1.push_back(a);
            list2.push_back(b);
            size++;
        }
    }
    input.close();

    // sort both lists
    sort(list1.begin(), list1.end());
    sort(list2.begin(), list2.end());

    for (int i = 0; i < size; i++) {
        // Part 1
        result1 += abs(list1[i] - list2[i]);
        // Part 2
        int current = list1[i];
        int count = 0;
        for (int j = 0; j < size; j++) {
            if (list2[j] == current) 
                count++;
        }
        result2 += current * count;
    }

    cout << "Part 1: " << result1 << '\n';
    cout << "Part 2: " << result2 << '\n';

    return 0;
}