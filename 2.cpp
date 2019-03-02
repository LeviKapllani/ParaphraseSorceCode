#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <sstream>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ext/hash_map>
#include <ext/hash_set>

#define eps 1e-9

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define forit(i, s) for(__typeof(s.begin()) i = s.begin(); i != s.end(); i++)
#define sz(v)((v).size())

#define fi first
#define se second
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef unsigned long long ull;
typedef double dbl;
typedef long double ldbl;

using namespace std;


map < long long, int > dp[12];
ll p[5];
int dic[155][26], ans[12], mod = 10009, u[5], v[5];

void unpack( long long x )
{
  for (int i = 0; i < 5; i++)
    u[i] = x % 1000, x /= 1000;
}

ll pack()
{
  ll res = 0;
  for (int i = 4; i >= 0; i--)
    res = res * 1000 + v[i];
  return res;
}

int main( void )
{
  int tn;
  scanf("%d", &tn);

  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d:", tt);

    char _s[1000];
    scanf("%s", _s);
    string s= _s;
    s += "+";
    vector <string> parts;
    string curr;
    for (int i = 0; i < (int)s.size(); i++)
    {
      if (s[i] == '+')
      {
        parts.pb(curr);
        curr = "";
      }
      else
        curr += s[i];
    }

    p[0] = 1;
    p[1] = 1000;
    p[2] = 1000000;
    p[3] = 1000000000;

    int k, n;
    scanf("%d%d", &k, &n);
    for (int i = 0; i < n; i++)
    {
      string curr;
      cin >> curr;
      memset(dic[i], 0, sizeof(dic[i]));
      for (int j = 0; j < (int)curr.size(); j++)
        dic[i][curr[j] - 'a']++;
    }                 

    for (int i = 1; i <= k; i++)
      ans[i] = 0;

    for (int i = 0; i < (int)parts.size(); i++)
    {
      cerr << i << endl;
      int tmp[26];
      string s = parts[i];
      memset(tmp, 0, sizeof(tmp));

      for (int i = 0; i < (int)s.size(); i++)
        tmp[s[i] - 'a']++;

      vector < pair <int, int> > poly;
      for (int i = 0; i < 26; i++)
        if (tmp[i])
          poly.pb(mp(tmp[i], i));

      sort(poly.begin(), poly.end());
/*      for (int i = 0; i < poly.size(); i++)
        printf("(%d %d)\n", poly[i].fi, poly[i].se);*/

      for (int i = 0; i <= k; i++)
        dp[i].clear();

      dp[0][0] = 1;

      for (int i = 0; i <= k; i++)
      {
        cerr << "k = " << i << " " << dp[i].size(); 
        forit(j, dp[i])
        {
          ll a = j->first;
          int c = j->second;
//          fprintf(stderr, "%I64d : %d\n", a, c);
          
          unpack(a);
          long long add = 1;
          for (int x = 0; x < (int)poly.size(); x++)
            for (int y = 0; y < (int)poly[x].first; y++)
              add = (add * u[x]) % mod;
          ans[i] = (ans[i] + add * c) % mod;

          if (i == k)
            continue;

          for (int x = 0; x < n; x++)
          {
            for (int y = 0; y < (int)poly.size(); y++)
             v[y] = u[y] + dic[x][poly[y].second];

/*            for (int x = (int)poly.size(); x >= 1; x--)
              for (int y = 0; y + 1 < x; y++)
                if (poly[y].fi == poly[y + 1].fi && v[y] > v[y + 1])
                  swap(v[x], v[x + 1]);*/
             
            ll to = pack() ;
            dp[i + 1][to] += c;
          }
        }
      }
    }

    for (int i = 1; i <= k; i++)
      cout << " " << (ans[i] % mod);
    cout << endl;
  }

  return 0;
}