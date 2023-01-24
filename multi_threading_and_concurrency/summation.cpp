#include <iostream>
#include <thread>
#include <numeric>
#include <vector>

using namespace std;

int sum(const vector<int>& v, size_t start, size_t end, int& result) {
    result = accumulate(v.begin() + start, v.begin() + end, 0);
}

int main() {
    vector<int> v = {1,2,3,4,5,6,7,8,9,10};
    int sum1, sum2;

    // Create two threads
    // Summing/accumulating is atomic, hence need for locks to avoid race conditions
    thread t1(sum, ref(v), 0, v.size() / 2, ref(sum1));
    thread t2(sum, ref(v), v.size() / 2, v.size(), ref(sum2));

    // Release threads
    t1.join();
    t2.join();

    cout << "Summation result: " << sum1 + sum2 << endl;

    return 0;
}