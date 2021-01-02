#include "decl.h"

int N, ret=0;
vector<int> val;

void splitNum(int n){
    while(n!=0) {
        val.push_back(n%10);
        n/=10;
    }
}

int solve(int N) {
    if(N<100) return N; //기저사례 : 입력받은 수가 100 미만
    if(N == 1000) ret -= 1; // 기저사례 : 입력받은 수가 1000

    for(int i=100; i<=N; ++i) {
        splitNum(i);

        if((val[2] - val[1]) == (val[1]-val[0]))
            ret += 1;

        val.clear();
    }
    return ret+99;
}

int main() {
    cin >> N;

    cout << solve(N) <<endl;
}