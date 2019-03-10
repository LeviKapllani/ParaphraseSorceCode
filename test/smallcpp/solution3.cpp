#include <cstdio>
#include <cstring>
#include <map>
#include <string>

using namespace std;

map<string, int> ff;

char str[1000];
int a[1000], b[1000];

int main() {
  freopen("a.in","r",stdin);
  int i, j, k, r, t, n, m, testcases;
  scanf("%d",&testcases);
  for (t = 1; t <= testcases; t++) {
    scanf("%d",&n);
    gets(str);
    ff.clear();
    for (i = 0; i < n; i++) {
      gets(str);
      ff[str] = i;
    }
    for (i = 0; i < n; i++) a[i] = 0;
    scanf("%d",&m);
    gets(str);
    for (i = 0; i < m; i++) {
      gets(str);
      j = ff[str];
      if (j < 0 || j >= n) {
	printf("!!!\n");
	exit(0);
      }
      for (k = 0; k < n; k++) b[k] = a[k];
      a[j] = m;
      for (k = 0; k < n; k++) if (k != j){
	for (r = 0; r < n; r++) {
	  if (b[r] + 1 < a[k]) a[k] = b[r] + 1;
	}
      }
    }
    j = m;
    for (i = 0; i < n; i++) if (a[i] < j) j = a[i];
    printf("Case #%d: %d\n", t, j);
  }
  return 0;
}
