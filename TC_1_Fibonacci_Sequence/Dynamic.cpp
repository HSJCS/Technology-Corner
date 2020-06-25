#include <iostream>
#include <vector>
using namespace std;

long long fib(int n, vector<long long> &dp) {
    if(n == 1 || n == 2)
        return 1;
    
    if(dp[n] != 0)
        return dp[n];
        
    return dp[n] = fib(n-1, dp)+fib(n-2, dp); 
}

int main() {
    int n;
    cin >> n;
    vector<long long> dp(101);
    cout << fib(n, dp);
}
