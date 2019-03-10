#include <vector>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <fstream>
#include <iomanip>

using namespace std;

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define fr(i, n) for(i = 0; i < (n); i++)
#define fr2(i, s, n) for(i = (s); i < (n); i++)

typedef long long ll;
#define mp make_pair
typedef vector<int> VI;
typedef vector<string> VS;
typedef istringstream ISS;
typedef ostringstream OSS;
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

const int INF = 1 << 20;

int NT;
int S, Q;
string s[2000];
string q[2000];
int dp[2000][200];

void read(ifstream &fin)
{
 string ln;
 int i;

 getline(fin, ln);
 ISS isS(ln);
 isS >> S;
 fr(i, S) getline(fin, s[i]);

 getline(fin, ln);
 ISS isQ(ln);
 isQ >> Q;
 fr(i, Q) getline(fin, q[i]);
}

void proc(ofstream &fout)
{
 int i, j, k;

 fr(i, Q) fr(j, S)
 {
  if(q[i] == s[j])
   dp[i][j] = INF;
  else if(i > 0)
  {
   dp[i][j] = dp[i-1][j];
   fr(k, S) dp[i][j] = min(dp[i][j], dp[i-1][k] + 1);
  }
  else
   dp[i][j] = 0;
 }

 int res = INF;

 fr(i, S)
  res = min(res, dp[Q-1][i]);

 fout << res << endl;
}

int main()
{
 int i;

 ifstream fin("input.txt");
 ofstream fout("output.txt");
 string ln;

 getline(fin, ln);
 istringstream is(ln);
 is >> NT;

 fr(i, NT)
 {
  read(fin);
  fout << "Case #" << i + 1 << ": ";
  proc(fout);
 }

 return 0;
}
