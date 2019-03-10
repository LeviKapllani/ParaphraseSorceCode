#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const int MAXN = 110;
const int MAXM = 1100;

string engine[MAXN], query[MAXM];
bool match[MAXM][MAXN];
int f[MAXM][MAXN];
int n, m;

void init()
{
	int i, j;
	
	cin >> n;
	getline(cin, engine[0]);
	for (i=1; i<=n; i++)
		getline(cin, engine[i]);
	cin >> m;
	getline(cin, query[0]);
	for (i=1; i<=m; i++)
		getline(cin, query[i]);
	for (i=1; i<=n; i++)
		for (j=1; j<=m; j++)
			if (engine[i]==query[j]) match[j][i]=true; else match[j][i]=false;
}

void work()
{
	int i, j, k, value, best;
	
	if (m==0){
		cout << 0 << endl;
		return;
	}
	memset(f, 0xFF, sizeof(f));
	for (i=1; i<=n; i++)
		if (!match[1][i])
			f[1][i]=0;
	for (i=2; i<=m; i++)
		for (j=1; j<=n; j++) 
			if (!match[i][j]){
				for (k=1; k<=n; k++)
					if (f[i-1][k]!=-1){
						if (j==k) value=0; else value=1;
						if (f[i][j]==-1 || f[i][j]>f[i-1][k]+value)
							f[i][j]=f[i-1][k]+value;
					}
			}
	best=-1;
	for (i=1; i<=n; i++)
		if ((best==-1 || best>f[m][i]) && f[m][i]!=-1)
			best=f[m][i];
	cout << best << endl;
}

int main()
{
	int cas=0, t;
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	while (t--){
		cas++;
		cout << "Case #" << cas << ": ";
		init();
		work();
	}
			
	return 0;
}
