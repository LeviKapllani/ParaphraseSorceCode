
#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int query[1000];
int best[1000];

int main()  {
  ofstream fout("A-large.out");
  ifstream fin("A-large.in");
  
  int i, j, N;
  fin >> N; cout << N << endl;
  for (int t = 1; t <= N; t++) {
    int S, Q;
    fin >> S; cout << S << endl;
    map <string, int> index;
    
    for (i = 0; i < S; i++) {
      string s; getline(fin, s);
      if (s.size() == 0) getline(fin, s);
      cout << s << endl;
      index[s] = i;
    }
    
    fin >> Q; cout << Q << endl;
    if (Q == 0) {
      fout << "Case #" << t << ": " << 0 << endl;
      continue;
    }
    for (i = 0; i < Q; i++) {
      string q; getline(fin, q);
      if (q.size() == 0) getline(fin, q);
      cout << q << endl;
      query[i] = index[q];
    }
    
    // let c1..cq be the counts
    // if min(ci) = 0, ans = 0
    // so extend backwards
    best[Q-1] = 0;
    for (i = Q-2; i >= 0; i--) {
      best[i] = 1000;
      
      int count = S;
      bool used[100];
      for (j = 0; j < S; j++) used[j] = false;
      
      for (j = i; j < Q; j++) {
        if (!used[query[j]]) {
          used[query[j]] = true;
          count--; 
        }
        best[i] = min(best[i], best[j] + 1);
        if (count == 0) break;
      }
      
      if (j == Q) best[i] = 0;
    }
    
    fout << "Case #" << t << ": " << best[0] << endl;
  }
  
  fin.close();
  fout.close();
  
  system("pause");
  
  return 0;
}
