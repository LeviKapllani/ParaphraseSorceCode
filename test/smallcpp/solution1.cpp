#include <cstdio>
#include <cstring>
#include <algorithm>
#define MIN(a,b) (a)<(b)?(a):(b)
using namespace std;
int N,M;

char dic[110][110];
char buf[110];
int dp[2][110];

int main()
{
	freopen("A-small.out","w",stdout);
	int t,st,i,j,k;
	int pre,last,mm;
	scanf("%d",&st);
	for (t=0;t<st;++t)
	{
		scanf("%d%*c",&N);
		for (i=0;i<N;++i) gets(dic[i]);
		scanf("%d%*c",&M);
		pre=0;last=1;
		memset(dp[1],0x7f,sizeof(dp[0]));
		memset(dp[0],0,sizeof(dp[0]));
		for (i=0;i<M;++i)
		{
			pre^=1;last^=1;
			gets(buf);
			for (j=0;j<N;++j)
			{//from dp[i][j] to dp[i][k]
				if (strcmp(buf,dic[j])!=0)
				{
					for (k=0;k<N;++k)
					{
						if (k!=j) dp[pre][k] = MIN(dp[pre][k],dp[last][j]+1);
						else dp[pre][k] = MIN(dp[pre][k],dp[last][j]);
					}
				}
			}
			//memcpy(dp[last],dp[pre],sizeof(dp[0]));
			memset(dp[last],0x7f,sizeof(dp[0]));
		}
		for (i=0;i<N;++i)
		{
			if (i==0 || mm>dp[pre][i]) mm=dp[pre][i];
		}
		printf("Case #%d: %d\n",t+1,mm);
	}
	return 0;
}



