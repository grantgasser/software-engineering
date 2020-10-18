// VI.l0 The following code sums the digits in a number. What is its big 0 time?
int sumDigits(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

// easy way to store and shave off last digit
// n % 10
// n /= 10 
// in python do: n = n // 10

// DIFF: time complexity of algo that counts digits?
// as it grows order of magnitude (i.e. 10x)
// 123 => 3
// 1234 => 4
// 12345 => 5

/* grows by one for each order of magnitude! so its O(log N), base-10 to be exact
>>> np.log10(123)
2.089905111439398
>>> np.log10(1234)
3.091315159697223
>>> np.log10(12345)
4.091491094267951
>>> np.log10(123456)
5.091512201627772
*/