#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

mutex mtx;
int counter = 0;

void increment() {
    for (int i = 0; i < 1000000; i++) {
        // Acquire lock for thread
        unique_lock<mutex> lock(mtx);
        counter++;
    }
}

void sequential_increment() {
    int seqCounter = 0;
    for (int i = 0; i < 1000000; i++) {
        seqCounter++;
    }
}

int main() {

    auto start_time = chrono::high_resolution_clock::now();

    thread t1(increment);
    thread t2(increment);
    t1.join();
    t2.join();

    auto end_time = chrono::high_resolution_clock::now();

    cout << "Increment result: " << counter << endl;

    auto elapsed_time = chrono::duration_cast<chrono::milliseconds>(end_time - start_time).count();
    cout << "Elapsed time: " << elapsed_time << "ms" << endl << endl;

    // Sequential
    auto start = chrono::high_resolution_clock::now();
    sequential_increment();
    auto end = chrono::high_resolution_clock::now();

    auto total = chrono::duration_cast<chrono::milliseconds>(end_time - start_time).count();
    cout << "Sequential Total:" << total << "ms" << endl;

    return 0;
}


