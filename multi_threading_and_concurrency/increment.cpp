#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

mutex mtx;
int counter = 0;

void increment() {
    for (int i = 0; i < 10000; i++) {
        // Acquire lock for thread
        unique_lock<mutex> lock(mtx);
        counter++;
    }
}

int main() {

    thread t1(increment);
    thread t2(increment);
    t1.join();
    t2.join();

    cout << "Increment result: " << counter << endl;

    return 0;
}


