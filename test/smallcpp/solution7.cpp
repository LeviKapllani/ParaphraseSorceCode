#include<string>
#include<iostream>
#include<sstream>
#include<assert.h>
#include<cstdio>
#include<map>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<queue>


using namespace std;

vector<string> engines;
vector<string> queries;

string readEngine()
{
    string x;
    while(x=="") getline(cin,x);
    return x;
}

int solve(int S,int Q)
{
    if(Q==0) return 0;
    string curr=queries[0];
    int c=-1;
    for (int i=0;i<Q;i++) if(curr==queries[i])
    {
        c++;
        map<string,bool> seen;
        int sn=0;
        for (int j=i;j<Q;j++)
        {
            if(seen.count(queries[j])) continue;
            else if(sn==S-1)
            {
                sn=S;
                
                curr=queries[j];
                break;
            }
            else
            {
                seen[queries[j]]=true;
                sn++;
            }
        }
        if(sn<S) break;

    }
    
    return c;
}

int main()
{
    int N;
    cin>>N;
    for (int i=1;i<=N;i++)
    {
        cout<<"Case #"<<i<<": ";
        int S,Q;
        cin>>S;
        engines.resize(S);
        for (int j=0;j<S;j++) engines[j]=readEngine();
        cin>>Q;
        queries.resize(Q);
        for (int j=0;j<Q;j++) queries[j]=readEngine();
        
        cout<<solve(S,Q)<<endl;
    }
    
    
    

    return 0;
}
