#include "decl.h"

void solve(vector<int>& cards, int maxNumb) {
    int ret = 0;

    for(vector<int>::size_type i=0; i < cards.size(); i++) {
        for(vector<int>::size_type j=i+1; j < cards.size();j++) {
            for(vector<int>::size_type k=j+1; k < cards.size(); k++) {
                if(max(ret, cards[i] + cards[j] + cards[k]) <= maxNumb)
                    ret = max(ret, cards[i] + cards[j] + cards[k]);
            }
        }
    }

    cout << ret << endl;
} 


int main() {
    int N, M;
    cin >> N >> M;

    vector<int> cards(N);

    for(vector<int>::size_type i=0; i<cards.size(); i++)
        cin >> cards[i];

    solve(cards, M);
}   